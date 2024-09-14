from ..repositories import TagRepository, GroupRepository


class TagsService():
    
    def __init__(self):
        self.tagRepo = TagRepository()
        self.groupRepo = GroupRepository()
    
    
    
    def addTag(self, data):
        tagName = data["name"]
        self.tagRepo.add(tagName)
        
        return f"New tag {tagName} successfully added"
    
    
    def deleteTag(self, data):
        tagID = data["tagID"]
        tagToDelete = self.tagRepo.getByIDNonSerialized(tagID)
        self.tagRepo.delete(tagToDelete)
        
        return f"Tag with id {tagID} deleted successfully"
    
    