import os.path
from flask import Flask
from flask_autoindex import AutoIndex

app = Flask(__name__)
AutoIndex(app, browse_root = '/home/pi/Desktop/surveillance/images')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)