// Wait for the page to load before running code
document.addEventListener("DOMContentLoaded", () => {
    loadTasks();
    
    document.getElementById("addBtn").addEventListener("click", addTask);
    
    document.getElementById("taskInput").addEventListener("keypress", (e) => {
        if (e.key === "Enter") addTask();
    });
    
    document.getElementById("taskInput").addEventListener("keydown", (e) => {
        if (e.key === "Escape") e.target.value = "";
    });
    
    document.getElementById("clearCompletedBtn").addEventListener("click", async () => {
        await fetch("/api/tasks/clear-completed", { method: "DELETE" });
        loadTasks();
    });
    
    document.getElementById("clearAllBtn").addEventListener("click", async () => {
        if (!confirm("Clear ALL tasks?")) return;
        await fetch("/api/tasks/clear-all", { method: "DELETE" });
        loadTasks();
    });
});
// Fetch tasks from the backend and display them
async function loadTasks() {
    const response = await fetch("/api/tasks");
    const tasks = await response.json();
    
    const taskList = document.getElementById("taskList");
    const emptyState = document.getElementById("emptyState");
    const counter = document.getElementById("counter");
    
    taskList.innerHTML = "";
    
    if (tasks.length === 0) {
        emptyState.classList.add("show");
        counter.textContent = "0 of 0 done";
        return;
    } else {
        emptyState.classList.remove("show");
    }
    
    const doneCount = tasks.filter(t => t.done).length;
    counter.textContent = `${doneCount} of ${tasks.length} done`;
    
    tasks.forEach(task => {
        const li = document.createElement("li");
        li.dataset.id = task.id;
        
        const checkbox = document.createElement("input");
        checkbox.type = "checkbox";
        checkbox.checked = task.done;
        checkbox.addEventListener("change", () => toggleTask(task.id));
        
        const span = document.createElement("span");
        span.textContent = task.text;
        span.classList.add("task-text");
        if (task.done) {
            span.classList.add("done");
        }
        // Double-click to edit
        span.addEventListener("dblclick", () => startEditing(li, task));
        
        const deleteBtn = document.createElement("button");
        deleteBtn.textContent = "✕";
        deleteBtn.classList.add("delete-btn");
        deleteBtn.addEventListener("click", () => deleteTask(task.id));
        
        li.appendChild(checkbox);
        li.appendChild(span);
        li.appendChild(deleteBtn);
        taskList.appendChild(li);
    });
}

// Send a new task to the backend
async function addTask() {
    const input = document.getElementById("taskInput");
    const text = input.value.trim();
    
    if (text === "") {
        alert("Please enter a task.");
        return;
    }
    
    const response = await fetch("/api/tasks", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: text })
    });
    
    if (response.ok) {
        input.value = ""; // Clear input box
        loadTasks();      // Refresh the task list
    }
}

// Toggle task done status
async function toggleTask(id) {
    const response = await fetch(`/api/tasks/${id}`, {
        method: "PUT"
    });
    console.log("Toggle response:", response.status);
    loadTasks();
}
// Delete a task
async function deleteTask(id) {
    const li = document.querySelector(`li[data-id="${id}"]`);
    if (!li) return;
    
    // Inline confirmation
    li.style.opacity = "0.5";
    
    const confirmed = await new Promise((resolve) => {
        const overlay = document.createElement("div");
        overlay.className = "confirm-overlay";
        overlay.innerHTML = `
            <div class="confirm-box">
                <p>Delete this task?</p>
                <button id="confirmYes">Yes</button>
                <button id="confirmNo">No</button>
            </div>
        `;
        document.body.appendChild(overlay);
        
        document.getElementById("confirmYes").onclick = () => {
            document.body.removeChild(overlay);
            resolve(true);
        };
        document.getElementById("confirmNo").onclick = () => {
            document.body.removeChild(overlay);
            resolve(false);
        };
    });
    
    if (!confirmed) {
        li.style.opacity = "1";
        return;
    }
    
    await fetch(`/api/tasks/${id}`, { method: "DELETE" });
    loadTasks();
}
// Start editing a task
function startEditing(li, task) {
    const span = li.querySelector(".task-text");
    const input = document.createElement("input");
    input.type = "text";
    input.value = task.text;
    input.classList.add("edit-input");
    
    li.replaceChild(input, span);
    input.focus();
    input.select();
    
    // Save on Enter
    input.addEventListener("keydown", async (e) => {
        if (e.key === "Enter") {
            await saveEdit(task.id, input.value);
        } else if (e.key === "Escape") {
            loadTasks(); // Cancel edit
        }
    });
    
    // Save on blur (clicking away)
    input.addEventListener("blur", async () => {
        await saveEdit(task.id, input.value);
    });
}

// Save edited task
async function saveEdit(id, newText) {
    const trimmed = newText.trim();
    if (trimmed === "") {
        loadTasks();
        return;
    }
    
    await fetch(`/api/tasks/${id}/edit`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: trimmed })
    });
    loadTasks();
}
