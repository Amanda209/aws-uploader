import os

from flask import Flask

UPLOAD_FOLDER = 'C:\\Users\\f9539184\\Desktop\\Vinicius\\uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS

# Routes definition
import application.routes.index
