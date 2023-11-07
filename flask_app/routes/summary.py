from flask import Blueprint, jsonify
from flask_app.models.data import get_summary

summary_bp = Blueprint('summary', __name__)

@summary_bp.route('/api/summary', methods=['GET'])
def get_summary_route():
    summary = get_summary()
    return summary.to_json(orient='split')
