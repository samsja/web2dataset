# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/searcher.ipynb (unless otherwise specified).

__all__ = ['Searcher', 'SearchError', 'GoogleImageSearchError', 'GoogleImageSearcher']

# Cell
import json
import os
from abc import ABC, abstractmethod
from typing import List, Optional

import jsons

from .cleaner import IdentityCleaner, MetaDataCleaner
from .document import Document

# Cell
class Searcher(ABC):
    def __init__(
        self, query: str, n_item: int, cleaners: Optional[List[MetaDataCleaner]] = None
    ):
        self.query = query
        self.n_item = n_item
        self.documents: List[Document] = []
        self.cleaners = cleaners

    @abstractmethod
    def search(self):
        pass

    def clean(self):
        if self.cleaners is not None:
            for cleaner in self.cleaners:
                self.documents = cleaner.clean(self.documents)

    def save(self, path: str):
        """
        path: folder path
        """

        if not os.path.isdir(path):
            os.mkdir(path)

        os.chdir(path)

        for doc in self.documents:
            with open(f"{doc.uuid}.json", "w") as fp:
                json.dump(jsons.dump(doc), fp)

# Cell


class SearchError(ValueError):
    pass

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
class GoogleImageSearchError(SearchError):
    pass

# Cell
class GoogleImageSearcher(Searcher):
    """
    query: str, it contains the query that is send to google search
    """

    def __init__(
        self, query: str, n_item: int, cleaners: Optional[List[MetaDataCleaner]] = None
    ):
        super().__init__(query, n_item,cleaners)

        self.google_image_url = self._create_url_from_query(self.query)

    def _create_url_from_query(self, query: str) -> str:
        if "+" in query:
            raise GoogleImageSearchError(
                " + should not be in the query because the whitespace are replaced by + so the meaning is different"
            )
        return f"https://www.google.com/search?q={query.replace(' ','+')}&source=lnms&tbm=isch"

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

            driver.get(self.google_image_url)

            _continue = True
            while _continue:
                self._scrap_all_images_in_current_page(driver)
                _continue = len(self.documents) < self.n_item

                if _continue:
                    self._scroll_to_next_page(driver)