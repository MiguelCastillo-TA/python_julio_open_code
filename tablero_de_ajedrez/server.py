from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<num1>/<num2>')
def index2(num1, num2):
    return render_template('index2.html', num1=int(num1), num2=int(num2))

if __name__=="__main__":
    app.run(debug=True)