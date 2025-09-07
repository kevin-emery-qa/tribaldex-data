"""
Page object for the tribaldex trade pages, e.g. https://tribaldex.com/trade/CTP
"""
import pytest
from playwright.sync_api import Page

class CtpPage:

    BASE_URL = 'https://tribaldex.com/trade/'

    def __init__(self, page: Page) -> None:
        self.page = page
        self.chratview = page.locator('div.vue-apexcharts')
        self.lastHive = page.locator('.font-bold:has-text("Last") + p')
        self.lastDollar = page.locator('.font-bold:has-text("Last") + p + p[class*="text-gray"]')
        self.twentyFourHive = page.locator('.font-bold:has-text("24H") + p')
        self.twentyFourDollar = page.locator('.font-bold:has-text("24H") + p + p[class*="text-gray"]')
        self.askHive = page.locator('.font-bold:has-text("Ask") + p')
        self.askDollar = page.locator('.font-bold:has-text("Ask") + p + p[class*="text-gray"]')
        self.bidHive = page.locator('.font-bold:has-text("Bid") + p')
        self.bidDollar = page.locator('.font-bold:has-text("Bid") + p + p[class*="text-gray"]')
        self.volumeHive = page.locator('.font-bold:has-text("Volume") + p')
        self.volumeDollar = page.locator('.font-bold:has-text("Volume") + p + p[class*="text-gray"]')
    
    def load(self, ticker) -> None:
        self.page.goto(self.BASE_URL + ticker)
    
    def pull_data(self, phrase: str) -> None:
        self.page.pause()

    @pytest.fixture(scope="session", autouse=True)
    def ticker(pytestconfig):
        return pytestconfig.getoption("ticker")