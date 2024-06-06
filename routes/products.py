from flask import Blueprint, jsonify

name_blueprint = Blueprint('products_blueprint', __name__)

@name_blueprint.route('/hello', methods=['GET'])
def get_foods():
        return jsonify("sucesso")
