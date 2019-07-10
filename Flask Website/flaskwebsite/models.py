from datetime import datetime
from flaskwebsite import db
class Post(db.Model):
    name = db.Column(db.String(100), primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Post('{self.name}', '{self.date_posted}')"
#models