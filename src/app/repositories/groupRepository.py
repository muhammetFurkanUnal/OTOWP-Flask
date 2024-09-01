from ..models import Group
from ..models import group_tag
from app import db

class GroupRepository:
    
    def __init__(self):
        self.model = Group
        
    def getAll(self):
        return self.model.query.all()
    
    def getByID(self, id):
        return self.model.query.get(id)
    
    def add(self, groupModelObject:Group):
        db.session.add(groupModelObject)
        db.session.commit()
        
    def update(self, groupModelObject:Group):
        db.session.merge(groupModelObject)
        db.session.commit()
        
    def delete(self, groupModelObject:Group):
        group = self.model.query.get(groupModelObject.id)
        
        if not group:
            print("Doesn't exist!")
            return
      
        db.session.query(group_tag).filter_by(tag_id=group.id).delete()  
        db.session.delete(group)
        db.session.commit()
            