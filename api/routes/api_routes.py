from flask_restful import Resource, reqparse

from models import db,Utilisateur

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

db.create_all()

