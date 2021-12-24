from flask import Flask
from flask_restx import Api, Resource, reqparse

app = Flask(__name__)
api = Api(
          app, 
          title='Calculator API', 
          version='1.0', 
          description='Sample calculator API with Flask',
          prefix='/api',
          default="calculator"
        )

parser = reqparse.RequestParser()
parser.add_argument('number1', type=int, help='first number')
parser.add_argument('number2', type=int, help='second number')

@api.route('/hello')
class HelloWorld(Resource):
  def get(self):
      return 'hello'

@api.route('/sum', methods=['POST'])
@api.doc(parser=parser)
class SumParameter(Resource):
  def post(self):
    args = parser.parse_args()
    sum = args['number1'] + args['number2']
    return {'result': sum}, 200

@api.route('/subtract', methods=['POST'])
@api.doc(parser=parser)
class SumParameter(Resource):
  def post(self):
    args = parser.parse_args()
    subtract = args['number1'] - args['number2']
    return {'result': subtract}, 200

if __name__ == '__main__':
  app.run(host='0.0.0.0', port="80") # Run outsite !!!
