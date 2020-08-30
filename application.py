from flask import Flask
from flask_restful import Resource, Api
# from pm import make_celery
from pm import celery ### if use one line celer code in pm.py file then uncomment this line

app = Flask(__name__)
# app.config['CELERY_BROKER_URL'] = 'amqp://guest:@localhost:5672//'
# app.config['CELERY_RESULT_BACKEND'] = 'db+sqlite:///db.sqlite3'
# celery = make_celery(app)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        # from pm import hello
        hello.delay()
        return 'I send hello'
        # return hello.delay()
        # return {'hello': 'world'}

@celery.task(name='application.hello')
def hello():
    # print("celery is working")
    return 'hello world'

api.add_resource(HelloWorld, '/')