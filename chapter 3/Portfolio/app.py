'''For this project I downloaded a template and modified it.'''

from flask import Flask, render_template

app = Flask(__name__)

projects_list = [
    {
        "title": "Composite Laminate Analysis",
        "description": "Modeling and analysis of Sym/Asym composite laminates using MATLAB and ABAQUS.",
        "github": ""
    },
    {
        "title": "Bell AH‑1 Cobra helicopter Analysis",
        "description": "Modeling and structural analysis of The Bell AH‑1 Cobra helicopter under static and dynamic loads.",
        "github": ""
    },
    {
        "title": "Creating a Chess Game",
        "description": "Programming a chess board, movements and interactions of the chess pieces and game rules using C++.",
        "github": ""
    },
    {
        "title": "Calculator",
        "description": "Programing a calculator using Tkinter package in Python.",
        "github": "https://github.com/Pardis-hub/python_masterclass_projects/blob/main/chapter%202/calculator/calculator.py"
    },
    {
        "title": "Gallery",
        "description": "Programing a gallery using Kivy package in Python.",
        "github": "https://github.com/Pardis-hub/python_masterclass_projects/blob/main/chapter%202/gallery/gallery.py"
    }
]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/skills")
def skills():
    return render_template("skills.html")

@app.route("/projects")
def projects():
    return render_template("projects.html", projects=projects_list)

if __name__ == "__main__":
    app.run(debug=True)