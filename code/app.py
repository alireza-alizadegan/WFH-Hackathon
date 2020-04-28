from flask import Flask
from flask_restful import Api

from resources.user import User

app = Flask(__name__)
api = Api(app)

api.add_resource(User, '/projects/<int:flag>') # http://127.0.0.1:5000/student/Rolf

if __name__ == '__main__':
    app.run(port=8080, debug=True)
