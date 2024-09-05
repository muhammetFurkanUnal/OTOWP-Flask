from ..repositories import GroupRepository, TagRepository

class MainpageService:
    
    def __init__(self):
        self.tagRepository = TagRepository()
        self.groupRepository = GroupRepository()
        
        
    def fetchGroups(self):
        groups = self.groupRepository.getAll()
        
        # add tags of each group to json
        for i in groups:
            i["tags"] = self.tagRepository.getByGroupID(i["id"])

        return groups
            
        
    def fetchTags(self):
        tags = self.tagRepository.getAll()
        return tags

