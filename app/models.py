from app import db, login
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Banner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    img = db.Column(db.String(250), default='img.jpg')

    def __repr__(self):
        return '<Banner %r>' % self.name


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    img = db.Column(db.String(250), default='img.jpg')

    def __repr__(self):
        return '<Table3 %r>' % self.name


class Services(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    desc = db.Column(db.Text())
    

    def __repr__(self):
        return '<Table4 %r>' % self.name


class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    desc = db.Column(db.Text())
    img = db.Column(db.String(250), default='img.jpg')
    

    def __repr__(self):
        return '<Table4 %r>' % self.name


class Videos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    video = db.Column(db.Text())


    def __repr__(self):
        return '<Table4 %r>' % self.name


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

