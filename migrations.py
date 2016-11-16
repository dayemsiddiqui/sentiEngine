from peewee import *
from playhouse.fields import ManyToManyField

db = SqliteDatabase('tweets.db')

class BaseModel(Model):
    class Meta:
        database = db



class TrackWord(BaseModel):
    track_id  = IntegerField(primary_key=True)
    track_word = CharField(unique=True, max_length=150)


class Tweets(BaseModel):
    tweet_id  = IntegerField(primary_key=True)
    tweets = CharField(unique=True, max_length=150)
    creation_date = DateTimeField()
    user  = CharField()
    is_processed = BooleanField()
    trackers = ManyToManyField(TrackWord, related_name='tweets')

class Brand(BaseModel):
    brand_id = IntegerField(primary_key=True)
    name = CharField()

class Product(BaseModel):
    product_id = IntegerField(primary_key=True)
    name = CharField()



db.connect()
db.create_tables([Tweets, TrackWord])
