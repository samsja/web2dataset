# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/cleaner.ipynb (unless otherwise specified).

__all__ = ['MetaDataCleanerError', 'check_no_docs_creation', 'MetaDataCleaner', 'ImageCleaner']

# Cell
from functools import wraps
from typing import List

from .document import Document

# Cell
class MetaDataCleanerError(ValueError):
    pass

# Cell
def check_no_docs_creation(f):
    @wraps(f)
    def wrapper(self, docs: List[Document]) -> List[Document]:
        new_docs = f(self, docs)
        if len(new_docs) > len(docs):
            raise MetaDataCleanerError(f"the cleaner should not create more docs than originaly. There were before {len(docs)} docs and there are now {len(new_docs)} docs")
        return new_docs
    return wrapper

# Cell
class MetaDataCleaner:
    @check_no_docs_creation
    def clean(self, docs: List[Document]) -> List[Document]:
        pass

# Cell
class ImageCleaner:
    def __init__(self, path: str):
        self.path = path

    def clean(self):
        pass