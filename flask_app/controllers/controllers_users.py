from flask_app import app
from flask import render_template, redirect, request, session

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

# Route for rendering the clock page.
@app.get('/clock')
def clock():
    return render_template('clock.html')

# Route for rendering the calculator page.
@app.get('/calculator')
def calculator():
    return render_template('calculator.html')

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
@app.get('/view_video')
def view_video():
    return render_template('view_video.html')


# Post Routes
@app.post('/click/view_video')
def click_view_video():
    session['url'] = request.form['file_path']
    session['project_name'] = request.form['project_name']
    return redirect('/view_video')