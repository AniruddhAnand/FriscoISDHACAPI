from flask import Flask, request
from index import (getGPAS, getInfo, getCurrentClasses, predictGPA)
from fakeData import *

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Hello World"


@app.route("/students/gpa", methods=["GET"])
def sendGPAS():
    username, password = request.args.values()

    if(username.lower() == "john" and password.lower() == "doe"):
        return currentGPAS

    return getGPAS(username, password)

@app.route("/students/info", methods=["GET"])
def sendInfo():
    username, password = request.args.values()

    if(username.lower() == "john" and password.lower() == "doe"):
            return studentData

    return getInfo(username, password)

@app.route("/students/currentclasses", methods=["GET"])
def sendCurrentClasses():
    username, password = request.args.values()

    if(username.lower() == "john" and password.lower() == "doe"):
            return currentClasses

    courses = []

    classes = getCurrentClasses(username, password)
    
    for course in classes:
        courses.append(
            {
                "name" : course.name,
                "grade" : course.grade,
                "weight" : course.weight,
                "credits" : course.credits,
                "Last Updated" : course.updateDate,
                "assignments" : course.assignments
            }
        )

    return {"currentClasses": courses}

@app.route("/students/predictedGPA", methods=["POST"])
def sendPredictedGPA():
    weightedGPA = request.json["weightedGPA"]
    unweightedGPA = request.json["unweightedGPA"]
    studentGrade = request.json["studentGrade"]
    currentClasses = request.json["currentClasses"]

    print(predictGPA(weightedGPA, unweightedGPA, studentGrade, currentClasses))

    return "Success"