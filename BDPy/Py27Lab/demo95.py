#encoding=UTF-8
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Rest1(Resource):
    def get(self):
        return {"name": 'BDPY', "duration": '35hr'}


class Rest2(Resource):
    def get(self):
        return ['Mark', 'John', None, '派森', u'中文派森']


api.add_resource(Rest1, "/rest1")
api.add_resource(Rest2, "/rest2")

app.run(port=5551, host='0.0.0.0', debug=True)
