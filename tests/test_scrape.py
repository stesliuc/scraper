import pytest
from unittest.mock import patch
from src.scrape_utils import Scraper
import requests


@pytest.fixture
def scraper():
    return Scraper()


@pytest.fixture
def mock_fetch_url():
    with patch("src.scrape_utils.Scraper.fetch_url") as mock_fetch:
        yield mock_fetch


@pytest.fixture
def mock_extract_links():
    with patch("src.scrape_utils.Scraper.extract_links") as mock_extract:
        yield mock_extract


@pytest.fixture
def mock_extract_content():
    with patch("src.scrape_utils.Scraper.extract_content") as mock_extract_content:
        yield mock_extract_content


def test_fetch_url_success(scraper):
    url = "http://example.com"
    return_text = requests.get("http://example.com").text
    response = scraper.fetch_url(url)
    assert response == return_text


def test_fetch_url_failure(scraper):
    response = scraper.fetch_url("not_a_url")
    assert response == None


def test_extract_links(scraper):
    html_content = '<a href="http://example.com">Link</a>'
    links = scraper.extract_links(html_content)
    assert links == ["http://example.com"]


def test_extract_content(scraper):
    html_content = "<p>Hello, World!</p>"
    content = scraper.extract_content(html_content, "p")
    assert content == ["Hello, World!"]


def test_scrape_url_single_page(
    scraper, mock_fetch_url, mock_extract_links, mock_extract_content
):
    url = "http://example.com"
    html_content = '<a href="http://example.com/page2">Link to page 2</a>'
    mock_fetch_url.return_value = html_content
    mock_extract_links.return_value = ["http://example.com/page2"]
    mock_extract_content.return_value = ["Content from page 1"]

    graph = scraper.scrape_url(url, depth=1)

    assert len(graph) == 1
    assert url in graph
    assert "http://example.com/page2" in graph[url]["edges"]
    assert "Content from page 1" in graph[url]["content"]


def test_scrape_url_multiple_pages(
    scraper, mock_fetch_url, mock_extract_links, mock_extract_content
):
    url = "http://example.com"
    html_content_page1 = '<a href="http://example.com/page2">Link to page 2</a>'
    html_content_page2 = "<p>Content from page 2</p>"
    mock_fetch_url.side_effect = [html_content_page1, html_content_page2]
    mock_extract_links.side_effect = [["http://example.com/page2"], []]
    mock_extract_content.side_effect = [
        ["Content from page 1"],
        ["Content from page 2"],
    ]

    graph = scraper.scrape_url(url, depth=2)

    assert len(graph) == 2
    assert url in graph
    assert "http://example.com/page2" in graph[url]["edges"]
    assert "Content from page 1" in graph[url]["content"]
    assert "Content from page 2" in graph["http://example.com/page2"]["content"]


def test_scrape_url_depth_0(scraper):
    url = "http://example.com"
    graph = scraper.scrape_url(url, depth=0)

    assert len(graph) == 0


def test_scrape_url_invalid_url(scraper):
    url = "invalid_url"
    graph = scraper.scrape_url(url)

    assert len(graph) == 0
