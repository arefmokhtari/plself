#                   [   Plague Dr.  ]
# - - - - - - - - - - - - - - - - - - - - - - - - - - - #
from bs4 import BeautifulSoup as bs
import requests as rq
# - - - - - - - - - - - - - - - - - - - - - - - - - - - #
coinmarketcap = 'https://coinmarketcap.com'
pages = '/?page='
# - - - - - - - - - - - - - - - - - - - - - - - - - - - #
def collection_dict(*data) -> dict:
    d = {}
    for dt in data: d.update(dt)
    return d

def _2float(text: str) -> float: 
    return float(text.replace('.','00'))
# - - - - - - - - - - - - - - - - - - - - - - - - - - - #
class getCoin:
    def __init__(self, *, site: str = coinmarketcap, page: int = None, loop: bool = False):
        if not loop:
            self.update(site=site, page=page)
    def length(self) -> int:
        return len(self.tags)
    def update(self, *, site: str = coinmarketcap, page: int = None) -> None:
        self.url = site if page == None else site+pages+str(page)
        self.code = rq.get(self.url)
        self.site = bs(self.code.text, 'html.parser')
        self.tags = self.site.select('.h7vnx2-2 > tbody:nth-child(3) > tr')
    def get_name(self, index: int) -> str:
        name = self.tags[index].select('td:nth-child(3)')
        tag_p = name[0].find_all('p')
        if tag_p == []:
            name = self.tags[index].select('td:nth-child(3)')[0].find_all('span', class_='')[0].text
        else:
            name = tag_p[0].text
        return name.lower().replace(' ','_')
    def get_price(self, index: int) -> float:
        name = self.tags[index].select('td:nth-child(4)')[0]
        return name.span.text[1:] #_2float(name.span.text[1:].replace(',', ''))
    def get_dict(self) -> dict:
        data = {}
        for coin_length in range(self.length()):
            data[self.get_name(coin_length)] = self.get_price(coin_length)
        return data
        
# - - - - - - - - - - - - - - - - - - - - - - - - - - - #