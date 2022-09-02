from flask import Flask, render_template, request, redirect, flash, session
import random

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

num = 0

def generate_random_num():
    global num
    num = random.randint(1,100)

@app.route('/')
def index():
    if 'is_playing' not in session:
        generate_random_num()
        session['is_playing'] = True
    print(num)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def check_guess():
    print('trying to guess: ', num)
    user_guess = int(request.form['guess'])
    print(user_guess)
    if user_guess == num:
        session['is_playing'] = False
        flash('You Guess Correct!', 'success')
    elif user_guess < num:
        flash('Too low!', 'error')
    else:
        flash('Too High!', 'error')
    return redirect('/')

@app.route('/restart', methods=['POST'])
def restart_game():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)