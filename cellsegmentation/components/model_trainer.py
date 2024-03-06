import os, sys
import yaml

from cellsegmentation.utils.main_utils import read_yaml_file
from cellsegmentation.logger import logging
from cellsegmentation.exception import AppException
from cellsegmentation.entity.config_entity import ModelTrainerConfig
from cellsegmentation.entity.artifacts_entity import ModelTrainerArtifacts


class ModelTrainer:
    def __init__(self, model_trainer_config):
        self.modeL_trainer_config = model_trainer_config

    def initiate_model_training(self):
        logging.info("Entered initiate_model_training method of ModelTrainer Class")

        try:
            logging.info("Unzipping the data")
            os.system("unzip data.zip")
            os.system("rm data.zip")

            os.system(
                f"yolo task=segment mode=train model={self.modeL_trainer_config.weight_name} data=data.yaml epochs={self.modeL_trainer_config.epochs_no} imgsz=640 save=true"
            )

            os.makedirs(self.modeL_trainer_config.model_trainer_dir)
            os.system(
                f"cp runs/segment/train/weights/best.pt {self.modeL_trainer_config.model_trainer_dir}"
            )

            os.system("rm -rf yolov8s-seg.pt")
            os.system("rm -rf train")
            os.system("rm -rf valid")
            os.system("rm -rf test")
            os.system("rm -rf data.yaml")
            os.system("rm -rf runs")

            model_trainer_artifacts = ModelTrainerArtifacts(
                trained_model_file_path="artifacts/model_trainer/best.pt"
            )

            logging.info("Exited initiate_model_training method of ModelTrainer Class")
            logging.info(f"Model Trainer Artifacts: {model_trainer_artifacts}")

            return model_trainer_artifacts

        except Exception as e:
            raise AppException(e, sys)
