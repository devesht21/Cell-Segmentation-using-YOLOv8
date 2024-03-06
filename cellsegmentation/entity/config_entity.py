import os
from dataclasses import dataclass
from datetime import datetime
from cellsegmentation.constant.training_pipeline import *


@dataclass
class TrainingPipelineConfig:
    artifacts_dir = ARTIFACTS_DIR


traininig_pipeline_config = TrainingPipelineConfig()


@dataclass
class DataIngestionConfig:
    data_ingestion_dir = os.path.join(
        traininig_pipeline_config.artifacts_dir, DATA_INGESTION_DIR_NAME
    )

    feature_store_file_path = os.path.join(
        data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR
    )

    data_download_url = DATA_DOWNLOAD_URL
