import numpy as np

from tensorflow import keras
from PIL import Image
from keras.applications.vgg16 import preprocess_input
from flask import Flask, request, jsonify

app = Flask(__name__)

IMAGE_SIZE_PX = 200
MODEL_PATH = "../model"

model = keras.models.load_model(MODEL_PATH)


def convert_image_to_tensor(image):
    img = Image.open(image)
    img = img.convert("RGB")
    img = img.resize((IMAGE_SIZE_PX, IMAGE_SIZE_PX))

    img = np.array(img)

    img = preprocess_input(img)

    return img


def predict(img_tensors):
    probs = model.predict(np.expand_dims(img_tensors, axis=0))
    pred = probs.argsort()[0][::-1][0]

    if pred == 1.0:
        return "hotdog"
    else:
        return "not hotdog"


@app.route("/", methods=["POST"])
def classify_hotdog():
    image = request.files.get("image_file", None)
    img_tensors = convert_image_to_tensor(image=image)
    prediction = predict(img_tensors=img_tensors)

    return jsonify(prediction=prediction)
