from app import app
from app.models.rps import *
from app.models.player import *
from flask import render_template, request

tasks = ["1", "2", "3", "4"]

@app.route('/<hand1>/<hand2>')
def play(hand1, hand2):
    game = Rps()
    player1 = Player("Player 1", hand1)
    player2 = Player("Player 2", hand2)
    winner = game.check_win(player1, player2)
    return render_template('result.html',  **locals())

@app.route('/play')
def play_computer():
    return render_template('play-computer.html', tasks=tasks)


@app.route('/result', methods=['POST'])
def result():
    choice = request.form['choice']
    name = request.form['name']
    game = Rps()
    player1 = Player(name, choice)
    player2 = game.generate_computer_player()
    winner = game.check_win(player1, player2)
    return render_template('result.html', **locals())
