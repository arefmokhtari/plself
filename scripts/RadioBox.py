from __future__ import print_function
from threading import Thread
from bs4.element import Tag
import requests
import time
from bs4 import BeautifulSoup
import re
from .Color import Color
import sys
from .utils import *


def write(text: str, color: str = Color.RESET, link: bool = False) -> None:
    """
    Write text to console

    :param text: str
    :param link: bool - example: "Visit [link=https://www.google.com]Google[/link]!"
    :param color: str - example: Color.RED
    :return: None
    """
    if link:
        sys.stdout.write(color)
        print(text, end="")
        sys.stdout.write(Color.RESET + "\n")
        return
    sys.stdout.write(color + text + Color.RESET)


# q = input("Search radio: " + Color.GREEN)
# q = 'berea fm'
lim = 5
ofst = 0
write(Color.RESET)

ta = time.time()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Host": "onlineradiobox.com",
    "Connection": "keep-alive"
}


class StationObject:
    def __init__(self, element: Tag):
        self.__element = element

    def name(self) -> str:
        return self.__element.find('figure', {
            'class': 'stations__station__title'}).find('a').find('figcaption', {'class': 'station__title__name'}).text

    def url(self) -> str:
        return self.__element.find('figure', {'class': 'stations__station__title'}).find('a').get('href')

    def logo(self) -> str:
        return self.__element.find('figure', {
            'class': 'stations__station__title'}).find('a').find('img', {'class': 'station__title__logo'}).get('src')

    def tags(self) -> list:
        if self.__element.find('ul', {'class': 'stations__station__tags'}):
            return [i.find('a').text for i in
                    self.__element.find('ul', {'class': 'stations__station__tags'}).find_all('li')]
        else:
            return []

    def country(self) -> tuple:
        c = self.__element.find('ul', {'class': "stations__station__info"}).find('li').find("a", {'class': 'i-flag'})
        return c.get('class')[1], c.get('title'), c.get('href')  # country code, country name, country url

    def region(self) -> tuple:
        c = self.__element.find('ul', {'class': "stations__station__info"}).find('li').find_all("a")
        if len(c) == 3:
            return c[1].get('href'), c[1].text  # region url, region name
        elif len(c) == 2:
            if '&ct=' not in c[1].get('href'):
                return c[1].get('href'), c[1].text  # region url, region name
            elif '&r=' in c[1].get('href'):
                __region_code = re.search(r'&r=(\d+)', c[1].get('href')).group(1)
                return f'https://onlineradiobox.com/search?r={__region_code}', c[1].text  # region url, region name

    def city(self) -> tuple or None:
        c = self.__element.find('ul', {'class': "stations__station__info"}).find('li').find_all("a")
        if len(c) == 3:
            return c[2].get('href'), c[2].text  # city url, city name
        elif len(c) == 2:
            if '&ct=' in c[1].get('href'):
                return c[1].get('href'), c[1].text  # city url, city name
            else:
                return None
        else:
            return None

    def listeners(self) -> int:
        return int(self.__element.find('ul', {'class': "stations__station__metric"}).find('li', {
            "class": "i-listeners"}).text.strip())

    def rating(self) -> int:
        return int(self.__element.find('ul', {'class': "stations__station__metric"}).find('li', {
            "class": "i-chart"}).text.strip())


class Station_data:
    def __init__(self):
        self.__data = {}

    def add(self, data_id, stream_id, stream_type, stream_url, error=None):
        self.__data[data_id] = [stream_id, stream_type, stream_url, error]

    def get_all(self):
        return self.__data

    def get(self, data_id):
        return self.__data[data_id]


def check_stream(link):
    try:
        r = requests.get(link, headers={'Icy-MetaData': '1'}, stream=True)
        if r.status_code == 200:
            return True
        else:
            return False
    except:
        return False


def get_playing_stream_title(url):
    encoding = 'latin1'
    info = ''

    radio_session = requests.Session()

    count = 0
    while True:
        count += 1
        if count > 5:
            return None

        radio = radio_session.get(url, headers={'Icy-MetaData': '1'}, stream=True)

        try:
            metaint = int(radio.headers['icy-metaint'])
        except KeyError:
            return None
        stream = radio.raw

        audio_data = stream.read(metaint)
        meta_byte = stream.read(1)

        if meta_byte:
            meta_length = ord(meta_byte) * 16

            meta_data = stream.read(meta_length).rstrip(b'\0')

            stream_title = re.search(br"StreamTitle='([^']*)';", meta_data)

            if stream_title:

                stream_title = stream_title.group(1).decode(encoding, errors='replace')

                if info != stream_title:
                    info = stream_title
                else:
                    return info

            else:
                return None

        time.sleep(0.01)


