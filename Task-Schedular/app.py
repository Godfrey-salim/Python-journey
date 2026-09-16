from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)
DB_FILE = "database.db"


def init_db():
    """Create the tasks table if it doesn't exist."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            done INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()


def get_db():
    """Open a database connection."""
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row  # Allows dict-like access
    return conn


@app.route("/")
def home():
    return render_template("index.html")


# API: Get all tasks
@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    conn = get_db()
    rows = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()
    tasks = [{"id": r["id"], "text": r["text"], "done": bool(r["done"])} for r in rows]
    return jsonify(tasks)


# API: Add a task
@app.route("/api/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    text = data.get("text", "").strip()
    
    if not text:
        return jsonify({"error": "Task cannot be empty"}), 400
    
    conn = get_db()
    cursor = conn.execute("INSERT INTO tasks (text, done) VALUES (?, ?)", (text, 0))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    
    return jsonify({"id": new_id, "text": text, "done": False}), 201


# API: Delete a task
@app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    conn = get_db()
    conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Task deleted"}), 200


# API: Toggle done
@app.route("/api/tasks/<int:task_id>", methods=["PUT"])
def toggle_task(task_id):
    conn = get_db()
    row = conn.execute("SELECT done FROM tasks WHERE id = ?", (task_id,)).fetchone()
    
    if not row:
        conn.close()
        return jsonify({"error": "Task not found"}), 404
    
    new_done = 0 if row["done"] else 1
    conn.execute("UPDATE tasks SET done = ? WHERE id = ?", (new_done, task_id))
    conn.commit()
    conn.close()
    
    return jsonify({"id": task_id, "done": bool(new_done)}), 200


# API: Edit task text
@app.route("/api/tasks/<int:task_id>/edit", methods=["PUT"])
def edit_task(task_id):
    data = request.get_json()
    new_text = data.get("text", "").strip()
    
    if not new_text:
        return jsonify({"error": "Task text cannot be empty"}), 400
    
    conn = get_db()
    result = conn.execute("UPDATE tasks SET text = ? WHERE id = ?", (new_text, task_id))
    conn.commit()
    conn.close()
    
    if result.rowcount == 0:
        return jsonify({"error": "Task not found"}), 404
    
    return jsonify({"id": task_id, "text": new_text}), 200


# API: Clear completed
@app.route("/api/tasks/clear-completed", methods=["DELETE"])
def clear_completed():
    conn = get_db()
    conn.execute("DELETE FROM tasks WHERE done = 1")
    conn.commit()
    conn.close()
    return jsonify({"message": "Completed tasks cleared"}), 200


# API: Clear all
@app.route("/api/tasks/clear-all", methods=["DELETE"])
def clear_all():
    conn = get_db()
    conn.execute("DELETE FROM tasks")
    conn.commit()
    conn.close()
    return jsonify({"message": "All tasks cleared"}), 200


if __name__ == "__main__":
    init_db()
    app.run(debug=True, host="0.0.0.0", port=5000)