import json
import re
import requests
from bs4 import BeautifulSoup


headers = {
    'accept': '*/*',
    'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}


def get_data(key):
    url = 'https://www.podrygka.ru/catalog/'
    req = requests.get(url=url, headers=headers)
    src = req.text

    soup = BeautifulSoup(src, 'lxml')
    categories = soup.find(class_='left-block-float cat_menu').find(
        class_="left-menu").find_all(class_="left-menu__item limit_tab")

    result_dict = {}
    result = []

    for item in categories:
        top_cat = item.find(class_="left-menu__title").find(class_='even_in_box').text
        top_cat = re.sub(r'[^\w\s]+|\d+', r'', top_cat).strip()

        if item.find(class_='left-menu-sub left-menu-sub--level-2'):
            subcategories = item.find(
                class_='left-menu-sub left-menu-sub--level-1').find_all(class_='left-menu-sub__item limit_tab')

            for category in subcategories:
                try:
                    sub_cat = category.find(class_="left-menu-sub__link even_in_box tab-link").text
                    sub_cat = re.sub(r'[^\w\s]+|\d+', r'', sub_cat).strip()

                    spec_cat = category.find(class_='left-menu-sub left-menu-sub--level-2').find_all(
                        class_='left-menu-sub__item limit_tab')

                    for spec_category in spec_cat:
                        try:
                            sp_cat_name = spec_category.find(class_='left-menu-sub__link even_in_box').text
                            sp_cat_name = f'{top_cat}_{sub_cat}_' + re.sub(r'[^\w\s]+|\d+', r'', sp_cat_name).strip()
                            sp_cat_href = spec_category.find(class_='left-menu-sub__link even_in_box').get('href')

                            result_dict[sp_cat_name] = 'https://www.podrygka.ru' + sp_cat_href

                        except AttributeError:
                            continue
                except AttributeError:
                    continue
        else:
            subcategories = item.find(
                class_='left-menu-sub left-menu-sub--level-1').find_all(class_='left-menu-sub__item limit_tab')
            for category in subcategories:
                try:
                    category_name = category.find(class_="left-menu-sub__link even_in_box").text
                    category_name = f'{top_cat}_' + re.sub(r'[^\w\s]+|\d+', r'', category_name).strip()
                    category_href = category.find(class_='left-menu-sub__link even_in_box').get('href')

                    if category_href not in result_dict.values():
                        result_dict[category_name] = 'https://www.podrygka.ru' + category_href

                except AttributeError:
                    continue

    # with open('all_categories.json', 'w', encoding='utf-8') as file:
    #     json.dump(result_dict, file, ensure_ascii=False, indent=4)

    for page in range(1, 10000):
        try:
            url = f'{result_dict.get(key)}?PAGEN_1={page}'
            req = requests.get(url=url, headers=headers)
            src = req.text

            soup = BeautifulSoup(src, 'lxml')
            products = soup.find(class_='products-list').find_all(class_='item-product-card')

            for product in products:
                if product.find(class_='products-list-item__price right_in_box').find(class_='value value--old'):
                    product_name = product.find(class_='products-list-item__title').text
                    product_href = product.find(class_='products-list-item__title').get('href')
                    old_price = product.find(class_='products-list-item__price right_in_box').find(
                        class_='value value--old')
                    old_price = old_price.text.strip()
                    current_price = product.find(class_='products-list-item__price right_in_box').find(
                        class_='value value--current')
                    current_price = current_price.text.replace('Р', '').strip()
                    sale_percent = round(100 - (int(current_price) / (int(old_price) / 100)), 1)

                    if sale_percent > 30:
                        result.append(
                            {
                                'product_name': product_name,
                                'product_href': 'https://www.podrygka.ru' + product_href,
                                'old_price': old_price,
                                'current_price': current_price,
                                'sale_percent': sale_percent
                            }
                        )

        except AttributeError:
            print('Все скидки найдены!')
            break

    with open('result.json', 'w', encoding='utf=8') as file:
        json.dump(result, file, ensure_ascii=False, indent=4)

    # return result


def main():
    get_data('Уход_Лицо_Кремы')


if __name__ == '__main__':
    main()
