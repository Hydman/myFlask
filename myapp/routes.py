from flask import Blueprint, render_template, request, redirect, url_for
main = Blueprint('main', __name__)

tasks = []

@main.route('/')
def home():
    return render_template('home2.html')

@main.route('/tasks', methods=['GET', 'POST'])
def task_list():
    if request.method == 'POST':
        task = request.form.get('task')
        if task:
            tasks.append(task)
        return redirect(url_for('main.task_list'))
    return render_template('tasks.html', tasks=tasks)