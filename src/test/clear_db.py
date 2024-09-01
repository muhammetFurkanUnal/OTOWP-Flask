from app.repositories import TagRepository, GroupRepository

def clearTest(app):
  with app.app_context():
      
    tagRepository = TagRepository()
    groupRepository = GroupRepository()

    for i in groupRepository.getAll():
        groupRepository.delete(i)
        
    for i in tagRepository.getAll():
        tagRepository.delete(i)
    