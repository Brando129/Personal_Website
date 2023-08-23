from flask_app import app
from flask import render_template, redirect

# Get Routes
# Route for rendering the Home Page.
@app.get('/')
def index():
    return render_template('homepage.html')

# Route for rendering the view Game Vault page.
@app.get('/view_game_vault')
def view_game_vault():
    return render_template('game_vault.html')

# Route for rendering the view Heroes and Villains page.
@app.get('/view_heroes_and_villains')
def view_heroes_and_villains():
    return render_template('heroes_and_villains.html')