from flask import Flask
from flask import render_template, redirect, url_for
from flask import request
from flask import Response
from flask.ext.socketio import SocketIO, emit
import os
import workout as w

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def home():
    things_to_say = {'Morning':['Good morning Collin', 'Isn\'t it great its a new day', 'Getting up at 3. I like it']}
    print ("Home")
    return render_template('home.html', things_to_say=things_to_say)

@app.route('/workout', methods = ['POST'])
def workout():
    emit('movement', 'That worked')
    w.start_workout(5, 10)
    return redirect(url_for('home'))


@socketio.on('connect')
def we_are_connected():
    print ("We have connected to socketio")
    

if (__name__ == "__main__"):
    app.debug = True
    socketio.run(app)
