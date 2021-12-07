# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/utils_data.ipynb (unless otherwise specified).

__all__ = ['file_to_doc', 'get_metadata_path', 'get_images_path', 'load_docs']

# Cell
import json
import os
from typing import List

import jsons

from .document import Document

# Cell
def file_to_doc(path_to_file: str) -> Document:
    """
    Function  to load a json file into a web2dataset.Document
    args:
        path_to_file: str. A string containing the path to a json file
    """
    with open(path_to_file) as json_file:
        data = json.load(json_file)

    return jsons.load(data,Document)

# Cell
def get_metadata_path(path: str) -> str:
    """
    Function to get the metadata path
    args:
        path: str. A string containing the path to the folder (where we saved a search)
    """
    return f"{path}/metadata"

# Cell
def get_images_path(path: str) -> str:
    """
    Function to get the metadata path
    args:
        path: str. A string containing the path to the folder (where we saved a search)
    """
    return f"{path}/images"

# Cell
def load_docs(path: str) -> List[Document]:
    """
    Function: Load the metadata of a dataset, i.e it load the docs from the metadata folder of the dataset
    args:
        path: str. A string containing the path to the folder where we saved save a search for example
    """

    metadata_path = get_metadata_path(path)
    if not os.path.isdir(metadata_path):
        raise PathError(f"not metadata subfolder in {path}")

    file_docs = os.listdir(metadata_path)

    return [file_to_doc(f"{metadata_path}/{file}") for file in file_docs]