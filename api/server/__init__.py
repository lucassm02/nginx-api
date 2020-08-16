import flask

APP = flask.Flask(__name__)

@APP.route('/')
def index():
  return flask.jsonify({'messsage': 'Server is running'})


if __name__ == '__main__':
  APP.debug = True
  APP.run()