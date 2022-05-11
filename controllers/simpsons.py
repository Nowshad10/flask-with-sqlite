from flask import Flask
from models import simpsonsModel

def index(req):
    fetch_all = simpsonsModel.Simpson.get_all()
    return fetch_all, 200

def show(req, id):
    fetch_simpson = simpsonsModel.Simpson.show(id)
    return fetch_simpson, 200

def create(req):
    new_simpson = req.get_json()
    create_simpson = simpsonsModel.Simpson.create(new_simpson)
    return create_simpson, 201

def update(req, id):
    fetch_simpson = simpsonsModel.Simpson.show(id)
    new_data = req.get_json()
    updated_simpson = simpsonsModel.Simpson.update(fetch_simpson[0], new_data)
    return updated_simpson, 203

def destroy(req, id):
    fetch_simpson = simpsonsModel.Simpson.show(id)
    simpsonsModel.Simpson.delete(fetch_simpson[0]['id'])
    return [{"message": "Deleted!"}], 204
