from flask import Flask
from flask_restful import Api, Resource, reqparse
import pandas as pd

app = Flask(__name__)
api = Api(app)


class Users(Resource):
    def get(self):
        data = pd.read_csv('users.csv')
        data = data.to_dict('records')
        return {'data': data}, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', required=True)
        parser.add_argument('genre', required=True)
        parser.add_argument('platform', required=True)
        parser.add_argument('publisher', required=True)
        args = parser.parse_args()

        data = pd.read_csv('users.csv')

        new_data = pd.DataFrame({
            'title': [args['title']],
            'genre': [args['genre']],
            'platform': [args['platform']],
            'publisher': [args['publisher']]
        })

        data = data.append(new_data, ignore_index=True)
        data.to_csv('users.csv', index=False)
        return {'data': new_data.to_dict('records')}, 201

        def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', required=True)
        args = parser.parse_args()

        data = pd.read_csv('users.csv')

        data = data[data['title'] != args['title']]

        data.to_csv('users.csv', index=False)
        return {'message': 'Record deleted successfully.'}, 200


class Cities(Resource):
    def get(self):
        data = pd.read_csv('users.csv', usecols=[2])
        data = data.to_dict('records')

        return {'data': data}, 200


class Name(Resource):
    def get(self, name):
        data = pd.read_csv('users.csv')
        data = data.to_dict('records')
        for entry in data:
            if entry['title'] == title:
                return {'data': entry}, 200
        return {'message': 'No entry found with this name !'}, 200


# Add URL endpoints
api.add_resource(Cities, '/genre')
api.add_resource(Cities, '/platform')
api.add_resource(Cities, '/publisher')
api.add_resource(Name, '/<string:title>')


if __name__ == '__main__':
    #     app.run(host="0.0.0.0", port=5000)
    app.run()
