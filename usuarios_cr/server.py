from flask import Flask, render_template, request, redirect, flash
from user import User
app = Flask(__name__)
app.secret_key = 'cdscds'


@app.route('/users')
def all_users():
    all_users = User.get_all()
    print(all_users)
    return render_template('index.html', all_users=all_users)


@app.route('/users/new', methods=['GET', 'POST'])
def add_new_user():
    print(f"REQUEST TYPE ", request.method)
    if request.method == 'GET':
        return render_template('addNewUser.html')

    elif request.method == 'POST':
        print(request.form)
        data = {
            "first_name": request.form['first_name'],
            "last_name": request.form['last_name'],
            "email": request.form['email'],
        }
        results = User.insert_user(data)
        if results != False:
            return redirect('/users')
        else:
            flash('There was an error inserting a new user' ,'error')
            return redirect('/users/new')


@app.route('/users/<id>')
def view_user_details(id):
    data = {
        "id": id
    }
    user = User.get_user_by_id(data)
    return render_template('userDetails.html', user=user)


@app.route('/users/<id>/edit', methods=['GET', 'POST'])
def edit_user_details(id):
    if request.method == 'GET':
        data = {
            "id": id
        }
        user = User.get_user_by_id(data)
        return render_template('editUserDetails.html', user=user)

    elif request.method == 'POST':
        print('REACHED EDIT POST')
        data = {
            "first_name": request.form['first_name'],
            "last_name": request.form['last_name'],
            "email": request.form['email'],
            "id": id
        }
        user = User.edit_user_by_id(data)
        return redirect('/users')
        # print('we got ...')
        # print(user)
        # IF STATEMENT TO CHECK FOR ERROR
 
@app.route('/users/<id>/delete')
def delete_user_by_id(id):
    data = {
        "id": id
    }
    user = User.delete_user_by_id(data)
    return redirect('/users')
    
if __name__ == "__main__":
    app.run(debug=True)