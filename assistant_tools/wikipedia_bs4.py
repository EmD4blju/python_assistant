import bs4
import requests as req
import re
def search_wikipedia(wikipedia_link:str) -> str: # [Notice]: function searches Wikipedia (web-scrapping) for content
    request = req.get(wikipedia_link) # sends HTTP GET request for HTML
    soup = bs4.BeautifulSoup(request.content, 'html.parser') # initiates HTML parser
    to_decompose = soup.find('table', attrs={'class': 'infobox'})
    if to_decompose is not None: to_decompose.decompose()
    found_content = soup.find('div', attrs={'id': 'mw-content-text'}).find('p') # searches for a paragraph
    return re.sub(r"\([^()]*\)|\[\d+]", "",  found_content.text) # formats acquired content