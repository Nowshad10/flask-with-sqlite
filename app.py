from crypt import methods
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug import exceptions

from controllers import simpsons

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "<h1>Welcome to The Simpsons API</h1>"

@app.route('/simpsons', methods = ['GET', 'POST'])
def simpsons_handlers():
    fns = {
        'GET': simpsons.index,
        'POST': simpsons.create
    }
    response, code = fns[request.method](request)
    return jsonify(response), code

@app.route('/simpsons/<int:id>', methods=['GET', 'PATCH', 'PUT', 'DELETE'])
def simpson_handlers(id):
    fns = {
        'GET': simpsons.show,
        'PATCH': simpsons.update,
        'PUT': simpsons.update,
        'DELETE': simpsons.destroy
    }
    response, code = fns[request.method](request, id)
    return jsonify(response), code

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return jsonify({"message": f"Opps... {err}"}), 404

@app.errorhandler(exceptions.InternalServerError)
def handle_server_error(err):
    return jsonify({"message": f"{err}.It's not you, it is us"}), 500

if __name__ == '__main__':
    app.run(debug=True)

