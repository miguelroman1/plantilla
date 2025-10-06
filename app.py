from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    autor = "miguel anegel"
    return render_template("index.html", nombre = autor)

if __name__ == "__main__":
    app.run(debug=True)