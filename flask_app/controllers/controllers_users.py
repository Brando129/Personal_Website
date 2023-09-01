from flask_app import app
from flask import render_template, redirect, request, session
import random

# Get Routes
# Route for rendering the Home Page.
@app.get('/')
def index():
    return render_template('homepage.html')

# Route for rendering the Game Vault page.
# @app.get('/game_vault')
# def view_game_vault():
#     return render_template('game_vault.html')

# Route for rendering the view Heroes and Villains page.
# @app.get('/heroes_and_villains')
# def view_heroes_and_villains():
#     return render_template('heroes_and_villains.html')

# Route for rendering the calculator page.
@app.get('/calculator')
def calculator():
    return render_template('calculator.html')

# Route for rendering the clock page.
@app.get('/clock')
def clock():
    return render_template('clock.html')

# Route for rendering the Gold Miner page.
@app.get('/gold_miner')
def gold_miner():
    if 'gold' and 'total_moves' and 'gold_won' not in session:
        session['gold'] = 0
        session['total_moves'] = 15
        session['gold_won'] = []
    return render_template('gold_miner.html')

# Route for reseting Gold Miner session/game.
@app.route('/reset')
def reset():
    session.clear()
    return redirect('/gold_miner')

# Route for rendering the The Wall page.
# @app.get('/wall')
# def wall():
#     return render_template('wall.html')

# Route for rendering the Recipes page.
# @app.get('/recipes')
# def recipes():
#     return render_template('recipes.html')

# Route for rendering Ohana Rideshares page.
# @app.get('/ohana')
# def ohana():
#     return render_template('ohana.html')

# Route for rendering the View Videos page.
@app.get('/view_pictures')
def view_video():
    return render_template('view_pictures.html')


# Post Routes
@app.post('/click/view_pictures')
def click_view_video():
    session['pic_one'] = request.form['pic_one']
    session['pic_two'] = request.form['pic_two']
    session['pic_three'] = request.form['pic_three']
    session['pic_four'] = request.form['pic_four']
    session['pic_five'] = request.form['pic_five']
    session['pic_six'] = request.form['pic_six']
    session['pic_seven'] = request.form['pic_seven']
    session['pic_eight'] = request.form['pic_eight']
    session['pic_nine'] = request.form['pic_nine']
    session['project_name'] = request.form['project_name']
    return redirect('/view_pictures')

# Route for processing gold and number of moves.
@app.post('/process_gold')
def process_gold():
    # Adds gold earned to session
    moves = 1

    # Get the property name from the request
    property_name = request.form['property']

    # Get the winnings for the property
    winnings = {
        'farm': random.randint(10, 20),
        'cave': random.randint(5, 10),
        'house': random.randint(2, 5),
        'casino': random.randint(-50, 50),
    }.get(property_name)

    # Add the winnings to the user's gold
    if winnings is not None:
        session['gold'] += winnings

    # Add the winnings to the user's gold_won list
    session['gold_won'].append(winnings)

    # Subtract one move from the user's total_moves
    session['total_moves'] -= moves

    # Redirect the user to the home page
    return redirect('/gold_miner')