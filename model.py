from mongoengine import Document
from mongoengine.fields import (StringField, ListField, ReferenceField)


class Bitcoin(Document):
    meta = {'collection': 'bitcoin'}

    date = StringField(required=True)
    high = StringField(required=True)
    low = StringField(required=True)
    open = StringField(required=True)
    close = StringField(required=True)
    volume = StringField(required=True)


class CrudeOil(Document):
    meta = {'collection': 'crude_oil'}

    date = StringField(required=True)
    high = StringField(required=True)
    low = StringField(required=True)
    open = StringField(required=True)
    close = StringField(required=True)
    volume = StringField(required=True)


class Gold(Document):
    meta = {'collection': 'gold'}

    date = StringField(required=True)
    high = StringField(required=True)
    low = StringField(required=True)
    open = StringField(required=True)
    close = StringField(required=True)
    volume = StringField(required=True)
