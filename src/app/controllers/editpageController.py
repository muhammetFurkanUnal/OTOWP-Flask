from flask import Blueprint, jsonify, request
from ..models import Group, Tag
from ..services import GroupsService, TagsService

editpageBP = Blueprint("editpage", __name__)
groupsService = GroupsService()
tagsService = TagsService()


@editpageBP.route("/groups/add", methods=["POST"])
def addGroup():
    return jsonify(groupsService.addNewGroup(request.json))


@editpageBP.route("/groups/delete", methods=["POST"])
def deleteGroup():
    return jsonify(groupsService.deleteGroup(request.json))


@editpageBP.route("/tags/add", methods=["POST"])
def addTag():
    return jsonify(tagsService.addTag(request.json))


@editpageBP.route("/tags/delete", methods=["POST"])
def deleteTag():
    return jsonify(tagsService.deleteTag(request.json))
