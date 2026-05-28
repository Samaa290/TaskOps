import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

# Base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///taskops.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo de tarea
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    priority = db.Column(db.String(20), nullable=False)
    completed = db.Column(db.Boolean, default=False)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    tasks = Task.query.all()
    return render_template("index.html", tasks=tasks)

from flask import request, redirect

@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title")
    priority = request.form.get("priority")

    new_task = Task(title=title, priority=priority)
    db.session.add(new_task)
    db.session.commit()

    return redirect("/")

@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    task = Task.query.get(task_id)
    task.completed = True
    db.session.commit()
    return redirect("/")

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect("/")

@app.route("/edit/<int:task_id>", methods=["POST"])
def edit_task(task_id):
    task = Task.query.get(task_id)

    new_title = request.form.get("title")
    new_priority = request.form.get("priority")

    task.title = new_title
    task.priority = new_priority

    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000, debug=True)