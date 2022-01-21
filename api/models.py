from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Utilisateur(db.Model):
  user = db.Column(db.String(255), unique=True, nullable=False, primary_key=True)
  mdp = db.Column(db.String(255), nullable=False)

  def __init__(self, user, mdp):
    self.user = user
    self.mdp = mdp











