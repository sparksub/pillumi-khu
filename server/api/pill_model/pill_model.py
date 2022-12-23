from flask_restx import Namespace, Resource

from api.pill_model.model.classification.Model import pill_classification_top5
from api.pill_model.model.pill_model_request import *
from api.pill_model.segmentation import segmentation
import cv2 as cv
import time

from api.pill_search.util.get_pill_info_csv import get_pill_info_csv

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
            start = time.time()
            segmentation('/Users/sparksub/Development/pillumi-khu/server/assets/pill_front.jpg',
                         '/Users/sparksub/Development/pillumi-khu/server/assets/result_front.png')
            segmentation('/Users/sparksub/Development/pillumi-khu/server/assets/pill_back.jpg',
                         '/Users/sparksub/Development/pillumi-khu/server/assets/result_back.png')

            pill_front = cv.imread('/Users/sparksub/Development/pillumi-khu/server/assets/result_front.png')
            pill_back = cv.imread('/Users/sparksub/Development/pillumi-khu/server/assets/result_back.png')

            result_list = pill_classification_top5(pill_front, pill_back)
            print(result_list)

            result = get_pill_info_csv(result_list[0]['ITEM_SEQ'],
                                       result_list[0]['ITEM_NAME'],
                                       result_list[0]['CLASS_NAME'],
                                       result_list[0]['ITEM_IMAGE'])

            similar = []

            for i in range(1, len(result_list)):
                similar.append(
                    get_pill_info_csv(
                        result_list[i]['ITEM_SEQ'],
                        result_list[i]['ITEM_NAME'],
                        result_list[i]['CLASS_NAME'],
                        result_list[i]['ITEM_IMAGE'])
                )

            print(result)

            print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간

            return {
                       "front-img": "string",
                       "back-img": "string"
                   }, 200

        except Exception as e:
            return (str(e)), 400
