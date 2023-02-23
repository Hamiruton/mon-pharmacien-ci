""" Import module """
from flask import request, jsonify
from src.pharmacy import pharmacy


@pharmacy.get('/')
def test():
    """
    Test function
    """
    return "Hey, test"