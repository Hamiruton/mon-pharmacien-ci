from flask import Blueprint, jsonify, request
from src.config.db import db

auth = Blueprint('auth', __name__, url_prefix='/api/v1/auth')