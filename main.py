from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///graphql.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200))
    user_id = db.Column(db.Integer)

def resolve_users():
    users = User.query.all()

    return [
        {
            "id": u.id,
            "username": u.username
        }
        for u in users
    ]

with app.app_context():
    db.create_all()

    db.session.add(User(username="Ali"))
    db.session.add(User(username="Vali"))

    db.session.commit()

    print(resolve_users())
