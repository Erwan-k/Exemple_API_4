from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
import os

#from routes.api_routes import exemple_route,exemple_route_all

app = Flask(__name__)
CORS(app)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')


from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Utilisateur(db.Model):
	user = db.Column(db.String(255), unique=True, nullable=False, primary_key=True)
	mdp = db.Column(db.String(255), nullable=False)

	def __init__(self, user, mdp):
		self.user = user
		self.mdp = mdp

db.create_all()

exemple_route_get_args = reqparse.RequestParser()
exemple_route_get_args.add_argument("user",type=str,required=True)
exemple_route_post_args = reqparse.RequestParser()
exemple_route_post_args.add_argument("user",type=str,required=True)
exemple_route_post_args.add_argument("password",type=str,required=True)
exemple_route_put_args = reqparse.RequestParser()
exemple_route_put_args.add_argument("user",type=str,required=True)
exemple_route_put_args.add_argument("password",type=str,required=True)
exemple_route_delete_args = reqparse.RequestParser()
exemple_route_delete_args.add_argument("user",type=str,required=True)

class exemple_route(Resource):
	def get(self):
		body = exemple_route_get_args.parse_args()
		[user] = [body[i] for i in body]
		user = Utilisateur.query.get(user)
		del user.__dict__['_sa_instance_state']
		return jsonify({"retour":"ok","valeur":user.__dict__["mdp"]})

	def post(self):
		body = exemple_route_post_args.parse_args()
		[user,password] = [body[i] for i in body]
		db.session.add(Utilisateur(user,password))
		db.session.commit()
		return jsonify({"retour":"ok"})

	def put(self):
		body = exemple_route_put_args.parse_args()
		[user,password] = [body[i] for i in body]
		db.session.query(Utilisateur).filter_by(user=user).update(dict(mdp=body['password']))
		db.session.commit()
		return jsonify({"retour":"ok"})

	def delete(self):
		body = exemple_route_delete_args.parse_args()
		[user] = [body[i] for i in body]
		db.session.query(Utilisateur).filter_by(user=user).delete()
		db.session.commit()
		return jsonify({"retour":"ok"})

class exemple_route_all(Resource):
	def get(self):
		users = []
		for user in db.session.query(Utilisateur).all():
			del user.__dict__['_sa_instance_state']
			users += [user.__dict__]
		return jsonify({"retour":"ok","valeur":users})

api.add_resource(exemple_route_all,"/exemple_route_all")
api.add_resource(exemple_route,"/exemple_route")

if __name__ == "__main__":
	app.run(debug=True,port=5000,host='0.0.0.0')
