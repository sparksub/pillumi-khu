from flask_restx import Namespace, Resource

from api.pill_model.model.classification.Model import pill_classification_top5
from api.pill_model.model.pill_model_request import *
from api.pill_model.segmentation import segmentation
import cv2 as cv

pill_model = Namespace("pillmodel")

pill_model_field = pill_model.model("pillmodelrequest", pill_model_request)
pill_model_request_field = pill_model.model("pillmodel", pill_model_response)


@pill_model.route("/segment")
class search_pill(Resource):
    @pill_model.expect(pill_model_field)
    @pill_model.response(200, "검색 성공", pill_model_request_field)
    @pill_model.doc(
        resources={
            400: "검색 실패",
        }
    )
    def post(self):
        """
        그냥 test 용 API로 동작하지 않습니다.
        :return: 알약 배경 분리 결과
        """

        try:
            segmentation('assets/pill_front.jpg',
                         'assets/result_front.png')
            segmentation('assets/pill_back.jpg',
                         'assets/result_back.png')

            pill_front = cv.imread('assets/result_front.png')
            pill_back = cv.imread('assets/result_back.png')

            result_list = pill_classification_top5(pill_front, pill_back)
            print(result_list)

            return {
                       "front-img": "string",
                       "back-img": "string"
                   }, 200

        except Exception as e:
            return (str(e)), 400
