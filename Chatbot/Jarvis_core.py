import os
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

import sounddevice as sd
import numpy as np
import wave
import subprocess
import ollama
import uuid
import time
import platform
import torch

# ========== CONFIGURATION ==========
STT_MODEL = "base"
LLM_MODEL = "llama3.2:3b"
TTS_MODEL = "en_US-danny-low.onnx"
SAMPLE_RATE = 48000
SILENCE_LIMIT = 2.0           # Stop recording after 2 seconds of silence

conversation_history = []
MAX_HISTORY = 6

LLM_OPTIONS = {
    "num_predict": 120,        # Longer responses
    "temperature": 0.5,
    "top_k": 20,
    "top_p": 0.8,
    "repeat_penalty": 1.1,
}

# ========== ONE-TIME MODEL LOADING ==========
print("[ Loading STT model... ]")
from faster_whisper import WhisperModel

device = "cuda" if torch.cuda.is_available() else "cpu"
compute_type = "float16" if device == "cuda" else "int8"
print(f"[ STT device: {device} ]")

stt_model = WhisperModel(STT_MODEL, device=device, compute_type=compute_type)

print("[ Loading wake word model... ]")
from openwakeword.model import Model
wake_model = Model(wakeword_models=["hey_jarvis"], inference_framework="onnx")
print("[ All models ready ]")

# ========== AUDIO CAPTURE WITH WAKE WORD ==========
def record_audio():
    """Waits for 'Hey Jarvis', then records until you stop talking"""
    print("\n[ Say 'Hey Jarvis' to wake... ]")
    
    # Phase 1: Wait for wake word
    stream = sd.InputStream(samplerate=16000, channels=1, dtype='int16', blocksize=1280)
    stream.start()
    
    while True:
        chunk, _ = stream.read(1280)
        prediction = wake_model.predict(chunk.flatten())
        if prediction.get("hey_jarvis", 0) > 0.5:
            stream.stop()
            stream.close()
            print("[ Listening... ]")
            time.sleep(0.3)
            break
    
    # Phase 2: Record until silence (stops automatically)
    buffer = []
    silence_frames = 0
    speech_detected = False
    
    stream = sd.InputStream(samplerate=SAMPLE_RATE, channels=1, dtype='float32')
    stream.start()
    
    while True:
        chunk, _ = stream.read(int(SAMPLE_RATE * 0.1))
        chunk = chunk.flatten()
        buffer.extend(chunk)
        
        # Check if this chunk contains speech
        if np.max(np.abs(chunk)) > 0.01:
            speech_detected = True
            silence_frames = 0
        elif speech_detected:
            silence_frames += 0.1
        
        # Stop after silence
        if speech_detected and silence_frames >= SILENCE_LIMIT:
            break
        
        # Timeout after 15 seconds
        if len(buffer) >= SAMPLE_RATE * 15:
            break
    
    stream.stop()
    stream.close()
    
    if not speech_detected:
        print("[ No speech detected ]")
        return None
    
    audio = np.array(buffer)
    
    # Trim silence from both ends
    threshold = 0.01
    non_silent = np.where(np.abs(audio) > threshold)[0]
    audio = audio[non_silent[0]:non_silent[-1] + 1]
    
    if len(audio) < SAMPLE_RATE * 0.3:
        print("[ Speech too short ]")
        return None
    
    recording_file = f"rec_{uuid.uuid4().hex[:8]}.wav"
    with wave.open(recording_file, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes((audio * 32767).astype(np.int16).tobytes())
    
    print("[ Transcribing... ]")
    return recording_file

# ========== TRANSCRIPTION ==========
def transcribe(filepath):
    segments, _ = stt_model.transcribe(
        filepath,
        beam_size=5,
        language="en",
        task="transcribe",
        vad_filter=True,
        vad_parameters=dict(
            threshold=0.5,
            min_speech_duration_ms=250,
            min_silence_duration_ms=400,
        )
    )
    text = " ".join([seg.text for seg in segments]).strip()
    print(f"[ You ]: {text}")
    
    try:
        os.remove(filepath)
    except:
        pass
    return text

# ========== GARBLED TEXT DETECTION ==========
def is_garbled(text):
    words = text.split()
    if len(words) < 2:
        return False
    from collections import Counter
    word_counts = Counter(words)
    most_common_count = word_counts.most_common(1)[0][1]
    return most_common_count > len(words) * 0.5

# ========== LLM RESPONSE ==========
def jarvis_think(prompt):
    """Non-streaming for faster, cleaner output"""
    global conversation_history
    
    conversation_history.append({'role': 'user', 'content': prompt})
    if len(conversation_history) > MAX_HISTORY:
        conversation_history = conversation_history[-MAX_HISTORY:]
    
    print("[ Jarvis ]: ", end="", flush=True)
    
    try:
        response = ollama.chat(
            model=LLM_MODEL,
            messages=conversation_history,
            options=LLM_OPTIONS
        )
        full_response = response['message']['content'].strip()
        print(full_response)
    except Exception as e:
        print(f"[ LLM error: {e} ]")
        full_response = "I encountered an error."
    
    if full_response and not is_garbled(full_response):
        conversation_history.append({'role': 'assistant', 'content': full_response})
    
    return full_response

# ========== TEXT-TO-SPEECH ==========
def speak(text):
    if not text.strip():
        return
    
    audio_file = f"tts_out_{uuid.uuid4().hex[:8]}.wav"
    
    try:
        result = subprocess.run([
            "piper",
            "--model", TTS_MODEL,
            "--output_file", audio_file
        ], input=text.encode(), capture_output=True)
        
        if result.returncode != 0:
            return
        
        if not os.path.exists(audio_file) or os.path.getsize(audio_file) < 100:
            return
        
        import winsound
        winsound.PlaySound(audio_file, winsound.SND_FILENAME)
    
    except Exception as e:
        print(f"[ Playback error: {e} ]")
    finally:
        try:
            os.remove(audio_file)
        except:
            pass

# ========== MAIN LOOP ==========
def main():
    print("=" * 40)
    print("JARVIS CORE")
    print("Say 'Hey Jarvis' to wake.")
    print("Say 'shutdown' to exit.")
    print("Press Ctrl+C to force quit.")
    print("=" * 40)
    
    while True:
        try:
            # Listen for wake word and record command
            audio_file = record_audio()
            if audio_file is None:
                continue
            
            # Transcribe
            user_text = transcribe(audio_file)
            if not user_text.strip():
                continue
            
            print(f"[ You said ]: {user_text}")
            
            # Simple shutdown check
            if user_text.lower().strip() in ["shutdown", "exit", "quit", "goodbye"]:
                print("[ Shutting down ]")
                speak("Shutting down. Goodbye.")
                break
            
            # Get response and speak
            response = jarvis_think(user_text)
            speak(response)
        
        except KeyboardInterrupt:
            print("\n[ Shutting down ]")
            break
        except Exception as e:
            print(f"[ Error: {e} ]")
            time.sleep(0.5)
            continue

if __name__ == "__main__":
    main()