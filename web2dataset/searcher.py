# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/searcher.ipynb (unless otherwise specified).

__all__ = ['Searcher', 'GoogleImageSearcher']

# Cell
import os
from typing import List
from .document import Document

import json
import jsons

# Cell
class Searcher:
    def __init__(self, query: str, n_item: int):
        self.query = query
        self.n_item = n_item
        self.documents: List[Document] = []

    def search(self):
        pass

    def save(self,path: str):
        """
        path: folder path
        """

        if not os.path.isdir(path):
            os.mkdir(path)

        os.chdir(path)

        for doc in self.documents:
            with open(f"{doc.uuid}.json", 'w') as fp:

                json.dump(jsons.dump(doc),fp)


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
class GoogleImageSearcher(Searcher):
    def __init__(self, query: str, n_item: int):
        super().__init__(query, n_item)

    def _element_to_document(self, element):
        url = element.get_attribute("src")
        return Document(origin=self.query, image_url=url)

    def _find_images(self, driver: WebDriver) -> List[WebElement]:
        return driver.find_elements(By.CLASS_NAME, "rg_i")

    def _scrap_all_images_in_current_page(self, driver: WebDriver):
        elements = self._find_images(driver)
        self.elements = elements
        self.documents += [
            self._element_to_document(e)
            for i, e in enumerate(elements)
            if len(self.documents) + i < self.n_item
        ]

    def _scroll_to_next_page(self, driver: WebDriver):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def search(self):
        with _get_driver() as driver:

            driver.get(self.query)

            _continue = True
            while _continue:
                self._scrap_all_images_in_current_page(driver)
                _continue = len(self.documents) < self.n_item

                if _continue:
                    self._scroll_to_next_page(driver)