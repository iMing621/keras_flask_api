#!/usr/bin/env python
# coding: utf-8
# Predict Image API

# import libs
import flask
from flask import jsonify, request
from keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
from keras.preprocessing import image
from PIL import Image
from io import BytesIO
import numpy as np
import tensorflow as tf
import requests
import sys
import os

# initialize flask and keras model
app = flask.Flask(__name__)
#app.config['DEBUG'] = True # Enable it for debug
#app.config["JSON_AS_ASCII"] = False # for fix chinese issue
model = None
graph = None

def load_model():
    global model
    model = VGG16(weights='imagenet')

    #
    global graph
    graph = tf.get_default_graph()

def get_image(filename, target):
    img = None
    # download image
    if filename.startswith('http://') or filename.startswith('https://'):
        response = requests.get(filename)
        img = Image.open(BytesIO(response.content))
        img = img.resize( target, Image.BILINEAR)
    # local file
    else:
        if not os.path.exists(filename):
            print('file does not exist')
        else:
            img = image.load_img(filename, target_size= target)
            
    return img
    
def process_image(img):
    x = None
    if img is not None:
        if img.mode != "RGB":
            img = img.convert("RGB")
            
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis = 0)
        x = preprocess_input(x)

    return x

@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello Flask!</h1>"

# featuresize: length of predict result
@app.route('/predict', methods=['POST'])
def predict():
    img = None
    img_path = ""
    featuresize = 10
    target = (224, 224)
    data = {"success": False}

    if 'size' in request.values:
        featuresize = int(request.values['size'])

    if 'img_path' in request.values:
        img_path = request.values['img_path']
        print('img_path='+img_path)
        img = get_image(img_path, target= target)

        # process image
        img = process_image(img)

        # predict
        with graph.as_default():
            preds = model.predict(img)
        results = decode_predictions(preds, top=featuresize)[0]
        data["predictions"] = []
        
        # loop over and format the result
        for (imagenetID, label, prob) in results:
            r = {"label": label, "probability": float(("{0:.2f}".format(prob * 100)))}
            data["predictions"].append(r)
            
        data["success"] = True

    return jsonify(data)

if __name__ == '__main__':
    load_model()
    app.run()
