import bs4
import requests as req
import re

# Did you know that polish wikipedia has actually different scheme than others?
# (Possibly every one differs from another)
# Estúpida como la mierda
def search_wikipedia(wikipedia_link:str) -> str:
    request = req.get(wikipedia_link)
    soup = bs4.BeautifulSoup(request.content, 'html.parser') # html.parser > html5lib
    to_decompose = soup.find('table', attrs={'class': 'infobox'})
    if to_decompose is not None: to_decompose.decompose()
    found_content = soup.find('div', attrs={'id': 'mw-content-text'}).find('p')
    return re.sub(r"\([^()]*\)|\[\d+]", "",  found_content.text)

if __name__ == '__main__':
    print(search_wikipedia('https://pl.wikipedia.org/wiki/Komputer_kwantowy'))