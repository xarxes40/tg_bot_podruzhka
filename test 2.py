import re
import requests
from bs4 import BeautifulSoup
import json

headers = {
    'accept': '*/*',
    'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}


def get_all_categories():
    url = 'https://www.podrygka.ru/catalog/'
    req = requests.get(url=url, headers=headers)
    src = req.text

    soup = BeautifulSoup(src, 'lxml')
    categories = soup.find(class_='left-block-float cat_menu').find(
        class_="left-menu").find_all(class_="left-menu__item limit_tab")

    result = {}
    for item in categories:
        subcategories = item.find(
            class_='left-menu-sub left-menu-sub--level-1').find_all(class_='left-menu-sub__item limit_tab')

        for category in subcategories:
            if category.find(class_='left-menu-sub left-menu-sub--level-2'):
                spec_cat = category.find(class_='left-menu-sub left-menu-sub--level-2').find_all(
                    class_='left-menu-sub__item limit_tab')

                for spec_category in spec_cat:
                    try:
                        category_name = spec_category.find(class_='left-menu-sub__link even_in_box').text
                        category_name = re.sub(r'[^\w\s]+|\d+', r'', category_name).strip()
                        category_href = spec_category.find(class_='left-menu-sub__link even_in_box').get('href')
                        result[category_name] = 'https://www.podrygka.ru' + category_href
                    except AttributeError:
                        print('attr')
                        continue
            else:
                try:
                    category_name = category.find(class_='left-menu-sub__link even_in_box').text
                    category_name = re.sub(r'[^\w\s]+|\d+', r'', category_name).strip()
                    category_href = category.find(class_='left-menu-sub__link even_in_box').get('href')
                    result[category_name] = 'https://www.podrygka.ru' + category_href
                except AttributeError:
                    print('attr')
                    continue
    with open('all_categories.json', 'w', encoding='utf-8') as file:
        json.dump(result, file, ensure_ascii=False, indent=4)


get_all_categories()
