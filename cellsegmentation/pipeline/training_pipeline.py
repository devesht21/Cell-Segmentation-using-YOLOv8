import sys, os

from cellsegmentation.logger import logging
from cellsegmentation.exception import AppException
from cellsegmentation.components.data_ingestion import DataIngestion
from cellsegmentation.components.data_validation import DataValidation

from cellsegmentation.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig,
)
from cellsegmentation.entity.artifacts_entity import (
    DataIngestionArtifacts,
    DataValidationArtifacts,
)


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()

    def start_data_ingestion(self):

        logging.info("Entered the start_data_ingestion method of TrainPipeline class")

        try:
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

    def start_data_validation(self, data_ingestion_artifacts):

        logging.info("Entered the start_data_validation method of TrainPipeline class")

        try:
            data_validation = DataValidation(
                data_ingestion_artifacts=data_ingestion_artifacts,
                data_validation_config=self.data_validation_config,
            )

            data_validation_artifacts = data_validation.initiate_data_validation()

            logging.info("Performed the data validation operation")
            logging.info(
                "Exited the start_data_validation method of TrainPipeline class"
            )

            return data_validation_artifacts
        except Exception as e:
            raise AppException(e, sys)

    def run_pipeline(self):
        try:
            data_ingestion_artifacts = self.start_data_ingestion()
            data_validation_artifacts = self.start_data_validation(
                data_ingestion_artifacts=data_ingestion_artifacts
            )
        except Exception as e:
            raise AppException(e, sys)
