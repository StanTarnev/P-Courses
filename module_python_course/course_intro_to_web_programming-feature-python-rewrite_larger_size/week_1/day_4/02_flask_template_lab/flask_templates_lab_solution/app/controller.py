from flask import render_template, request, redirect
from app import app
from app.models.events import events, add_new_event, delete_event
from app.models.event import *

@app.route('/')
def index():
    return render_template('index.html', title='Home', events=events)

@app.route('/add-event', methods=['POST'])
def add_event():
  date = request.form['date']
  name = request.form['name']
  guests = request.form['guests']
  recurring = True if 'recurring' in request.form else False
  roomLocation = request.form['roomLocation']
  description = request.form['description']
  newevent = Event(date=date, name= name, guests=guests, recurring=recurring, room_location=roomLocation, description=description)
  add_new_event(newevent)
  return redirect('/')

@app.route('/delete/<name>', methods=['POST'])
def delete(name):
  delete_event(name)
  return redirect('/')
