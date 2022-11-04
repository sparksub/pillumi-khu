from flask import request
from flask_restx import Namespace, Resource
from shortuuid import uuid
import numpy as np
import io
import base64
from PIL import Image

from api.pill_search.model.pill_search_request import *

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
            p_id = str(uuid())
            data = request.get_json()
            print(data)

            # TODO: 약 검색 모델에 넣기
            # classification_modal = tf.keras.models.load_model("api/pill_model/pill_classification.h5")
            # TODO: 약 종류 리스트 만들어야 함
            # image_front = Image.open(io.BytesIO(base64.b64decode(data["image_front"])))
            # image_back = Image.open(io.BytesIO(base64.b64decode(data["image_back"])))
            # print("2")
            #
            # image_front = np.asarray(image_front)
            # image_back = np.asarray(image_back)
            # print(image_front)
            #
            # image_front_pil = Image.fromarray(image_front)
            # image_back_pil = Image.fromarray(image_back)
            #
            # image_front_pil = image_front_pil.resize((256, 256))
            # image_back_pil = image_back_pil.resize((256, 256))
            # print("4")
            #
            # image_front_input = np.asarray(image_front_pil)
            # image_back_input = np.asarray(image_back_pil)
            # image_front_input = np.resize(image_front_input, (1, 256, 256, 3))
            # image_back_input = np.resize(image_back_input, (1, 256, 256, 3))
            #
            # print("image_front received: {}".format(image_front_input.shape))
            # print("image_back received: {}".format(image_back_input.shape))

            # predictions = classification_model.predict(image_input).tolist()[0]
            # max_value = max(predictions)
            # max_index = predictions.index(max_value)
            # classified_food_id = foods[max_index]
            #
            # data["food_id"] = classified_food_id
            #
            # user_ref.document(f"{data['userid']}").collection("pill_search").document(f"{fr_id}").set(data)

            return {
                       "ITEM_NAME": "타이레놀500mg",
                       "ENTP_NAME": "한국얀센",
                       "CLASS_NAME": "해열, 진통, 소염제",
                       "Efficacy": "감기로 인한 발열 및 동통(통증), 두통, 신경통, 근육통, 월경통, 염좌통(삔 통증)",
                       "Dosage": "만 12세 이상 소아 및 성인: 1회 1~2정씩 1일 3-4회 (4-6시간 마다) 필요시 복용한다. 1일 최대 4그램 (8정)을 초과하여 복용하지 않는다. 이 "
                                 "약은 가능한 최단기간동안 최소 유효용량으로 복용한다.",
                       "InfoImg": ["assets/sample_eat_info1.jpeg", "assets/sample_eat_info2.jpeg"]
                   }, 200

        except Exception as e:
            return (str(e)), 400
