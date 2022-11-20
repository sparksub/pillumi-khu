import numpy as np

from PIL import Image
import torch
from torch.autograd import Variable
from torchvision import transforms
import torch.nn.functional as F

import requests
from io import BytesIO

from data_loader_cache import normalize, im_reader, im_preprocess

PATH = '../model/'
device = 'cuda' if torch.cuda.is_available() else 'cpu'
net = torch.load(PATH + 'model.pt')

hypar = {}  # paramters for inferencing

hypar["model_path"] = "../model"  ## load trained weights from this path
# hypar["restore_model"] = "isnet.pth"  ## name of the to-be-loaded weights
hypar["interm_sup"] = False  ## indicate if activate intermediate feature supervision

##  choose floating point accuracy --
hypar["model_digit"] = "full"  ## indicates "half" or "full" accuracy of float number
hypar["seed"] = 0

hypar["cache_size"] = [512, 512]  ## cached input spatial resolution, can be configured into different size

## data augmentation parameters ---
hypar["input_size"] = [512,
                       512]  ## mdoel input spatial size, usually use the same value hypar["cache_size"], which means we don't further resize the images
hypar["crop_size"] = [512,
                      512]  ## random crop size from the input, it is usually set as smaller than hypar["cache_size"], e.g., [920,920] for data augmentation


class GOSNormalize(object):
    '''
    Normalize the Image using torch.transforms
    '''

    def __init__(self, mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]):
        self.mean = mean
        self.std = std

    def __call__(self, image):
        image = normalize(image, self.mean, self.std)
        return image


transform = transforms.Compose([GOSNormalize([0.5, 0.5, 0.5], [1.0, 1.0, 1.0])])


def load_image(im_path, hypar):
    if im_path.startswith("http"):
        im_path = BytesIO(requests.get(im_path).content)

    im = im_reader(im_path)
    im, im_shp = im_preprocess(im, hypar["cache_size"])
    im = torch.divide(im, 255.0)
    shape = torch.from_numpy(np.array(im_shp))
    return transform(im).unsqueeze(0), shape.unsqueeze(0)  # make a batch of image, shape


def predict(net, inputs_val, shapes_val, hypar, device):
    '''
    Given an Image, predict the mask
    '''
    net.eval()

    if (hypar["model_digit"] == "full"):
        inputs_val = inputs_val.type(torch.FloatTensor)
    else:
        inputs_val = inputs_val.type(torch.HalfTensor)

    inputs_val_v = Variable(inputs_val, requires_grad=False).to(device)  # wrap inputs in Variable

    ds_val = net(inputs_val_v)[0]  # list of 6 results

    pred_val = ds_val[0][0, :, :, :]  # B x 1 x H x W    # we want the first one which is the most accurate prediction

    ## recover the prediction spatial size to the orignal image size
    pred_val = torch.squeeze(
        F.upsample(torch.unsqueeze(pred_val, 0), (shapes_val[0][0], shapes_val[0][1]), mode='bilinear'))

    ma = torch.max(pred_val)
    mi = torch.min(pred_val)
    pred_val = (pred_val - mi) / (ma - mi)  # max = 1

    if device == 'cuda': torch.cuda.empty_cache()
    return (pred_val.detach().cpu().numpy() * 255).astype(np.uint8)  # it is the mask we need



def segmentation(img_path, img_name, SAVE_PATH):
    image_tensor, orig_size = load_image(img_path, hypar)
    mask = predict(net, image_tensor, orig_size, hypar, device)
    im = Image.fromarray(mask)
    im.save(SAVE_PATH + img_name)
