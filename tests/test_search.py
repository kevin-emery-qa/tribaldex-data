"""
These tests cover DuckDuckGo searches.
"""

import pytest

from pages.search import CtpPage
from playwright.sync_api import expect, Page


CRYPTOS = [
    'CTP'
]

@pytest.mark.parametrize('phrase', CRYPTOS)
def test_basic_ctp_load(
    phrase: str,
    page: Page,
    search_page: CtpPage,
    ticker) -> None:
    
    # Given the Tribaldex home page is displayed
    search_page.load(ticker)

    # The user saves json data for elasticsearch time series
    search_page.pull_data(phrase, ticker)