import bs4
import requests as req
import re


def search_wikipedia(wikipedia_link:str) -> str:
    request = req.get(wikipedia_link)
    soup = bs4.BeautifulSoup(request.content, 'html.parser') # html.parser > html5lib
    soup.find('table', attrs={'class': 'infobox'}).decompose()

    found_content = soup.find('div', attrs={'id': 'mw-content-text'}).find('p')
    return re.sub(r"\([^()]*\)|\[\d+]", "",  found_content.text)