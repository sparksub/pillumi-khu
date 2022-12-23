import cv2 as cv
import numpy as np

from api.pill_model.model.classification import ShapePreprocess


def classification_grapcut():
    # segmentation('/Users/sparksub/Development/pillumi-khu/server/assets/pill_front.jpg',
    #              '/Users/sparksub/Development/pillumi-khu/server/assets/result_front_grapcut.png')
    target_path = '/Users/sparksub/Development/pillumi-khu/server/assets/pill_front.jpg'
    save_path = '/Users/sparksub/Development/pillumi-khu/server/assets/result_front_grapcut.png'

    src = cv.imread(target_path)

    if src is None:
        print('Image load failed!')
        return

    src_normalize = ShapePreprocess.image_normalization(src)
    cv.imwrite('/Users/sparksub/Development/pillumi-khu/server/assets/row-resize.png',src_normalize)
    mask = np.zeros(src_normalize.shape[:2], np.uint8)

    rect = (70, 70, 150, 150)

    cv.grabCut(src_normalize, mask, rect, None, None, 5, cv.GC_INIT_WITH_RECT)

    mask2 = np.where((mask == 0) | (mask == 2), 0, 1).astype('uint8')
    dst = src_normalize * mask2[:, :, np.newaxis]

    cv.imwrite(save_path, dst)