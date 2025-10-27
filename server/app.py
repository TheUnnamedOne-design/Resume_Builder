from flask import Flask, send_from_directory
from server.api.routes import api
from flask_cors import CORS

def create_app():
    app = Flask(__name__, static_folder="../client", static_url_path="")

    # ✅ Allow your GitHub Pages origins + localhost for testing
    allowed_origins = [
        "https://theunnamedone-design.github.io",
        "https://theunnamedone-design.github.io/Resume_Builder",
        "http://localhost:5500",  # optional (VSCode live server)
        "http://127.0.0.1:5500"
    ]

    # ✅ Apply CORS globally with full support
    CORS(
        app,
        resources={r"/*": {"origins": allowed_origins}},
        supports_credentials=True,
        allow_headers=["Content-Type", "Authorization"],
        methods=["GET", "POST", "OPTIONS", "PUT", "DELETE"]
    )

    # Register API blueprint *after* CORS
    app.register_blueprint(api)

    @app.route("/")
    def home():
        return send_from_directory(app.static_folder, "index.html")

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
