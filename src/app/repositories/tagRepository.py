from ..models import Tag, group_tag
from app import db

class TagRepository:
    
    def __init__(self):
        self.model = Tag
        
    def getAll(self):
        return self.model.query.all()
    
    def getByID(self, id):
        return self.model.query.get(id)
    
    def add(self, tagModelObject:Tag):
        db.session.add(tagModelObject)
        db.session.commit()
        
    def update(self, tagModelObject:Tag):
        db.session.merge(tagModelObject)
        db.session.commit()
        
    def delete(self, tagModelObject:Tag):
        tag = self.model.query.get(tagModelObject.id)
        
        if not tag:
            print("Doesn't exist!")
            return
    
        db.session.query(group_tag).filter_by(tag_id=tag.id).delete()
        db.session.delete(tag)
        db.session.commit()
            