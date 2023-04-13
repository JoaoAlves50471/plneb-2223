from flask import Flask, render_template

app= Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/homepage")
def homepage():
    return render_template("home.html", title="Homepage")

@app.route("/creditos")
def creditos():
    return "<p>Créditos</p>"

@app.route("/termos")
def termos():
    return "<p>Linha de Termos</p>"

app.run(host="localhost",port=3000, debug=True)