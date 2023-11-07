from flask import Blueprint, jsonify
from flask_app.models.data import get_mean_loan_amount

get_mean_loan_amount_bp = Blueprint('get_mean_loan_amount_bp', __name__)

@get_mean_loan_amount_bp.route('/api/mean-loan-amount', methods=['GET'])
def get_mean_loan_amount_bp_route():
    mean_loan_amount = get_mean_loan_amount()
    return mean_loan_amount
