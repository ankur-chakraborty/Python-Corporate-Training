from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", 'dev_secret')

db = SQLAlchemy(app)
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), nullable=False, default='Pending')
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'created_at': self.created_at.isoformat()
        }

    def __repr__(self):
        return f'<Task {self.id}-{self.title}>'

@app.route('/')
def index():
    tasks = Task.query.order_by(Task.created_at.desc()).all()
    return render_template('index.html', tasks=tasks)

@app.route('/tasks', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        title = request.form.get('title',"").strip()
        description = request.form.get('description',"").strip()
        if not title:
            flash('Title is required.', 'error')
            return redirect(url_for('add_task'))

        new_task = Task(title=title, description=description or None)
        db.session.add(new_task)
        db.session.commit()
        flash('Task successfully added!', 'success')
        return redirect(url_for('index'))
    return render_template('add_edit.html', task = None)

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    if request.method == 'POST':
        title = request.form.get('title',"").strip()
        description = request.form.get('description',"").strip()
        if not title:
            flash('Title is required.', 'error')
            return redirect(url_for('edit_task', task_id=task_id))
        task.title = title
        task.description = description
        db.session.commit()
        flash('Task successfully edited!', 'success')
        return redirect(url_for('index'))
    return render_template('add_edit.html', task = task)

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.status = 'completed' if task.status == 'Completed' else 'failed'
    db.session.commit()
    flash('Task status changed.', 'success')
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted.', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)