import sqlite3
from flask_restful import Resource, reqparse
from recommender import getCurrent, getFuture

class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
        type=str,
        required=True,
        help="This field cannot be blank!")
    parser.add_argument('age',
        type=int,
        required=True,
        help="This field cannot be blank!")
    parser.add_argument('zipcode',
        type=str,
        required=True,
        help="This field cannot be blank!")
    parser.add_argument('time',
        type=float,
        required=True,
        help="This field cannot be blank!")
    parser.add_argument('interests',
        action="append",
        required=True,
        help="This field cannot be blank!")
    #!!! ADD INTERESTS. RATINGS and EXPERIENCE

# Given a user and a flag to indicate the type of search, get
# a list of projects
    def get(self, flag):
        data = User.parser.parse_args()

        if flag == 1:
            # Get list of projects in JSON format
            projects = getCurrent(data)
        elif flag == 2:
            # Get list of projects in JSON format
            projects = getFuture(data)
        else:
            return {'message': "Invalid flag given.".format(flag)}, 400

        return projects
