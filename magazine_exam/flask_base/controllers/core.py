import os

from flask import flash, redirect, render_template, request, session
from flask_base import app
from flask_base.models.magazine import Magazine
from flask_base.models.usuario import Usuario
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route("/")
@app.route("/dashboard")
def index():

    if 'usuario' not in session:
        flash('Primero tienes que logearte', 'error')
        return redirect('/login')
   
    return render_template("index.html", all_magazines = Magazine.get_all())

@app.route('/user/account')
def account():
    if 'usuario' not in session:
        flash('Primero tienes que logearte', 'error')
        return redirect('/login')
    all_user_magazines = Magazine.get_all_user_magazines(session['user_id'])
    print(all_user_magazines)
    return render_template("account.html", user = Usuario.get_by_id(session['user_id']), all_magazines = all_user_magazines)

@app.route('/account/update', methods=['post'])
def update_account():
    if not Usuario.validar_update(request.form):
        return redirect('/login')

    data = {
        'id': session['user_id'],
        'name': request.form['name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    updated_user = Usuario.update(data)
    if updated_user == False:
        flash('failed to update account', 'error')
    print(updated_user)
    flash('Update was succesful', 'success')
    return redirect('/user/account')

@app.route("/login")
def login():

    if 'usuario' in session:
        flash('Ya estás LOGEADO!', 'warning')
        return redirect('/')

    return render_template("login.html")

@app.route("/procesar_registro", methods=["POST"])
def procesar_registro():

    if not Usuario.validar(request.form):
        return redirect('/login')

    pass_hash = bcrypt.generate_password_hash(request.form['password'])

    data = {
        'name' : request.form['name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'password' : pass_hash,
    }

    resultado = Usuario.save(data)

    if not resultado:
        flash("error al crear el usuario", "error")
        return redirect("/login")

    flash("Usuario creado correctamente", "success")
    return redirect("/login")


@app.route("/procesar_login", methods=["POST"])
def procesar_login():

    usuario = Usuario.buscar(request.form['identificacion'])

    if not usuario:
        flash("Usuario/Correo/Clave Invalidas", "error")
        return redirect("/login")

    if not bcrypt.check_password_hash(usuario.password, request.form['password']):
        flash("Usuario/Correo/Clave Invalidas", "error")
        return redirect("/login")

    session['usuario'] = usuario.name
    session['user_id'] = usuario.id
    
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')
