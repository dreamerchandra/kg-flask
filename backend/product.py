from peewee import *

db = SqliteDatabase('product.db')

class Product(Model):
    name = TextField()
    price = IntegerField()
    id = IntegerField(primary_key=True)
    img = TextField()
    description = TextField()

    class Meta:
        database = db 

def initialize_db():
    db.connect()
    # db.drop_tables([Product], safe = True)
    db.create_tables([Product], safe = True)
    db.close()