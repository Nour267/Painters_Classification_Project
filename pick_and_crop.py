from PIL import Image
import os
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
from torch.autograd import Variable
from torchvision import datasets, transforms
from itertools import combinations
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import os
import numpy as np
from torchvision import transforms
import csv
from torchvision import transforms

# THIS CODE WE USED FOR TRAIN AND TEST THE DIFFERENCE WAS ONLY THE NAME OF THE CSV AND THE PATHS

center_crop = transforms.CenterCrop((224, 224))

train_data = pd.read_csv("./train_validation_data.csv")


images = train_data['image_name']
images_dir = './train'
corrubted = './cor_train'

for img in images:
    print(img)
    if img in ["3917.jpg", "41945.jpg", "79499.jpg", "91033.jpg", "92899.jpg", "95347.jpg", "101947.jpg"]:
    # if img in ["18649.jpg", "20153.jpg", "100532.jpg"]:
    #     image_path = os.path.join(corrubted, img)
        image_path = corrubted + '/' + img
    else:
        image_path = images_dir + '/' + img

    image = Image.open(image_path)
    if image.mode != 'RGB':
        image = image.convert('RGB')

    cropped_image = center_crop(image)

    cropped_image.save("./train_images_11_4/" + img)

