from flask_app import app
from flask import render_template, redirect

# Get Routes
# Route for rendering the Home Page.
@app.get('/')
def index():
    return render_template('homepage.html')