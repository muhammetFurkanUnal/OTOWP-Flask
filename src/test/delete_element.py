from app.repositories import GroupRepository


def deleteTest(app):
  with app.app_context():
      
      groupRepo = GroupRepository()
      
      groupToDelete = groupRepo.getByIDNonSerialized(108)
      groupRepo.delete(groupToDelete)
    
