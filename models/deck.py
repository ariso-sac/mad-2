from pytz import timezone
from models import db


class Decks(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(20), unique=True)
    created_on = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    updated_on = db.Column(
        db.DateTime(timezone=True), server_default=db.func.now(), server_onupdate=db.func.now()
    )

    # def GetDict(self):
    #     return {'id': self.id, 'name': self.name}
    def GetDict(self):
        return {
            "id": self.id,
            "name": self.name,
            "created_on": str(self.created_on),
            "updated_on":str(self.updated_on)
        }
