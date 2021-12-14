from flask_app import app
from flask import render_template, redirect, session, request, flash

from flask_app.models import model_user #import all model tables 


@app.route('/')
def index():
    return render_template('index.html')

#@app.errorhandler(404)
#def server_error(e):
#    print('running error function')
#    return render_template('error.html')