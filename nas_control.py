#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask, request, abort, make_response, jsonify

import importlib
from Player import Player
from Utils.Flask_auth import requires_auth

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/')
@requires_auth
def index():
    return "Nas control App"


@app.route('/app', methods=['POST'])
@requires_auth
def application():
    if not request.json or 'app_name' not in request.json or 'state' not in request.json:
        abort(400)

    # get the app name
    app_name = request.json['app_name']
    try:
        mod = importlib.import_module("Apps." + app_name)
    except ImportError:
        return make_response(jsonify({'error': "No module named %s" % app_name}), 404)

    # get the new status
    state = request.json['state']
    if state == "start":
        mod.start()
        return jsonify({'app_name': app_name, 'state': state}), 201
    if state == "stop":
        mod.stop()
        return jsonify({'app_name': app_name, 'state': state}), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
