"""
This is a boilerplate pipeline 'train_model'
generated using Kedro 0.18.11
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import load_data, build_model, train_model

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=load_data,
            inputs=None,
            outputs="dataloader",
            name="load_data",
        ),
        node(
            func=build_model,
            inputs=None,
            outputs="model",
            name="build_model",
        ),
        node(
            func=train_model,
            inputs=["model", "dataloader", "params:devices"],
            outputs="trained_model",
            name="train_model",
        ),
    ])
