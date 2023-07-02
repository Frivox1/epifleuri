from flask import Flask, render_template

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__, instance_relative_config=True)

  @app.route("/")
  def accueil():
    return render_template("index.html")
  
  #Fête des mère
  """@app.route("/fete")
  def fete():
    return render_template("fete.html")"""
  
  """@app.route("/anniversaire")
  def anniv():
    return render_template("anniversaire.html")"""

  @app.route("/produit")
  def prod():
    return render_template("produit.html")

  @app.route("/evenement")
  def event():
    return render_template("evenement.html")

  @app.route("/informations")
  def info():
    return render_template("informations.html")

  return app