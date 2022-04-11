from datetime import datetime
from models import db
from flask_restful import Resource
from flask import request
from models.score import Scores
from flask_security import auth_required
import datetime

def GetUser(u_id,d_id):
    d=Scores.query.filter_by(user_id=u_id,deck_id=d_id).first()
    return d

def createScore(Easy,Moderate,Hard,u_id,d_id):
    s=Scores(easy=Easy,moderate=Moderate,hard=Hard,user_id=u_id,deck_id=d_id)
    db.session.add(s)
    db.session.commit()
    return s

class Scores_Api(Resource):

    # @auth_required("token")

    def get(self,d_id,u_id):
        g=GetUser(u_id,d_id)
        if (g==None):
            # dummy data
             return {
            "id": 0,
            "easy": 0,
            "moderate": 0,
            "hard": 0,
            "user_id": 0,
            "deck_id": 0,
            "created_on": str(datetime.datetime.now()),
            "updated_on": str(datetime.datetime.now())
        }
        return g.GetDict()

    def delete(self,d_id,u_id):
        g=GetUser(u_id,d_id)
        if g==None:
            return {"Error":"Not Found"},404
        db.session.delete(g)
        db.session.commit()
        return g.GetDict(),204

    def put(self,d_id,u_id):
        g=GetUser(u_id,d_id)
        if g==None:
            return {"Error":"Not Found"},404
        easy=request.json['easy']
        moderate=request.json['moderate']
        hard=request.json['hard']
        if easy==None or moderate==None or hard==None:
            return {"Error":"Invalid Input"},400
        g.easy=easy
        g.moderate=moderate
        g.hard=hard
        db.session.commit()
        g=GetUser(u_id,d_id)
        return g.GetDict(),200

    def post(self,u_id,d_id):
        easy=request.json['easy']
        moderate=request.json['moderate']
        hard=request.json['hard']
        if easy==None or moderate==None or hard==None:
            return {"Error":"Invalid Input"},400
        #print(name)
        d=createScore(easy,moderate,hard,u_id,d_id)
        return d.GetDict(),201