def get_playing_stream_title2(url):
    try:
        import urllib2
    except ImportError:  # Python 3
        import urllib.request as urllib2

    url = get_exact_link(url)
    encoding = 'latin1'  # default: iso-8859-1 for mp3 and utf-8 for ogg streams
    request = urllib2.Request(url, headers={'Icy-MetaData': 1})  # request metadata
    response = urllib2.urlopen(request)
    metaint = int(response.headers['icy-metaint'])
    for _ in range(10):  # # title may be empty initially, try several times
        response.read(metaint)  # skip to metadata
        metadata_length = struct.unpack('B', response.read(1))[0] * 16  # length byte
        metadata = response.read(metadata_length).rstrip(b'\0')
        # extract title from the metadata
        m = re.search(br"StreamTitle='([^']*)';", metadata)
        if m:
            title = m.group(1)
            if title:
                break
    else:
        return None
    return title.decode(encoding, errors='replace')


def get_all_genres():
    url = 'https://onlineradiobox.com/genres/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    tags_list = soup.find('div', {'id': 'tags'}).find_all('dl')
    genres = []
    for _i in tags_list:
        dds = [_j for _j in _i.find_all('dd')]
        genres_list = [k for k in dds[0].find_all('a')] + [k for k in dds[1].find_all('a')]
        genres_text = [k.text for k in genres_list]
        genres_link = [k.get('href') for k in genres_list]
        genres.append([(_i.find('dt').find('a').text, _i.find('dt').find('a').get('href'))] +
                      list(zip(genres_text, genres_link)))

        # [ [('tag_title', 'tag_url), (genre_title, genre_url), (genre_title, genre_url), ...], ...]
    del genres_list, genres_text, genres_link
    return genres


class radioBox:
    def __init__(self):
        self.url = 'https://onlineradiobox.com/search?part=1&offset={OFFSET}&q={QUERY}'

    def rUrl(self, offset, query):
        return self.url.replace("{OFFSET}", str(offset)).replace("{QUERY}", str(query))

    def get_stations_by_query(self, query, limit=200, offset=0) -> list[StationObject]:
        __stations_list = []
        r = requests.get(self.rUrl(offset, query), headers=headers)
        r.close()

        __soup = BeautifulSoup(r.text, 'html.parser')
        __stations_list = __soup.find('ul', {'class': 'stations-list'}).find_all('li', {'class': 'stations__station'})

        # __stations = list(map(StationObject, __stations_list))
        if limit == 20:
            __stations = list(map(StationObject, __stations_list))
        elif limit < 20:
            __stations = list(map(StationObject, __stations_list[:limit]))
        else:
            _offset = __soup.find('ul', {'class': 'stations-list'}).get('offset')
            while True:
                _r = requests.get(self.rUrl(_offset, query), headers=headers)
                _r.close()

                __soup = BeautifulSoup(_r.text, 'html.parser')
                try:
                    _temp_list = __soup.find('ul', {'class': 'stations-list'}).find_all('li', {
                        'class': 'stations__station'})
                    for i in _temp_list:
                        print(i.find('figure', {
                            'class': 'stations__station__title'}).find('a').find('figcaption',
                                                                                 {
                                                                                     'class': 'station__title__name'}).text)
                    __stations_list = __stations_list + _temp_list
                except AttributeError:
                    __stations = list(map(StationObject, __stations_list[:limit]))
                    break
                _offset = __soup.find('ul', {'class': 'stations-list'}).get('offset')

                if len(__stations_list) >= limit:
                    __stations = list(map(StationObject, __stations_list[:limit]))
                    break
        print(len(__stations))
        return __stations


std = Station_data()


def stream_scraper(link: str, header, stations: list[StationObject]):
    __r = requests.get(link, headers=header)
    __r.close()
    __soup = BeautifulSoup(__r.text, 'html.parser')
    try:
        station_stream_url = __soup.find('section', {'class': 'station'}). \
            find('button', {'class': 'station_play'}).get('stream')
        station_stream_type = __soup.find('section', {'class': 'station'}). \
            find('button', {'class': 'station_play'}).get('streamtype')
        station_radio_id = __soup.find('section', {'class': 'station'}). \
            find('button', {'class': 'station_play'}).get('radioid')
        std.add([i.url() for i in stations].index(link.removeprefix('https://onlineradiobox.com')), station_radio_id,
                station_stream_type, station_stream_url)
    except AttributeError as e:
        erText = __soup.find('head').find('title').text
        if 'unavailable' in erText:
            write(f"\n{Color.GRAY}[!] Error: {Color.RED}{erText}{Color.RESET}")
        else:
            write(f"\n{Color.GRAY}{erText}{Color.RESET}")
        std.add([i.url() for i in stations].index(link.removeprefix('https://onlineradiobox.com')), '', '', '', erText)


def get_stream_by_link(link, stations: list[StationObject]):
    Thread(target=stream_scraper, args=(link, headers, stations)).start()


