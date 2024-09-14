from ..models import Tag, group_tag
from app import db

class TagRepository:
    
    def __init__(self):
        self.model = Tag
        
        
    def serialize(self, tagModelObject:Tag):
        tag = {
            "id":tagModelObject.id,
            "name":tagModelObject.name
        }
        
        return tag
    
        
    def getAll(self):
        return [self.serialize(i) for i in self.model.query.all()]
    
    def getAllNonSerialized(self):
        return self.model.query.all()
    
    def getByID(self, id):
        return self.serialize(self.model.query.get(id))
    
    def getByIDNonSerialized(self, id):
        return self.model.query.get(id)
    
    def getByName(self, name):
        return self.serialize(self.model.query.filter_by(name=name).first())
    
    def getByNameNonSerialized(self, name):
        return self.model.query.filter_by(name=name).first()
    
    
    def addModel(self, tagModelObject:Tag):
        db.session.add(tagModelObject)
        db.session.commit()
        
    def add(self, tagName):
        self.addModel(Tag(name=tagName))
    
        
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
            
            
    def getByGroupID(self, groupID):
        # get only rows with desired groupID
        tags = db.session.query(group_tag).filter_by(group_id=groupID).all()
        # get only tag ids from rows
        tags = [i[1] for i in tags]
        tags = [self.getByID(i) for i in tags]
        return tags
        
        