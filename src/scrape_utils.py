# Function that opens a website ans aves a beautiful soup class
import requests
import bs4


def open_site(url):
    site = requests.get(url)
    siteSoup = bs4.BeautifulSoup(site.text, 'html.parser')
    return siteSoup


# Function that given a BeautifulSoup website object, returns all the parsed text on the page
def scrape_text(bs4TextClass, html_obj='p'):
    content = bs4TextClass.select(html_obj)
    output = []
    for item in content:
        output.append(item.getText())

    return output
