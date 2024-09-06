from flask import Blueprint, jsonify
from ..services import MainpageService
from flask import request


mainpageBP = Blueprint("mainpage", __name__)
mpService = MainpageService()


@mainpageBP.route("/groups")
def getGroups():
    return jsonify(mpService.fetchGroups())


@mainpageBP.route("/tags")
def getTags():
    return jsonify(mpService.fetchTags())


@mainpageBP.route("/send-message", methods=["POST"])
def send():
    mpService.getMessageForMSI(request.json)
    return "Message recieved succesfully"
