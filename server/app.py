from flask import Flask, render_template
from flask_restx import Api

from api.pill_model.model.classification.Model import load_classificate_model
from api.pill_model.segmentation import load_segment_model
from api.pill_search.pill_search import pill_search
from api.pill_model.pill_model import pill_model
import utils
from api.pill_search.util.get_pill_info_csv import load_spacing_model

app = Flask(__name__)
api = Api(app, title="Pillumi API Documentation")


def create_app():
    app.config['JSON_AS_ASCII'] = False

    return app, api


if __name__ == "__main__":
    # os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

    @app.route("/manual")
    def manual():
        return render_template("pillumi.html")


    load_segment_model()
    load_classificate_model()
    load_spacing_model()

    api.add_namespace(pill_search)
    api.add_namespace(pill_model)
    app.run(utils.ip, port=5001, debug=True)
