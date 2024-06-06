from flask import Flask
from flask_cors import CORS
import os
from flask_jwt_extended import JWTManager

from routes.products import name_blueprint

ALLOWED_HOSTS = ["gpt-treinador.herokuapp.com/", "127.0.0.1"]

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['JSON_SORT_KEYS'] = False
app.config['JWT_SECRET_KEY'] = 'Lelo_318318'
jwt = JWTManager(app)

app.register_blueprint(name_blueprint)

port = int(os.environ.get("PORT", 5000))

if __name__ == '__name__':
    app.run(host="0.0.0.0", port=port)