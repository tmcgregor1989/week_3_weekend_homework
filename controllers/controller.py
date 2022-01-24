from flask import render_template, request
from app import app
from models.players import Player
from models.game import *

@app.route('/rps')
def index():
    return render_template('rules.html', title='Rock, Paper, Scissors')

# @app.route('/rps/rules')
# def rules():
#     return render_template('rules.html', title="rules")

@app.route('/rps/rock/paper')
def result1():
    return render_template('results.html', title="results", player_1_choice="rock", player_2_choice="paper")

@app.route('/rps/rock/scissors')
def result2():
    return render_template('results.html', title="results", player_1_choice="rock", player_2_choice="scissors")

@app.route('/rps/rock/rock')
def result3():
    return render_template('results.html', title="results", player_1_choice="rock", player_2_choice="rock")


@app.route('/rps/paper/rock')
def result4():
    return render_template('results.html', title="results", player_1_choice="paper", player_2_choice="rock")


@app.route('/rps/paper/scissors')
def result5():
    return render_template('results.html', title="results", player_1_choice="paper", player_2_choice="scissors")


@app.route('/rps/paper/paper')
def result6():
    return render_template('results.html', title="results", player_1_choice="paper", player_2_choice="paper")


@app.route('/rps/scissors/paper')
def result7():
    return render_template('results.html', title="results", player_1_choice="scissors", player_2_choice="paper")


@app.route('/rps/scissors/rock')
def result8():
    return render_template('results.html', title="results", player_1_choice="scissors", player_2_choice="rock")

@app.route('/rps/scissors/scissors')
def result9():
    return render_template('results.html', title="results", player_1_choice="scissors", player_2_choice="scissors")


# @app.route('/rps/play-computer')
# def play_computer():
#     return render_template('index.html', title="play computer")



# @app.route('rps/play-computer', methods=["POST"])
# def play_game():
#     name = request.form['player_1_name']
#     move = request.form['player_1_move']
#     player_1 = Player(name, move)
#     computer_choice = game.pc_choice()
#     computer = Player("computer", computer_choice)
#     game.play_new_game(player_1, computer)
#     return render_template('results.html', title="play computer", player_1=player_1, player_2=computer)



@app.route('/rps/players')
def player_game():
    name_1 = request.form['player_1_name']
    move_1 = request.form['player_1_move']
    name_2 = request.form['player_2_name']
    move_2 = request.form['player_2_move']
    player_1 = Player(name_1, move_1)
    player_2 = Player(name_2, move_2)
    new_game = Game(player_1, player_2)
    outcome = game.play_new_game(new_game)
    return render_template('player_result.html', title="player results", outcome=outcome, player_1=player_1, player_2=player_2)

