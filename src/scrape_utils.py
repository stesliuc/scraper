# Script that defines functions to scrape a site given a url
# This script should allow you to request content from a webbsite
# And save the content to a list
import requests
from bs4 import BeautifulSoup
import src.graph_utils as grp
from collections import deque


class Scraper:
    def __init__(self):
        self.scraped_graph = grp.Graph()

    def fetch_url(self, url):
        try:
            response = requests.get(url)
            return response.text
        except requests.exceptions.RequestException as e:
            print("Failed to fetch {url}: {e}")
            return None

    def extract_links(self, html_content):
        links = []
        if html_content:
            soup = BeautifulSoup(html_content, "html.parser")
            for link in soup.find_all("a"):
                href = link.get("href")
                if href and href.startswith("http"):
                    links.append(href)
        return links

    def extract_content(self, html_content, html_element):
        content = []
        if html_content:
            soup = BeautifulSoup(html_content, "html.parser")
            for text in soup.select(html_element):
                content.append(text.getText())
        return content

    # Scrape using BFS algorithm to a desired depth
    def scrape_url(self, url, depth=2, html_element="p"):
        G = self.scraped_graph
        depth_counter = 0
        queue = deque([url])

        # TODO add a visited node hash map for non-tree graphs
        while queue:
            n = len(queue)
            for _ in range(n):
                vertex = queue.popleft()
                if (vertex not in G.graph) and (depth_counter < depth):
                    html = self.fetch_url(vertex)
                    if html is None:
                        continue
                    G.add_node(vertex)
                    links = self.extract_links(html)
                    contents = self.extract_content(html, html_element)

                    for link in links:
                        G.add_edge(vertex, link)
                    for content in contents:
                        G.add_content(vertex, content)

                    for neighbor in G.get_edges(vertex):
                        if neighbor not in G.graph:
                            queue.append(neighbor)
            depth_counter += 1
        return G.graph
