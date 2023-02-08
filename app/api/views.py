import logging

from flask import Blueprint, jsonify, request
from app.dao.app_dao import AppDAO

api_blueprint = Blueprint('api_blueprint', __name__)
app_dao = AppDAO()


@api_blueprint.route('/', methods=['GET'])
def api_root() -> str:
    '''Root method of api'''
    return "All works well. You can send your requests..."


# GET

@api_blueprint.route("/users", methods=['GET'])
def all_users():
    logging.info('Запрос: /users')
    data = app_dao.get_all_users()
    return jsonify(data)


@api_blueprint.route("/users/<int:id>", methods=['GET'])
def user_by_id(id: int):
    data = app_dao.get_user_by_id(id)
    return jsonify(data)


@api_blueprint.route("/orders", methods=['GET'])
def all_orders():
    logging.info('Запрос: /orders')
    data = app_dao.get_all_orders()
    return jsonify(data)


@api_blueprint.route("/orders/<int:id>", methods=['GET'])
def order_by_id(id: int):
    logging.info(f'Запрос: /orders/{id}')
    data = app_dao.get_orders_by_id(id)
    return jsonify(data)


@api_blueprint.route("/offers", methods=['GET'])
def all_offers():
    logging.info('Запрос: /offers')
    data = app_dao.get_all_offers()
    return jsonify(data)


@api_blueprint.route("/offers/<int:id>", methods=['GET'])
def offer_by_id(id: int):
    logging.info(f'Запрос: /offers/{id}')
    data = app_dao.get_offer_by_id(id)
    return jsonify(data)


# POST

@api_blueprint.route("/users", methods=['POST'])
def add_user():
    return app_dao.add_user(json=request.json)


@api_blueprint.route("/users/<int:id>", methods=['PUT'])
def update_user(id: int):
    return app_dao.update_user(id=id, json=request.json)


@api_blueprint.route("/users/<int:id>", methods=['DELETE'])
def delete_user(id: int):
    return app_dao.delete_user(id=id)


@api_blueprint.route("/orders", methods=['POST'])
def add_order():
    return app_dao.add_order(json=request.json)


@api_blueprint.route("/orders/<int:id>", methods=['PUT'])
def update_order(id: int):
    return app_dao.update_order(id=id, json=request.json)


@api_blueprint.route("/orders/<int:id>", methods=['DELETE'])
def delete_order(id: int):
    return app_dao.delete_order(id=id)


@api_blueprint.route("/offers", methods=['POST'])
def add_offer():
    return app_dao.add_offer(json=request.json)


@api_blueprint.route("/offers/<int:id>", methods=['PUT'])
def update_offer(id: int):
    return app_dao.update_offer(id=id, json=request.json)


@api_blueprint.route("/offers/<int:id>", methods=['DELETE'])
def delete_offer(id: int):
    return app_dao.delete_offer(id=id)
