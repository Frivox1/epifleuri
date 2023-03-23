from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def accueil():
  return render_template("index.html")

@app.route("/produit")
def prod():
  return render_template("produit.html")

@app.route("/informations")
def info():
  return render_template("informations.html")


if __name__ == "__main__":
  app.run()