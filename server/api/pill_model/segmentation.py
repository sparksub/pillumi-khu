from api.pill_model.util.dis_method import *
from PIL import Image
import cv2 as cv
import utils
import time

PATH = "/Users/sparksub/Development/pillumi-khu/server/api/pill_model/save_models/segment-model.pth"


def load_segment_model():
    utils.segment_model = ISNetDIS()
    utils.segment_model.load_state_dict(torch.load(PATH))


def segmentation(img_path, save_path):
    start = time.time()
    image_tensor, orig_size = load_image(img_path, hypar)
    mask = predict(utils.segment_model, image_tensor, orig_size, hypar, device)

    im = Image.fromarray(mask)
    im.save('/Users/sparksub/Development/pillumi-khu/server/assets/mask.png')

    row_img = cv.imread(img_path)
    mask_img = cv.imread('/Users/sparksub/Development/pillumi-khu/server/assets/mask.png')

    mask_img = mask_img / 255
    row_img = row_img * mask_img
    cv.imwrite(save_path, row_img)

    print("seg time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간

