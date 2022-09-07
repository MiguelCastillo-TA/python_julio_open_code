from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'csdvdf'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    age = request.form['age']
    print(name)
    session['ninja'] = {
        'name': name,
        'age': age
    }
    return redirect('/results')

@app.route('/results')
def results():
    return render_template('results.html')

if __name__ == "__main__":
    app.run(debug=True)