def main(stations: list[StationObject], query):
    write(f"[+] Starting search for '{query}'", Color.LIGHT_BLUE)
    if not stations:
        print("\x1b[1m\n" + Color.RED + 'Nothing found!' + Color.RESET + "\x1b[0m")
        return
    write("\r[+] Loading stations info ...", Color.CYAN)
    station_names = [i.name() for i in stations]
    station_urls = [i.url() for i in stations]
    station_logos = [i.logo() for i in stations]
    station_tags = [', '.join(i.tags()) for i in stations]
    station_country = [i.country() for i in stations]
    station_region = [i.region() for i in stations]
    station_rgn = []
    for p in station_region:
        if not p:
            station_rgn.append(("❌", "❌"))
        else:
            station_rgn.append(p)
    station_region = station_rgn

    station_city = [(i.city() if i.city() else "") for i in stations]
    station_listeners = [i.listeners() for i in stations]
    station_rating = [i.rating() for i in stations]
    station_stream = []
    write("\r[+] Loading stations streams ...", Color.CYAN)
    for i in station_urls:
        get_stream_by_link("https://onlineradiobox.com" + i, stations)
    while True:
        if len(std.get_all()) == len(station_urls):
            for i in station_urls:
                station_stream.append(std.get(station_urls.index(i)))

            write(f"\r[+] Loading stations streams ... {Color.GREEN}Done ✔" + " " * 30 + "\u200C",
                  Color.CYAN)
            write("\n[+] Stations info loaded" + " " * 30 + "\n", Color.GREEN)
            break
        else:
            write(f"\r[+] Loading stations streams ... {Color.GREEN}{len(std.get_all())}"
                  f"{Color.CYAN}/{Color.GREEN}{len(station_urls)}", Color.CYAN)
        time.sleep(0.1)

    write("\n")

    station_counter = 1
    for i in station_urls:
        # print(i)
        # print(station_region)
        print(Color.RED + "[" + str(station_counter) + "]  " + Color.GREEN +
              f"\t{station_names[station_urls.index(i)]} " + Color.BLACK +
              ("┈" * (len(max(station_names, key=len)) - len(station_names[station_urls.index(i)]))) +
              Color.CYAN + "  https://onlineradiobox.com" + i + Color.BLACK + "  " +
              "┈" * (len(max(station_urls, key=len)) - len(i) + 2) + Color.BLUE + "  " +

              (station_tags[station_urls.index(i)]
               .replace(',', Color.GREEN + ',' + Color.BLUE) if station_tags[
                  station_urls.index(i)] else Color.RED + "Unknown" + Color.RESET) +
              #   "http:" + station_logos[station_urls.index(i)] + Color.RESET +
              #
              #   station_country[station_urls.index(i)][0] + "\u001B[31m, \u001B[34m" +
              #   station_country[station_urls.index(i)][1] + "\u001B[31m, \u001B[34m" + " " + Color.BLACK +
              #   "┈" * ((len(max([j[1] for j in station_country], key=len))) - len(
              # station_country[station_urls.index(i)][1])) + " \u001B[34m" +
              #   station_country[station_urls.index(i)][2] +

              #   station_region[station_urls.index(i)][1] + "\u001B[31m, \u001B[34m" +
              #   " " * ((len(max([j[1] for j in station_region], key=len))) - len(
              # station_region[station_urls.index(i)][1])) +
              #   " " + station_region[station_urls.index(i)][0] +
              #
              # station_city[station_urls.index(i)][1] + "\u001B[31m, \u001B[34m" +
              # " " * ((len(max([j[1] for j in station_city], key=len))) - len(station_city[station_urls.index(i)][1])) +
              # " " + station_city[station_urls.index(i)][0] +
              #
              # "🎧" + str(station_listeners[station_urls.index(i)]) + "\u001B[31m  " +
              # "♥️\u001B[34m" + str(station_rating[station_urls.index(i)]) +
              #
              # station_stream[station_urls.index(i)][0] + "\u001B[31m, \u001B[34m" +  # id
              # # station_stream[station_urls.index(i)][1] +  # type
              ("\u001B[31m, \u001B[34m" +
               station_stream[station_urls.index(i)][2] if station_stream[station_urls.index(i)][
                                                               3] is None else '') +  # url
              "\u001B[31m, \u001B[34m" +
              # show error
              (Color.RED + 'Error: ' + Color.RED + station_stream[station_urls.index(i)][3] + Color.RESET if
               station_stream[station_urls.index(i)][3] else '') +

              Color.RESET)

        station_counter += 1

# main(stn)

# stt = get_playing_stream_title(input("Enter stream url: "))
# print(stt)

# for i in get_all_genres():
#     write(f'- [link=https://onlineradiobox.com{i[0][1]}]{i[0][0]}[/link]', link=True, color=Color.BLUE)
#     for j in i[1:]:
#         write(f'[link=https://onlineradiobox.com{j[1]}]{j[0]}[/link]', link=True)

# tb = time.time()
# print(colorama.Style.DIM +
#       Color.YELLOW + f"\ntime: {str(tb - ta).split('.')[0] + '.' + str(tb - ta).split('.')[-1][:3]}"
#                             "\n" + Color.RESET + colorama.Style.RESET_ALL)
