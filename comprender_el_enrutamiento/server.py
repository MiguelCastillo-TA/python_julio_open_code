from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return "Hola Mundo!"

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/say/<name>')
def saludo(name):
    return f"Hola {name}!"

@app.route('/repeat/<int:num>/<string:name>')
def repeat(num, name):
    # print(f"{name * 10}", end="\n")
    # john<br>john<br>john<br>john<br>
    # return f"{name * int(num)} <br>"
    response = ""
    for x in range(0, num):
        # print(f"{name}", end="\n")
        response = response + "<h1>" +name + "</h1>"
    print(response)
    return response

# PATIO DE JUEGOS
@app.route('/play')
def play():
    return render_template("play.html")


# CATCH ALL
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return "¡Lo siento! No hay respuesta. Inténtalo otra vez."
