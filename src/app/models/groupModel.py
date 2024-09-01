from app import db
from .groupTagModel import group_tag

class Group(db.Model):
    
    __tablename__ = "groups"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
    
    tags = db.relationship('Tag', secondary=group_tag, back_populates='groups')
    