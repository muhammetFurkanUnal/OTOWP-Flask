from app.repositories import TagRepository, GroupRepository

def clearTest(app):
  with app.app_context():
      
    tagRepository = TagRepository()
    groupRepository = GroupRepository()

    for i in groupRepository.getAllNonSerialized():
        groupRepository.delete(i)
        
    for i in tagRepository.getByNameNonSerialized():
        tagRepository.delete(i)
    