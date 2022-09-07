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

if __name__ == "__main__":
    app.run(debug=True)