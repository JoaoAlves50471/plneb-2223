from flask import Flask, render_template
import os

app= Flask(__name__)

img = os.path.join('static', 'Image')

@app.route("/")
def home():
    file = os.path.join(img, 'montagem.jpg')
    return render_template("homepage.html", title="Homepage",image=file)

@app.route("/elefantes")
def elephants():
    return render_template("elefantes.html", title="Elefantes")
       
@app.route("/engenheiros")
def engineers():
    return render_template("engenheiros.html", title="Engenheiros")
   
@app.route("/eguas")
def mares():
    return render_template("eguas.html", title="Éguas")
    
app.run(host="localhost",port=3000, debug=True)

