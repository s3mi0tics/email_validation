from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models import model_user


@app.route('/user/create', methods = ['POST'])
def user_create():
    if not model_user.User.validate_email(request.form):
        return redirect('/')
    model_user.User.create(request.form)
    return redirect ('/user/success')

@app.route('/user/success')
def success():
    context = {
        'all_users' : model_user.User.get_all()
    }
    return render_template("success.html", **context)



#/user/new ->display
#/user/create ->action
#/user/<int:id> ->display
#/user/<int:id>/edit ->display
#/user/<int:id>/update ->action
#/user/<int:id>/delete ->action