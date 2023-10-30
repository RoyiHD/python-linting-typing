"""
Module to manage the flask application
"""

from flask import Flask


def create_app() -> Flask:
    """
        Method to create a flask application 
    """
    app: Flask = Flask(__name__, static_folder=None)
    return app


if __name__ == "__main__":

    flask_app = create_app()

    flask_app.run(
        host="0.0.0.0",
        port=3000
    )
