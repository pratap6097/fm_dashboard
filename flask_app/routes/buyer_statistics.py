from flask import Blueprint, jsonify
from flask_app.models.data import get_buyer_statistics

get_buyer_statistics_bp = Blueprint('get_buyer_statistics_bp', __name__)

@get_buyer_statistics_bp.route('/api/buyer-statistics', methods=['GET'])
def get_buyer_statistics_bp_route():
    buyer_statistics = get_buyer_statistics()
    return buyer_statistics
