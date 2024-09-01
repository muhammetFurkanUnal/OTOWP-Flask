from app import create_app, db
from app.models import Group, Tag
from app.repositories import GroupRepository, TagRepository
from itertools import product

def updateTest(app):
    with app.app_context(): 
        
        groupRepository = GroupRepository()
        tagRepository = TagRepository()
        
        # sample data construction
        areas = ["Akdeniz",
                 "Karadeniz",
                 "Marmara",
                 "Anadolu",
                 "Ege"
        ]
        
        schools = [
          "İlkokul",
          "Ortaokul",
          "Lise",
          "Üniversite"    
        ]
        
        lectures = [
            "Matematik",
            "Edebiyat",
            "Tarih",
            "Coğrafya",
            "Hukuk"
        ]
        
        # generate tags and add to db
        for tag in areas + schools + lectures:
            tagRepository.add(Tag(name=tag))
            
            
        # generate groups and add to db
        tags = {tag.name : tag for tag in tagRepository.getAll()}
        for area, school, lecture in product(areas, schools, lectures):
            group = Group(name=f"{area} {school} {lecture}")
            group.tags.append(tags[area])
            group.tags.append(tags[school])
            group.tags.append(tags[lecture])
            groupRepository.add(group)
          
            

        print("başarılı!")
        