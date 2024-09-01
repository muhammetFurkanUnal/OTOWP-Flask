from flask import Blueprint, jsonify
from ..models import Group, Tag


mainpageBP = Blueprint("mainpage", __name__)


@mainpageBP.route("/mainpage")
def index():
    return "main page controller works!"


@mainpageBP.route("/groups")
def getGroups():
    groups = Group.query.all()
    groups = [{
        "id": i.id,
        "name":i.name, 
        } for i in groups]
        
    return jsonify(groups)


@mainpageBP.route("/tags")
def getTags():
    tags = Tag.query.all()
    tags = [{
        "id": i.id,
        "name": i.name
    } for i in tags]
    
    return jsonify(tags)
