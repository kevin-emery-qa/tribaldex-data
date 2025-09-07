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
    search_page: CtpPage) -> None:
    
    # Given the Tribaldex CTP home page is displayed
    search_page.load()

    # When the user searches for a phrase (currently just pauses)
    search_page.search(phrase)
