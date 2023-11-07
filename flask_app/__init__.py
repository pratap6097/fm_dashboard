from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_app.configs.config import DEBUG
from flask_app.configs.config import SQLALCHEMY_DATABASE_URI
from flask_app.configs.config import SQLALCHEMY_TRACK_MODIFICATIONS

app = Flask(__name__)
app.config['DEBUG'] = DEBUG

# Register blueprints here
from flask_app.routes.summary import summary_bp
from flask_app.routes.loan_issuers import loan_issuers_bp
from flask_app.routes.loan_origination import loan_origination_bp

from flask_app.routes.mean_credit_score import get_mean_credit_score_bp
from flask_app.routes.buyer_statistics import get_buyer_statistics_bp
from flask_app.routes.units_statistics import get_units_statistics_bp

from flask_app.routes.top_10_states_most_units import get_top_10_states_most_units_bp
from flask_app.routes.top_10_states_least_units import get_top_10_states_least_units_bp
from flask_app.routes.mean_price import get_mean_price_bp
from flask_app.routes.mean_loan_amount import get_mean_loan_amount_bp

app.register_blueprint(summary_bp)
app.register_blueprint(loan_issuers_bp)
app.register_blueprint(loan_origination_bp)

app.register_blueprint(get_mean_credit_score_bp)
app.register_blueprint(get_buyer_statistics_bp)
app.register_blueprint(get_units_statistics_bp)

app.register_blueprint(get_top_10_states_most_units_bp)
app.register_blueprint(get_top_10_states_least_units_bp)
app.register_blueprint(get_mean_price_bp)
app.register_blueprint(get_mean_loan_amount_bp)


app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

#db = SQLAlchemy(app)

#http://localhost:5000/api/summary: Get summary statistics of the data.
#http://localhost:5000/api/top-loan-issuers: Get the top loan issuers.
#http://localhost:5000/api/loan-origination-by-year: Get loan origination by year.
