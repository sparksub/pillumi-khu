import base64
import io

from flask import request
from flask_restx import Namespace, Resource
from PIL import Image
import numpy as np

from api.pill_model.model.classification.Model import pill_classification_top5
from api.pill_search.model.pill_search_request import *
from api.pill_search.util.get_pill_info_csv import get_pill_info_csv
from api.pill_model.segmentation import segmentation

result_front_url = '/Users/sparksub/Documents/GitHub/pillumi-khu/server/assets/result_front.png'
result_back_url = '/Users/sparksub/Documents/GitHub/pillumi-khu/server/assets/result_back.png'

pill_search = Namespace("pillsearch")

pill_search_field = pill_search.model("pillsearchrequest", pill_search_request)
pill_search_request_field = pill_search.model("pillsearch", pill_search_response)


@pill_search.route("/")
class search_pill(Resource):
    @pill_search.expect(pill_search_field)
    @pill_search.response(200, "검색 성공", pill_search_request_field)
    @pill_search.doc(
        resources={
            400: "검색 실패",
        }
    )
    def post(self):
        """
        알약 검색
        :return: 알약 검색 결과
        """

        try:
            data = request.get_json()

            raw_front = base64.b64decode(data['image_front'])
            raw_back = base64.b64decode(data['image_back'])

            image_front = Image.open(io.BytesIO(raw_front))
            image_back = Image.open(io.BytesIO(raw_back))

            image_front.save('assets/pill_front.jpg')
            image_back.save('assets/pill_back.jpg')

            segmentation('assets/pill_front.jpg', result_front_url)
            segmentation('assets/pill_back.jpg', result_back_url)

            pill_front = np.array(Image.open(result_front_url))
            pill_back = np.array(Image.open(result_back_url))

            result_list = pill_classification_top5(pill_front, pill_back)

            result = get_pill_info_csv(result_list[0]['ITEM_SEQ'],
                                   result_list[0]['CLASS_NAME'],
                                   result_list[0]['ITEM_IMAGE'])

            similar = []

            for i in range(1, len(result_list)):
                similar.append(
                    get_pill_info_csv(
                        result_list[i]['ITEM_SEQ'],
                        result_list[i]['CLASS_NAME'],
                        result_list[i]['ITEM_IMAGE'])
                )

            print(result)

            return {
                       "ResultPill": result,
                       "OtherPill": similar
                   }, 200

        except Exception as e:
            return (str(e)), 400
