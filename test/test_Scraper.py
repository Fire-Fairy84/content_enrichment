import pytest
from src.Scraper import Scraper


@pytest.fixture
def scraper():
    return Scraper()


def test_scrapebot_success(scraper):
    url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
    result = scraper.scrapebot(url)

    assert result is not None
    assert len(result) > 0
    assert any("Python" in paragraph for paragraph in result)


def test_scrapebot_failure(scraper):
    url = 'https://thispagedoesnotexist.com'
    result = scraper.scrapebot(url)

    assert result is None