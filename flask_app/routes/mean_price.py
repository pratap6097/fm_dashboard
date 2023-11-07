from flask import Blueprint, jsonify
from flask_app.models.data import get_mean_price

get_mean_price_bp = Blueprint('get_mean_price_bp', __name__)

@get_mean_price_bp.route('/api/mean-price', methods=['GET'])
def get_mean_price_bp_route():
    mean_price = get_mean_price()
    return mean_price
