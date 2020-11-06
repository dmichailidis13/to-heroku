from app1 import app1
from db import db

db.init_app(app1)

@app1.before_first_request
def create_tables():
    db.create_all()
