from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage
records = []


@app.route("/", methods=["GET", "POST"])
def index():
    error = None

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        age = request.form.get("age", "").strip()
        interest = request.form.get("interest", "").strip()
        level = request.form.get("level", "")
        description = request.form.get("description", "").strip()

        if not name:
            error = "Name cannot be empty."
        elif not age.isdigit():
            error = "Age must be a number."
        else:
            records.append({
                "name": name,
                "age": int(age),
                "interest": interest,
                "level": level,
                "description": description
            })
            return redirect(url_for("index"))

    return render_template("index.html", records=records, error=error)


if __name__ == "__main__":
    app.run(debug=True)
