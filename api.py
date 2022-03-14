from flask import Flask
from src.dbv.ranking import ranking_bp

app = Flask(__name__)

app.register_blueprint(ranking_bp)
