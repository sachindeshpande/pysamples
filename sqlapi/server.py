from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify

db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)

class Employee(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from employee") # This line performs query and returns json result
        return {'employee': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID

class Track(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select trackid, name, composer, unitprice from track;")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Employee_Name(Resource):
    def get(self, employee_id):
        conn = db_connect.connect()
        query = conn.execute("select * from employee where EmployeeId =%d "  %int(employee_id))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)
        

api.add_resource(Employee, '/employee') # Route_1
api.add_resource(Track, '/track') # Route_2
api.add_resource(Employee_Name, '/employee/<employee_id>') # Route_3


if __name__ == '__main__':
     app.run(port='5002')