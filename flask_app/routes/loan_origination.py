# flask-app/flask_app/routes/loan_origination.py
from flask import Blueprint, jsonify
from flask_app.models.data import get_loan_origination_by_year

loan_origination_bp = Blueprint('loan_origination', __name__)

@loan_origination_bp.route('/api/loan-origination-by-year', methods=['GET'])
def get_loan_origination_by_year_route():
    origination_by_year = get_loan_origination_by_year()
    return origination_by_year.to_json()
