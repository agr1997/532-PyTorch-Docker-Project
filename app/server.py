from app import app

from flask import render_template, request, make_response, session, url_for, redirect
from flask import safe_join, send_from_directory, abort, flash, copy_current_request_context
#from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class

from torchvision import models, transforms
from PIL import Image
import torch

import os, json, io

# Load pretrained densenet model
dense_model = models.densenet121(pretrained=True)
# Loading dictionary to interpret densenet results
class_dict = json.load(open(os.path.join(os.path.curdir, "imagenet_class_index.json")))
# Push model to CUDA for GPU acceleration if available
if torch.cuda.is_available():
    dense_model.to('cuda')


def predict(img):
    # Try reading image  
    try:
        img = Image.open(io.BytesIO(img))
    except IOError:
        return "Couldn't open image file! Try another format."

    # Transformation sepcification of input images for densenet-121
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    # Apply transformation to image to obtain tensor
    image_tensor = preprocess(img)
    # Convert tensor to mini-batch for model
    image_batch = image_tensor.unsqueeze(0)
    # move the input to GPU for speed if available
    if torch.cuda.is_available():
        image_batch = image_batch.to('cuda')

    with torch.no_grad():
        outputs = dense_model.forward(image_batch)
    _, y_hat = outputs.max(1) 
    pred_index = str(y_hat.item())
    # TODO: jsonify returns
    return ("The imagenet class ID and class_names are" + str(class_dict[pred_index]))

# TODO: Add UI with render_template()- Bootstrap

# TODO: Save images or not?

@app.route('/')
def index():
    return "test"

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        img = file.read()
        return predict(img)
