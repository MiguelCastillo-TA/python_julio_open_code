from app import app
from app.models.dojo import Dojo
from flask import render_template, redirect, request

@app.route('/')
def index():
    return redirect('/dojos')


@app.route('/dojos')
def dojos_index():
    return render_template('dojos/dojos_index.html', all_dojos=Dojo.get_all())


@app.route('/dojos/process', methods=['POST'])
def process_new_dojo():
    print(request.form)
    data = {
        'name': request.form['name']
    }
    new_dojo = Dojo.add_dojo(data)
    print(new_dojo)
    return redirect('/dojos')


@app.route('/dojos/<int:id>')
def dojo_details(id):
    data = {
        'dojo_id': id
    }
    dojo_ninjas = Dojo.get_dojo_ninjas(data)
    return render_template('dojos/dojo_details.html', dojo=dojo_ninjas)