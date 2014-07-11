from flask import Flask
from flask import render_template, redirect, url_for
from flask import request
from flask import Response
from flask.ext.pymongo import PyMongo
import voice
import os
import json
from task_model import Task_Model

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir, static_folder='public', static_url_path='')
#mongo = PyMongo(app)
task_model = Task_Model()

@app.route('/')
@app.route('/task/<selected_task>')
def home(selected_task = None):
    return render_template('task.html', tasks=map(json.dumps,task_model.get_all_tasks()), selected_task = selected_task) 

@app.route('/add_task', methods = ['POST'])
def add_task():
    task_model.add_task(request.form['task'])
    return redirect(url_for('home'))

@app.route('/rand_sel', methods = ['POST'])
def rand_sel():
    task = task_model.randomly_select_task()
    voice.say(task)
    return redirect(url_for('home', selected_task = task) )

@app.route('/remove_task', methods = ['POST'])
def remove_task():
   task = request.form['task'] 
   task_model.remove_task(task)
   return redirect(url_for('home'))


if (__name__ == "__main__"):
    app.debug = True
    app.run()
    


















