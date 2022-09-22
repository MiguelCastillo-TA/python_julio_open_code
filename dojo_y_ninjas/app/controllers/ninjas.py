from app import app
from app.models.ninja import Ninja
from app.models.dojo import Dojo
from flask import render_template, redirect, request, flash

@app.route('/ninjas')
def ninjas_index():
    return render_template('ninjas/ninjas_index.html', all_dojos=Dojo.get_all())

@app.route('/ninjas/process', methods=['POST'])
def process_new_ninja():
    # print(request.form)
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojos_id': request.form['dojos_id'],
    }
    new_ninja = Ninja.add_ninja(data)
    if new_ninja != False:
        return redirect(f"/dojos/{request.form['dojos_id']}")
    flash('Failed to create Ninja')
    return redirect('/ninjas')
    print(new_ninja)
