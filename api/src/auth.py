from flask import Blueprint, jsonify, request

auth = Blueprint('auth', __name__, url_prefix='/api/v1/auth')