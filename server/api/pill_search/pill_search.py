import base64
import io

from flask import request
from flask_restx import Namespace, Resource
from PIL import Image
import cv2 as cv

from api.pill_model.model.classification.Model import pill_classification_top5
from api.pill_search.model.pill_search_request import *
from api.pill_search.util.get_pill_info_csv import get_pill_info_csv
from api.pill_model.segmentation import segmentation
import time

from api.pill_search.util.resize_image_half import resize_image_half

result_front_url = '/Users/sparksub/Development/pillumi-khu/server/assets/result_front.png'
result_back_url = '/Users/sparksub/Development/pillumi-khu/server/assets/result_back.png'

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
            start = time.time()
            data = request.get_json()

            raw_front = base64.b64decode(data['image_front'])
            raw_back = base64.b64decode(data['image_back'])

            image_front = Image.open(io.BytesIO(raw_front))
            image_back = Image.open(io.BytesIO(raw_back))

            if image_front.height < 300:
                image_front.save('/Users/sparksub/Development/pillumi-khu/server/assets/result_front.png')
            else:
                image_front = resize_image_half(image_front)
                image_front.save('/Users/sparksub/Development/pillumi-khu/server/assets/pill_front.jpg')
                segmentation('/Users/sparksub/Development/pillumi-khu/server/assets/pill_front.jpg',
                             '/Users/sparksub/Development/pillumi-khu/server/assets/result_front.png')

            if image_back.height < 300:
                image_back.save('/Users/sparksub/Development/pillumi-khu/server/assets/result_back.png')
            else:
                image_back = resize_image_half(image_back)
                image_back.save('/Users/sparksub/Development/pillumi-khu/server/assets/pill_back.jpg')
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

            print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간

            return {
                       "ResultPill": result,
                       "OtherPill": similar
                   }, 200

        except Exception as e:
            return (str(e)), 400
