import io
import cv2 as cv

from api.pill_model.util.dis_method import *
from PIL import Image

PATH = "api/pill_model/saved_models/segment-model.pth"


def segmentation(img_path, save_path):
    model = ISNetDIS()
    model.load_state_dict(torch.load(PATH))

    image_tensor, orig_size = load_image(img_path, hypar)
    mask = predict(model, image_tensor, orig_size, hypar, device)

    im = Image.fromarray(mask)
    im.save('assets/mask.png')

    row_img = Image.open(img_path)
    mask_img = Image.open('assets/mask.png')

    row_img = row_img.convert('RGBA')
    mask_img = mask_img.convert('L')
    row_img.putalpha(mask_img)
    row_img.save(save_path)

    # src = cv.imread(img_path)
    # mask = cv.imread('assets/mask.png', cv.IMREAD_GRAYSCALE)
    # result = np.zeros_like(mask)
    #
    # cv.copyTo(src, mask, result)
    #
    # cv.imwrite(save_path, result)
