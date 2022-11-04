from flask import Flask, render_template
from flask_restx import Api
import os

from api.pill_search.pill_search import pill_search
from api.pill_model.pill_model import pill_model

app = Flask(__name__)
api = Api(app, title="Pillumi API Documentation")


def create_app():
    app.config['JSON_AS_ASCII'] = False

    return app, api


# def add_api(api):
#     api.add_namespace(pill_model)
#     api.add_namespace(pill_search)


if __name__ == "__main__":
    # os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

    @app.route("/manual")
    def manual():
        return render_template("pillumi.html")

    api.add_namespace(pill_search)
    api.add_namespace(pill_model)
    app.run('172.16.23.198', port=5001, debug=True)
