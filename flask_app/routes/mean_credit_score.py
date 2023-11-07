from flask import Blueprint, jsonify
from flask_app.models.data import get_mean_credit_score

get_mean_credit_score_bp = Blueprint('get_mean_credit_score', __name__)

@get_mean_credit_score_bp.route('/api/mean-credit-score', methods=['GET'])
def get_mean_credit_score_route():
    mean_credit_score = get_mean_credit_score()
    return mean_credit_score
    #return mean_credit_score.to_json(orient='split')
