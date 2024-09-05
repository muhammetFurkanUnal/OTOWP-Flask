from flask import Blueprint, jsonify
from ..models import Group, Tag
from ..services import MainpageService


mainpageBP = Blueprint("mainpage", __name__)
mpService = MainpageService()


@mainpageBP.route("/mainpage")
def index():
    return "main page controller works!"


@mainpageBP.route("/groups")
def getGroups():
    return jsonify(mpService.fetchGroups())


@mainpageBP.route("/tags")
def getTags():
    return jsonify(mpService.fetchTags())
