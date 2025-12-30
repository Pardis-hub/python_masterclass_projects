from flask import Flask, render_template, request, redirect, send_file
import pandas as pd
import json

app = Flask(__name__)

# In-memory storage
tasks = []
task_id_counter = 1


@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add_task():
    global task_id_counter

    task = {
        "id": task_id_counter,
        "title": request.form["title"],
        "description": request.form["description"],
        "status": request.form["status"]
    }
    tasks.append(task)
    task_id_counter += 1

    return redirect("/")


@app.route("/delete/<int:id>")
def delete_task(id):
    global tasks
    tasks = [t for t in tasks if t["id"] != id]
    return redirect("/")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_task(id):
    task = next(t for t in tasks if t["id"] == id)

    if request.method == "POST":
        task["title"] = request.form["title"]
        task["description"] = request.form["description"]
        task["status"] = request.form["status"]
        return redirect("/")

    return render_template("edit.html", task=task)


@app.route("/import", methods=["POST"])
def import_excel():
    global task_id_counter

    file = request.files["file"]
    df = pd.read_excel(file)

    for _, row in df.iterrows():
        tasks.append({
            "id": task_id_counter,
            "title": row["title"],
            "description": row["description"],
            "status": row["status"]
        })
        task_id_counter += 1

    return redirect("/")


@app.route("/download")
def download_json():
    with open("tasks.json", "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)

    return send_file("tasks.json", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
