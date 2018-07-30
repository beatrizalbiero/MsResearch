from requests import get
from bs4 import BeautifulSoup as bs
import codecs

''' Scraping first page'''
base_url = 'https://www.conjugacao.com.br/verbos-populares/'
verb_url = 'https://www.conjugacao.com.br'

verbospop = get(base_url)
verbospop_page = bs(verbospop.text, 'html.parser')

links = verbospop_page.find_all('li')

pageverbs = []
for link in links:
    a = link.find('a', href=True)
    pageverbs.append(a['href'])

for verb in pageverbs:
    try:
        verb_pg = get(verb_url+verb)
        verbpage = bs(verb_pg.text, 'html.parser')
        x = verbpage.find_all('div')[15]
        infinitivo = verbpage.find_all('div')[0].find_all('div')[5].\
            find_all('br')[1].text
        infinitivo = infinitivo.replace("Infinitivo: ", '')
        result = x.find('span', attrs={"class": "f"}).text

        with codecs.open('scraptest.csv', 'a', 'utf-8') as f:
            f.write(infinitivo + ';' + result + '\n')

    except:
        errors = []
        errors.append(infinitivo)

'''Scraping all pages'''

for page in range(2, 51):
    url = base_url + str(page) + "/"
    verb_url = 'https://www.conjugacao.com.br'

    verbospop = get(url)
    verbospop_page = bs(verbospop.text, 'html.parser')

    links = verbospop_page.find_all('li')

    pageverbs = []
    for link in links:
        a = link.find('a', href=True)
        pageverbs.append(a['href'])

    for verb in pageverbs:
        try:
            verb_pg = get(verb_url+verb)
            verbpage = bs(verb_pg.text, 'html.parser')
            x = verbpage.find_all('div')[15]
            infinitivo = verbpage.find_all('div')[0].find_all('div')[5].\
                find_all('br')[1].text
            infinitivo = infinitivo.replace("Infinitivo: ", '')
            result = x.find('span', attrs={"class": "f"}).text

            with codecs.open('scraptest.csv', 'a', 'utf-8') as f:
                f.write(infinitivo + ';' + result + '\n')
        except:
            errors = []
            errors.append(infinitivo)
