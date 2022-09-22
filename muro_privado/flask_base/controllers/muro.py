from flask import flash, redirect, render_template, request, session
from flask_base import app
from flask_base.models.message import Message
from flask_base.models.usuario import Usuario


@app.route("/wall")
def wall():
    if 'usuario' not in session:
        flash('Primero tienes que logearte', 'error')
        return redirect('/login')

    all_users = Usuario.get_all()
    data = {'id': session['usuario_id']}
    all_user_messages = Message.get_all_user_messages(data)
    if all_user_messages:
        total_messages_received = len(all_user_messages)
    else:
        total_messages_received = 0
    user_messages_sent = Message.get_user_message_sent_count(data)
    return render_template('muro/wall.html', all_users=all_users, message_sent_count = user_messages_sent, all_messages = all_user_messages, messages_received_count = total_messages_received)

@app.route("/new/message", methods=["POST"])
def new_message():
    data = {
        'usuario_sent_id': session['usuario_id'],
        'usuario_received_id': request.form['usuario_received_id'],
        'message': request.form['message']
    }
    print(data)
    new_message = Message.save(data)
    print(new_message)
    return redirect('/wall')
