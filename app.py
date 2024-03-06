import os, sys
from cellsegmentation.pipeline.training_pipeline import TrainPipeline

obj = TrainPipeline()
obj.run_pipeline()
print("Ingestion done!")
