from flask import Blueprint, jsonify
from flask_app.models.data import get_top_10_states_least_units

get_top_10_states_least_units_bp = Blueprint('get_top_10_states_least_units_bp', __name__)

@get_top_10_states_least_units_bp.route('/api/bottom-10-states', methods=['GET'])
def get_top_10_states_least_units_bp_route():
    top_10_states_least_units = get_top_10_states_least_units()
    return top_10_states_least_units
