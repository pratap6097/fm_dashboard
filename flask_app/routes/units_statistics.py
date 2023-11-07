from flask import Blueprint, jsonify
from flask_app.models.data import get_units_statistics

get_units_statistics_bp = Blueprint('get_units_statistics_bp', __name__)

@get_units_statistics_bp.route('/api/units-statistics', methods=['GET'])
def get_units_statistics_bp_route():
    units_statistics = get_units_statistics()
    return units_statistics
