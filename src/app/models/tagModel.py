from app import db
from .groupTagModel import group_tag

class Tag(db.Model):
    
    __tablename__ = "tags"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    
    groups = db.relationship('Group', secondary=group_tag, back_populates='tags')
    