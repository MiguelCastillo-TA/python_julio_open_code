import os

from flask import flash, redirect, render_template, request, session
from flask_base import app
from flask_base.models.magazine import Magazine


@app.route("/new")
def new_magazine():
    if 'usuario' not in session:
        flash('Primero tienes que logearte', 'error')
        return redirect('/login')

    return render_template('magazine/new_magazine.html')

@app.route('/process_new_magazine', methods=['post'])
def process_new_magazine():
    if not Magazine.validar(request.form):
        return redirect('/new')

    data = {
        'title': request.form['title'],
        'description': request.form['description'],
        'user_id': session['user_id']
    }
    new_magazine = Magazine.save(data)
    print(new_magazine)
    if new_magazine == False:
        flash('Failed to created new magazine', 'error')
        return redirect('/new')
    
    return redirect('/dashboard')


@app.route('/show/<int:id>')
def show_magazine(id):
    if 'usuario' not in session:
        flash('Primero tienes que logearte', 'error')
        return redirect('/login')

    return render_template('magazine/show.html', magazine = Magazine.get_by_id(id))

@app.route('/delete/magazine/<int:id>')
def delete_magazine(id):
    deleted_mag = Magazine.delete(id)
    print(deleted_mag)
    return redirect('/dashboard')

    
