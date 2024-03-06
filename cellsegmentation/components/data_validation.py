import os, sys
import shutil
from cellsegmentation.logger import logging
from cellsegmentation.exception import AppException
from cellsegmentation.entity.config_entity import DataValidationConfig
from cellsegmentation.entity.artifacts_entity import (
    DataIngestionArtifacts,
    DataValidationArtifacts,
)


class DataValidation:
    def __init__(self, data_ingestion_artifacts, data_validation_config):
        try:
            self.data_ingestion_artifacts = data_ingestion_artifacts
            self.data_validation_config = data_validation_config
        except Exception as e:
            raise AppException(e, sys)

    def validate_all_files_exist(self):
        try:
            validation_status = None

            all_files = os.listdir(self.data_ingestion_artifacts.feature_store_path)

            for file in all_files:
                if file not in self.data_validation_config.req_files_list:
                    validation_status = False
                    os.makedirs(
                        self.data_validation_config.data_validation_dir, exist_ok=True
                    )
                    with open(self.data_validation_config.valid_status_file, "w") as f:
                        f.write(f"Validation Status: {validation_status}")
                else:
                    validation_status = True
                    os.makedirs(
                        self.data_validation_config.data_validation_dir, exist_ok=True
                    )
                    with open(self.data_validation_config.valid_status_file, "w") as f:
                        f.write(f"Validation Status: {validation_status}")

            return validation_status

        except Exception as e:
            raise AppException(e, sys)

    def initiate_data_validation(self):
        logging.info(
            "Entered initialize_data_validation method in DataValidation Class"
        )

        try:
            status = self.validate_all_files_exist()
            data_validation_artifacts = DataValidationArtifacts(
                validation_status=status
            )

            logging.info(
                "Exited initialize_data_validation method in DataValidation Class"
            )
            logging.info(f"Data Validation Artifact: {data_validation_artifacts}")

            if status:
                shutil.copy(
                    self.data_ingestion_artifacts.data_zip_file_path, os.getcwd()
                )

            return data_validation_artifacts

        except Exception as e:
            raise AppException(e, sys)
