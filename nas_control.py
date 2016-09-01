#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask, request

from Kodi import Kodi
from Player import Player

app = Flask(__name__)


@app.route('/')
def index():
    return "Nas control App"


@app.route('/music_on', methods=['POST'])
def music_on():
    if request.method == 'POST':

        if request.values['password'] == "monpass":
            print "Lancement musique"
            radio = "http://192.99.17.12:6410"
            player = Player()
            player.play(radio)
        else:
            print "mauvais pass"

        return "Lancement musique"


@app.route('/music_off', methods=['POST'])
def music_off():
    if request.method == 'POST':

        if request.values['password'] == "monpass":
            print "Arret musique"
            player = Player()
            player.stop()
        else:
            print "mauvais pass"

        return "Arret musique"


@app.route('/kodi_on', methods=['POST'])
def kodi_on():
    if request.method == 'POST':

        if request.values['password'] == "monpass":
            print "Lancement kodi"
            kodi = Kodi()
            kodi.play()

        else:
            print "mauvais pass"

        return "Lancement kodi"


@app.route('/kodi_off', methods=['POST'])
def kodi_off():
    if request.method == 'POST':

        if request.values['password'] == "monpass":
            print "Stop kodi"
            kodi = Kodi()
            kodi.stop()

        else:
            print "mauvais pass"

        return "Stop kodi"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
