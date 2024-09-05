from ..models import Group, group_tag
from .tagRepository import TagRepository
from app import db

class GroupRepository:
    
    def __init__(self):
        self.model = Group
        self.tagRepo = TagRepository()
        
    def serialize(self, groupModelObject:Group):
        group = {
            "id" : groupModelObject.id,
            "name" : groupModelObject.name
        }
        
        return group
        
        
    def getAll(self):
        return [self.serialize(i) for i in self.model.query.all()]

    
    
    def getByID(self, id):
        return self.serialize(self.model.query.get(id))
    
    
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
            
            
    def getTags(self, groupModelObject:Group):
        tags = self.tagRepo.getByGroupID(groupModelObject.id)
        return tags
    