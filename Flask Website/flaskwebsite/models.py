from datetime import datetime
from flaskwebsite import db
class Post(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    your_idea = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Post('{self.name}', '{self.date_posted}')"
#models
db.create_all()