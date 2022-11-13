from flask_restx import fields

pills = {
    "ITEM_NAME": fields.String(),
    "ENTP_NAME": fields.String(),
    "CLASS_NAME": fields.String(),
    "Efficacy": fields.String(),
    "Dosage": fields.String(),
    "AtpnWarnQesitm": fields.String(),
    "AtpnQesitm": fields.String(),
    "SeQesitm": fields.String(),
    "DepositMethodQesitm": fields.String(),
    "PillImg": fields.String()
}

pill_search_request = {
    "image_front": fields.Url(),
    "image_back": fields.Url()
}

pill_search_response = {
    "ResultPill": fields.String(),
    "OtherPill": fields.List(fields.String())
}