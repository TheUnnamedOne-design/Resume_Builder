from flask import Flask, send_from_directory
from server.api.routes import api
from flask_cors import CORS
import os

def create_app():
    app = Flask(__name__, static_folder="../client", static_url_path="")

    # ✅ Full GitHub Pages path
    CORS(app, origins=["https://theunnamedone-design.github.io/Resume_Builder/"], supports_credentials=True)

    app.register_blueprint(api)

    @app.route("/")
    def home():
        return send_from_directory(app.static_folder, "index.html")

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
