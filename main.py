from unittest import expectedFailure

import requests
from bs4 import BeautifulSoup
import lxml

url = 'https://habr.com/ru/articles/top/daily/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
}

def get_page():
    try:
        req = requests.get(url)
        req.raise_for_status()
        src = req.text
    except requests.RequestException as e:
        print(f'Ошибка при загрузке страницы {e}')
        return []

    soup = BeautifulSoup(src, 'lxml')
    title = []
    views = []

    title_elements = soup.find_all('a', class_='tm-title__link')
    for title_el in title_elements:
        t = title_el.find('span')
        title.append(t.text.strip()) # сохранение названий в список

    view_elements = soup.find_all('span', class_='tm-icon-counter__value')
    for view_el in view_elements:
        v = view_el.get('title')
        views.append(v.strip())
    dicty = dict(zip(title, views))
    return dicty



def main():
    print('Загрузка данных...')
    print(get_page())

if __name__ == '__main__':
    main()






