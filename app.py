from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    arr = ["luis","juan","miguel","omar"]
    autor = "miguel"
    return render_template("index.html", nombre = autor,amigos = arr)

@app.route("/p1")
def index1():
    arr = ["Julieta","Miguel"]
    autor = "miguel angel"
    return render_template("p1.html", nombre = autor,papas = arr)

@app.route("/p2")
def index2():
    arr = ["aron","santiago"]
    autor = "miguel angel roman"
    return render_template("p2.html", nombre = autor,hermanos = arr)

@app.route("/p2")
def index3():
    arr = ["angel","ruben","acevedo","brayan"]
    autor = "miguel angel roman padilla"
    return render_template("p3.html", nombre = autor,amigos = arr)

if __name__ == "__main__":
    app.run(debug=True)