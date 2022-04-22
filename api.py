"""
Arquivo principal da api
"""
from flask import Flask
from flask_cors import CORS
from src.blueprints.dbv.ranking import ranking_bp
from src.blueprints.dbv.members import members_bp
from src.blueprints.auth import auth_bp
from src.blueprints.church.quiz import quiz_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(ranking_bp)
app.register_blueprint(members_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(quiz_bp)
