import base64
import io

from flask import request
from flask_restx import Namespace, Resource
# from shortuuid import uuid
from PIL import Image

from api.pill_search.model.pill_search_request import *
from api.pill_search.util.get_pill_info import get_pill_info
from api.pill_model.segmentation import segmentation

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
            similar = [[197100081, "건위소화제 (233)"], [197000208, "비타민 A제 및 D제"]]
            data = request.get_json()

            raw_front = base64.b64decode(data['image_front'])
            raw_back = base64.b64decode(data['image_back'])

            image_front = Image.open(io.BytesIO(raw_front))
            image_back = Image.open(io.BytesIO(raw_back))

            image_front.save('assets/pill_front.jpg')
            image_back.save('assets/pill_back.jpg')

            segmentation('/Users/sparksub/Documents/GitHub/pillumi-khu/server/assets/pill_front.jpg',
                         'assets/result_front.png')
            segmentation('/Users/sparksub/Documents/GitHub/pillumi-khu/server/assets/pill_back.jpg',
                         'assets/result_back.png')

            result = get_pill_info(201605694, "칼슘제(321)")

            if len(similar) is not 0:
                for i in range(len(similar)):
                    similar[i] = get_pill_info(similar[i][0], similar[i][1])

            return {
                       "ResultPill": result,
                       "OtherPill": similar
                   }, 200

        except Exception as e:
            return (str(e)), 400
