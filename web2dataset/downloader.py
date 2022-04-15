# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/Downloader.ipynb (unless otherwise specified).

__all__ = ['Downloader', 'DownloaderError', 'ImageDownloader', 'GoogleImageDownloaderError', 'GoogleImageDownloader']

# Cell
import os
import urllib
import uuid
from abc import ABC, abstractmethod
from typing import List, Optional

import requests
from docarray import Document, DocumentArray
from rich.progress import (
    BarColumn,
    MofNCompleteColumn,
    Progress,
    TextColumn,
    TimeRemainingColumn,
)

# Cell
class Downloader(ABC):
    _DOCS_FILE_NAME = "dataset.bin"

    def __init__(self, path: str, dataset_fn: str = "dataset.bin"):
        """
        path: folder in which to save the files
        dataset_fn: name of the file in which to save the docarray dataset, by default dataset.bin
        """
        self.docs: DocumentArray = DocumentArray()

        self.path = path[0:-2] if path[-1] == "/" else path
        os.makedirs(path, exist_ok=True)

        self.dataset_fn = dataset_fn

    def download(self, query: str, n_item: int, silence: bool = False):
        """Scrap internet and download some files
        query: a tag to define the download query
        n_item: the number of file to download
        silence: to silence the logging and the progress bar
        """
        with Progress(*self.get_default_column(), disable=silence) as progress:

            progress.add_task(f"Scrapping {query} ...", total=n_item)
            self._download(query, n_item, progress)
            self._save_docs()

    @abstractmethod
    def _download(self, query: str, n_item: int, progress: Progress, task_id: int = 0):
        """Internal method wrap around downlaod method
        query: a tag to define the download query
        n_item: the number of file to download
        progress: rich progress bar
        task_id: the number of the rich task
        """
        ...

    @property
    def path_docs(self):
        return f"{self.path}/{self.dataset_fn}"

    def _save_docs(self):
        """Save the metadata"""
        with open(self.path_docs, "wb") as f:
            f.write(self.docs.to_bytes())

    @staticmethod
    def get_default_column():
        return (
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            MofNCompleteColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            TimeRemainingColumn(),
        )

# Cell
class DownloaderError(ValueError):
    pass

# Cell
class ImageDownloader(Downloader):
    """
    Specialize abstract downloader for image
    """

    _IMG_SUB_PATH = "images"

    def __init__(self, path: str):
        """
        path: folder in which to save the files
        """
        super().__init__(path)
        os.makedirs(self.path_image, exist_ok=True)

    def _data_url_to_file(self, url: str, id_: str):

        with open(f"{self.path_image}/{id_}.jpg", "wb") as f:

            if url.startswith("http"):
                img_data = requests.get(url).content
            else:
                response = urllib.request.urlopen(url)
                img_data = response.file.read()

            f.write(img_data)

    @property
    def path_image(self):
        return f"{self.path}/{self.__class__._IMG_SUB_PATH}"

# Cell
from contextlib import contextmanager

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

# Cell
@contextmanager
def _get_driver(debug=False):

    if debug:
        driver = webdriver.Chrome()
    else:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
    try:
        yield driver
    finally:
        driver.quit()

# Cell
class GoogleImageDownloaderError(DownloaderError):
    pass

# Cell
class GoogleImageDownloader(ImageDownloader):
    """
    GoogleImageDownloader: A downloader to download image from google images

    Example:
    ```python
    >>> from web2dataset import GoogleImageDownloader
    >>> downloader = GoogleImageDownloader(f"tmp/bikedataset")
    >>> downloader.download("red bike", 10)
    ```
    """

    def __init__(self, path: str, debug=False, *args, **kwargs):
        super().__init__(path, *args, **kwargs)
        self.debug = debug

    def _download(self, query: str, n_item: int, progress: Progress, task_id: int = 0):
        """Internal method wrap around downlaod method
        query: a tag to define the download query
        n_item: the number of file to download
        progress: rich progress bar
        task_id: the number of the rich task
        """
        google_image_url = self._create_url_from_query(query)
        with _get_driver(self.debug) as driver:

            driver.get(google_image_url)

            _continue = True
            while _continue:

                self._scrap_all_images_in_current_page(
                    driver, query, n_item, progress, task_id
                )

                if _continue := len(self.docs) < n_item:
                    self._scroll_to_next_page(driver)

    def _create_url_from_query(self, query: str) -> str:
        if "+" in query:
            raise GoogleImageDownloaderError(
                " + should not be in the query because the whitespace are replaced by + so the meaning is different"
            )
        return f"https://www.google.com/search?q={query.replace(' ','+')}&source=lnms&tbm=isch"

    def _element_to_document(
        self, element, query: str, progress: Progress, task_id: int
    ):
        """
        convert an google image element to a document
        """
        url = element.get_attribute("src")

        if url is None:
            return None

        id_ = str(uuid.uuid1())

        self._data_url_to_file(url, id_)

        doc = Document(
            uri=f"{self._IMG_SUB_PATH}/{id_}.jpg",
            tag={"uuid": id_, "origin": query},
        )

        progress.update(task_id, advance=1)

        return doc

    def _find_images(self, driver: WebDriver) -> List[WebElement]:
        return driver.find_elements(By.CLASS_NAME, "rg_i")

    def _scrap_all_images_in_current_page(
        self,
        driver: WebDriver,
        query: str,
        n_item: int,
        progress: Progress,
        task_id: int,
    ):
        elements = self._find_images(driver)
        self.elements = elements

        self.docs.extend(
            filter(
                None,
                [
                    self._element_to_document(e, query, progress, task_id)
                    for i, e in enumerate(elements)
                    if len(self.docs) + i < n_item
                ],
            )
        )

    def _scroll_to_next_page(self, driver: WebDriver):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")