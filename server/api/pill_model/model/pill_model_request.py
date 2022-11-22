from flask_restx import fields

pill_model_request = {
    "image_front": fields.Url(),
    "image_back": fields.Url()
}

pill_model_response = {
    "ResultPill": fields.String(),
    "OtherPill": fields.List(fields.String())
}