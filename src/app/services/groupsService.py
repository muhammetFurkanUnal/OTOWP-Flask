from ..repositories import TagRepository, GroupRepository


class GroupsService():
    
    def __init__(self):
        self.tagRepo = TagRepository()
        self.groupRepo = GroupRepository()
    
    
    def addNewGroup(self, data):
        groupName = data["name"]
        tags = data["tags"]
        self.groupRepo.add(name=groupName, tags=tags)
        
        return "add works!"
    
    
    def deleteGroup(self, data):
        
        groupsToDelete = data["groupIDs"]
        for i in groupsToDelete:
            groupToDelete = self.groupRepo.getByIDNonSerialized(i)
            self.groupRepo.delete(groupToDelete)
        
        return f"groups successfully deleted: {groupsToDelete}"
        
    
