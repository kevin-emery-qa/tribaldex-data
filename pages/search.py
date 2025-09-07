"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""

from playwright.sync_api import Page


class CtpPage:

    URL = 'https://tribaldex.com/trade/CTP'

    def __init__(self, page: Page) -> None:
        self.page = page
        self.chratview = page.locator('div.vue-apexcharts')

    
    def load(self) -> None:
        self.page.goto(self.URL)
    
    def search(self, phrase: str) -> None:
        self.page.pause()
        self.chratview.hover(position={"x": })
