from flask import Flask
from src.dbv.ranking import ranking_bp
from src.dbv.members import members_bp

app = Flask(__name__)

app.register_blueprint(ranking_bp)
app.register_blueprint(members_bp)
