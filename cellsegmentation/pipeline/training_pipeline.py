import sys, os

from cellsegmentation.logger import logging
from cellsegmentation.exception import AppException
from cellsegmentation.components.data_ingestion import DataIngestion

from cellsegmentation.entity.config_entity import DataIngestionConfig
from cellsegmentation.entity.artifacts_entity import DataIngestionArtifacts


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def start_data_ingestion(self):
        try:
            logging.info(
                "Entered the start_data_ingestion method of TrainPipeline class"
            )
            logging.info("Getting data from URL")

            data_ingestion = DataIngestion(
                data_ingestion_config=self.data_ingestion_config
            )

            data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()

            logging.info("Got data from the URL")
            logging.info(
                "Exited the start_data_ingestion method of TrainPipeline class"
            )

            return data_ingestion_artifacts
        except Exception as e:
            raise AppException(e, sys)

    def run_pipeline(self):
        try:
            data_ingestion_artifacts = self.start_data_ingestion()
        except Exception as e:
            raise AppException(e, sys)
