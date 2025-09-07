"""
This module contains shared fixtures.
"""

# ------------------------------------------------------------
# Imports
# ------------------------------------------------------------

import sys
import os
import pytest

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname('tribaldex'))

from pages.search import CtpPage
from playwright.sync_api import Playwright, APIRequestContext, Page, expect
from typing import Generator


# ------------------------------------------------------------
# DuckDuckGo search fixtures
# ------------------------------------------------------------

@pytest.fixture
def search_page(page: Page) -> CtpPage:
    return CtpPage(page)


# ------------------------------------------------------------
# GitHub project fixtures
# ------------------------------------------------------------

# Environment variables

def pytest_addoption(parser):
    parser.addoption("--ticker", action="store", default="CTP")

def pytest_generate_tests(metafunc):
    # This is called for every test. Only get/set command line arguments
    # if the argument is specified in the list of test "fixturenames".
    option_value = metafunc.config.option.ticker
    if 'ticker' in metafunc.fixturenames and option_value is not None:
        metafunc.parametrize("ticker", [option_value])

def _get_env_var(varname: str) -> str:
    value = os.getenv(varname)
    assert value, f'{varname} is not set'
    return value

