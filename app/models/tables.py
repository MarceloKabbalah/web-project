from app import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Colum(db.String)
    name = db.Colum(db.String(80))
    email = db.Colum(db.String(120), unique=True)

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def __repr__(self):
        return "<User %r>" % self.username

class Ticket(db.Model):
    __tablename = "tickets"
    id = db.Column(db.Integer, primary_key=True)
    ticket_priority_Type = db.Colum(db.String)
    sector = db.Colum(db.String(20))
    subject = db.Colum(db.String(80))
    content = db.Colum(db.Text)
    user_id = db.Colum(db.Integer, db.Foreignkey('users.id'))

    User = db.relationship('User', foreign_keys=user_id)

    def __init__(self, ticket_priority_Type, sector, subject, content, user_id):
        self.ticket_priority_Type = ticket_priority_Type
        self.sector = sector
        self.subject = subject
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return "<Ticket %r>" % self.id