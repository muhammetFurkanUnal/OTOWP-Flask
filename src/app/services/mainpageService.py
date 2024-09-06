from ..repositories import GroupRepository, TagRepository
from MSI import MSI 
from threading import Thread

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


    def runMSI(self, request):
        message = request["message"]
        groups = request["groups"]
        groups = [i["name"] for i in groups]
        _MSI = MSI()
        _MSI.sendMessage(message=message, groups=groups)
        
        
    def getMessageForMSI(self, request):
        Thread(target=self.runMSI, args=(request,)).start()
        