# flask-app/flask_app/routes/loan_issuers.py
from flask import Blueprint, jsonify
from flask_app.models.data import get_top_loan_issuers

loan_issuers_bp = Blueprint('loan_issuers', __name__)

@loan_issuers_bp.route('/api/top-loan-issuers', methods=['GET'])
def get_top_loan_issuers_route():
    top_issuers = get_top_loan_issuers()
    return top_issuers.to_json()
