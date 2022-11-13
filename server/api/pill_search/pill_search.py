from flask import request
from flask_restx import Namespace, Resource
from shortuuid import uuid

from api.pill_search.model.pill_search_request import *
from api.pill_search.util.get_pill_info import get_pill_info

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

        # TODO: 기존 dataset에서 itemSeq로 공데포에서 복약정보 검색. 기존 dataset에서 약 분류데이터 가져와서 사용하기

        try:
            similar = [[197100081, "건위소화제 (233)"], [197000208, "비타민 A제 및 D제"]]
            p_id = str(uuid())
            data = request.get_json()
            # print(data)

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

            result = get_pill_info(201605694, "칼슘제(321)")
            # print(result)
            if len(similar) is not 0:
                for i in range(len(similar)):
                    similar[i] = get_pill_info(similar[i][0], similar[i][1])
            # print(similar)

            return {
                       "ResultPill": result,
                       "OtherPill": similar
                   }, 200

        except Exception as e:
            return (str(e)), 400
