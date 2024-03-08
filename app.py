import sys, os
from flask import Flask, request, jsonify, render_template, Response
from flask_cors import CORS, cross_origin

from cellsegmentation.pipeline.training_pipeline import TrainPipeline
from cellsegmentation.utils.main_utils import decodeImage, encodeImageIntoBase64
from cellsegmentation.constant.application import APP_HOST, APP_PORT


app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "inputimage.jpg"


@app.route("/trainmodel")
def train_model():
    obj = TrainPipeline()
    obj.run_pipeline()
    return "Training Successful"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST", "GET"])
def predictRoute():
    try:
        image = request.json["image"]
        decodeImage(image, clApp.filename)

        os.system(
            "yolo task=segment mode=predict model=artifacts/model_trainer/best.pt conf=0.5 source=data/inputimage.jpg save=true hide_conf=true hide_labels=true"
        )

        opencodedbase64 = encodeImageIntoBase64("runs/segment/predict/inputimage.jpg")
        result = {"image": opencodedbase64.decode("utf-8")}
        os.system("rm -rf runs")
    except ValueError as val:
        print(val)
        return Response("Value Not Found Inside JSON data")
    except KeyError:
        return Response("Incorrect Key Passed!")
    except Exception as e:
        print(e)
        result = "Invalid input"

    return jsonify(result)


if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host=APP_HOST, port=APP_PORT)
