"""
Page object for the tribaldex trade pages, e.g. https://tribaldex.com/trade/CTP
"""
import pytest
import json
from datetime import datetime, timezone
from playwright.sync_api import Page

class CtpPage:

    BASE_URL = 'https://tribaldex.com/trade/'

    def __init__(self, page: Page) -> None:
        self.page = page
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
    
    def pull_data(self, phrase: str, ticker) -> None:
        utc_now = datetime.now(timezone.utc)
        timestamp = utc_now
        json_timestamp = timestamp.strftime('%Y-%m-%dT%H:%M:%SZ')
        file_timestamp = timestamp.strftime("%Y%m%d_%H%M%SZ")

        def _sets_to_lists(obj):
            if isinstance(obj, set):
                return list(obj)
            raise TypeError
        
        data = {
            "@timestamp": json_timestamp,
            "ecs.version": "9.1.3",
            "host.name": "willman-enterprises",
            "agent": {
                "id": "tribaldex-bot",
                "name": "tribaldex-bot",
                "type": "elastic-agent"
            },
            "data_stream": {
                "dataset": "cryptocurrency.metrics",
                "namespace": "tribaldex-ui",
                "type": "metrics"
            },
            "ticker": ticker,
            "prices": {
                "last_hive" + self.lastHive.text_content(),
                "last_usd" + self.lastDollar.text_content(),
                "24hr_hive" + self.twentyFourHive.text_content(),
                "24hr_usd" + self.twentyFourDollar.text_content(),
                "ask_hive" + self.askHive.text_content(),
                "ask_usd" + self.askDollar.text_content(),
                "bid_hive" + self.bidHive.text_content(),
                "bid_usd" + self.bidDollar.text_content(),
                "volume_hive" + self.volumeHive.text_content(),
                "volume_usd" + self.volumeDollar.text_content()
            },
            "event": {
                "dataset": "cryptocurrency.metrics",
                "kind": "metric",
            }
        }
        json_string = json.dumps(data, default=_sets_to_lists, indent=4)

        with open("tribaldex-" + ticker + "-" + file_timestamp + ".json", "w") as f:
            f.write(json_string);
        
        """
        print("ticker: " + ticker)
        print("last (hive): " + self.lastHive.text_content())
        print("last (USD) : " + self.lastDollar.text_content())
        print("24hr (hive): " + self.twentyFourHive.text_content())
        print("24hr (USD) : " + self.twentyFourDollar.text_content())
        print("ask (hive) : " + self.askHive.text_content())
        print("ask (USD)  : " + self.askDollar.text_content())
        print("bid (hive) : " + self.bidHive.text_content())
        print("bid (USD)  : " + self.bidDollar.text_content())
        print("vol (hive) : " + self.volumeHive.text_content())
        print("vol (USD)  : " + self.volumeDollar.text_content())
        """

    @pytest.fixture(scope="session", autouse=True)
    def ticker(pytestconfig):
        return pytestconfig.getoption("ticker")