from flask import jsonify


def success(data, status=200):

    return jsonify(data), status


def error(message, status):

    return jsonify({
        "error": message
    }), status