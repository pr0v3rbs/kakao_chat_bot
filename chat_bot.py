# -*- coding: utf-8 -*-

import os
from flask import Flask, request, jsonify
import gfl_info

app = Flask(__name__)

gfl = gfl_info.gfl_info()

@app.route('/keyboard')
def Keyboard():
    dataSend = {
        "type" : "text"
    }

    return jsonify(dataSend)

@app.route('/message', methods=['POST'])
def Message():
    dataReceive = request.get_json()
    content = dataReceive['content'].lower()

    if content.startswith('gfldt'):
        dataSend = {
            "message": {
                "text": gfl.getDollTime(content.split(' ')[1:])
            }
        }
    elif content.startswith('gflet'):
        dataSend = {
            "message": {
                "text": gfl.getEquipTime(content.split(' ')[1:])
            }
        }
    else:
        dataSend = {
            "message": {
                "text": "None"
            }
        }

    return jsonify(dataSend)

if __name__ == "__main__":
    if not os.path.exists('config'):
        port = raw_input('insert port number\n>')
        open('config', 'w').write(port)
    configs = open('config').read().split()
    app.run(host='0.0.0.0', port = int(configs[0]))
