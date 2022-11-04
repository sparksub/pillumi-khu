from flask_restx import fields

pills = {
    'ITEM_NAME': 'ITEM_NAME',
    'ENTP_NAME': 'ENTP_NAME',
    'ITEM_IMAGE': 'ITEM_IMAGE',
    'CLASS_NAME': 'CLASS_NAME'
}

pill_search_request = {
    "image_front": fields.Url(),
    "image_back": fields.Url()
}

pill_search_response = {
    "ITEM_NAME": fields.String(),
    "ENTP_NAME": fields.String(),
    "CLASS_NAME": fields.String(),
    "Efficacy": fields.String(),
    "Dosage": fields.String(),
    "InfoImg": fields.List(fields.String()),
}