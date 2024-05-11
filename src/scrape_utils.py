# Script that defines functions to scrape a site given a url
# This script should allow you to request content from a webbsite
# And save the content to a list
import requests
import bs4
import src.graph_utils as grp
from collections import deque


class Scraper:
    def __init__(self):
        self.scraped_graph = grp.Graph()

    def fetch_url(url):
        try:
            response = requests.get(url)
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch {url}: {e}")
            return None

    def extract_links(html_content):
        links = []
        if html_content:
            soup = bs4(html_content, 'html.parser')
            for link in soup.find_all('a'):
                href = link.get('href')
                if href and href.startswith('http'):
                    links.append(href)
        return links

    def extract_content(self, html_content, html_element):
        content = []
        if html_content:
            soup = bs4(html_content, 'html.parser')
            for text in soup.select(html_element):
                content.append(text.getText())
        return content

    # Scrape using BFS algorithm to a desired depth
    def scrape_url(self, url, depth=2, html_element='p'):
        graph = self.scraped_graph()
        depth_counter = 0
        queue = deque([url])

        while queue:
            vertex = queue.popleft()
            if vertex not in graph & depth_counter < depth:
                depth_counter += 1
                graph.add_node(vertex)

                html = self.fetch_url(url)
                links = self.extract_links(html)
                content = self.extract_content(html, html_element)

                graph.add_edges(vertex, links)
                graph.add_content(vertex, content)

                for neighbor in graph.get_edges(vertex):
                    if neighbor not in graph:
                        queue.append(neighbor)




