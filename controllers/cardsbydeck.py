from unittest import result
from models import db
from flask_restful import Resource
from flask import request, render_template
from models import card
from models.card import Cards
from models.deck import Decks
from flask_weasyprint import HTML, render_pdf

def GetCard(id):
    c=Cards.query.filter_by(deck_id=id).all()
    return c

def GetDeck():
    d=Decks.query.order_by(Decks.name).all()
    return d


class AllCrds(Resource):
    def get(self,d_id):
        l=GetCard(d_id)
        les=[]
        for x in l:
            les.append(x.GetDict())
        return les

def GetAll():
    cards=[]
    decks=GetDeck()
    for x in decks:
        k=x.id
        temp=GetCard(k)
        cards.append(temp)
    #print(cards,decks)
    result=""
    for x,y in zip(cards,decks):
        html = render_template('export.html',c=x,d=y)
        result+=html
    return render_pdf(HTML(string=result))
    
