from datetime import datetime
from config import db, ma


# define the Person class that the class inherits, originates from  db.Model
class Person(db.Model):
    __tablename__ = 'person'
    person_id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(32), index=True)
    fname = db.Column(db.String(32))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

""""
 inherits from ma.ModelSchema and gives the PersonSchema class Marshmallow features, 
 like introspecting the Person class to help serialize/deserialize instances of that class.
"""
class PersonSchema(ma.ModelSchema):
    class Meta:
        model = Person
        sqla_session = db.session
