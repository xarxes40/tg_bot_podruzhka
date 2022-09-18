import re
import requests
from bs4 import BeautifulSoup


def get_top_categories(headers):
    url = 'https://www.podrygka.ru/catalog/'
    req = requests.get(url=url, headers=headers)
    src = req.text

    soup = BeautifulSoup(src, 'lxml')
    categories = soup.find(class_='left-block-float cat_menu').find(
        class_="left-menu").find_all(class_="left-menu__item limit_tab")

    all_categories_dict = {}
    for category in categories:
        category_name = category.find(class_='left-menu__title').find(class_='even_in_box').text
        category_name = re.sub(r'[^\w\s]+|\d+', r'', category_name).strip()
        category_href = 'https://www.podrygka.ru' + category.find(class_='left-menu__link tab-link').get('href')
        all_categories_dict[category_name] = category_href
    return get_subcategories(all_categories_dict, headers)


def get_subcategories(categories, headers):
    print(list(categories.keys()))
    url = categories.get(str(input('Введите название категории: ')))
    req = requests.get(url=url, headers=headers)
    src = req.text

    soup = BeautifulSoup(src, 'lxml')
    categories = soup.find(class_='left-menu__item limit_tab active selected').find(
        class_="left-menu-sub left-menu-sub--level-1").find_all(class_="left-menu-sub__item limit_tab")

    if categories[0].find(class_="left-menu-sub left-menu-sub--level-2"):
        all_subcategories_dict = {}
        for category in categories:
            try:
                category_name = category.find(class_='left-menu-sub__link even_in_box tab-link').text
                category_name = re.sub(r'[^\w\s]+|\d+', r'', category_name).strip()
                category_href = category.find(class_='left-menu-sub__link even_in_box tab-link').get('href')
                all_subcategories_dict[category_name] = 'https://www.podrygka.ru' + category_href
            except AttributeError:
                continue
        return get_specific_category(all_subcategories_dict, headers)

    else:
        all_subcategories_dict = {}
        for category in categories:
            try:
                category_name = category.find(class_='left-menu-sub__link even_in_box').text
                category_name = re.sub(r'[^\w\s]+|\d+', r'', category_name).strip()
                category_href = category.find(class_='left-menu-sub__link even_in_box').get('href')
                all_subcategories_dict[category_name] = 'https://www.podrygka.ru' + category_href
            except AttributeError:
                continue
        return get_data(all_subcategories_dict, headers)


def get_specific_category(subcategories, headers):
    print(list(subcategories.keys()))
    url = subcategories.get(str(input('Введите название категории: ')))
    req = requests.get(url=url, headers=headers)
    src = req.text

    soup = BeautifulSoup(src, 'lxml')
    categories = soup.find(class_='left-menu__item limit_tab active').find(
        class_='left-menu-sub__item limit_tab active selected').find(
        class_="left-menu-sub left-menu-sub--level-2").find_all(class_="left-menu-sub__item limit_tab")

    all_specific_categories_dict = {}
    for category in categories:
        try:
            category_name = category.find(class_='left-menu-sub__link even_in_box').text
            category_name = re.sub(r'[^\w\s]+|\d+', r'', category_name).strip()
            category_href = category.find(class_='left-menu-sub__link even_in_box').get('href')
            all_specific_categories_dict[category_name] = 'https://www.podrygka.ru' + category_href
        except AttributeError:
            continue
    return get_data(all_specific_categories_dict, headers)


def get_data(specific_category, headers):
    print(list(specific_category.keys()))
    category_for_scrap = str(input('Введите название категории: '))
    for page in range(1, 10000):
        try:
            url = f'{specific_category.get(category_for_scrap)}?PAGEN_1={page}'
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

                    if sale_percent < 30:
                        print(f'--- {product_name} со старой ценой {old_price} сейчас стоит {current_price}. '
                              f'Скидка составляет {sale_percent} %. '
                              f'Небольшая скидочка, но если нужно, можно рассмотреть.'
                              f'Вот ссылочка: https://www.podrygka.ru{product_href} ---\n')

                    elif 30 <= sale_percent < 50:
                        print(f'---{product_name} со старой ценой {old_price} сейчас стоит {current_price}. '
                              f'Скидка составляет {sale_percent} %. '
                              f'Средняя скидка,соответственно можно рассмотреть.'
                              f'Вот ссылочка: https://www.podrygka.ru{product_href} ---\n')

                    elif 50 <= sale_percent < 70:
                        print(f'---{product_name} со старой ценой {old_price} сейчас стоит {current_price}. '
                              f'Скидка составляет {sale_percent} %. '
                              f'Хорошая скидка, посмотри, может что-то нужно?.'
                              f'Вот ссылочка: https://www.podrygka.ru{product_href} ---\n')

                    elif sale_percent >= 70:
                        print(f'---{product_name} со старой ценой {old_price} сейчас стоит {current_price}. '
                              f'Скидка составляет {sale_percent} %. Скидка бомба!!!.'
                              f'Вот ссылочка: https://www.podrygka.ru{product_href} ---\n')

        except AttributeError:
            print('Все скидки найдены!')
            break


def main():

    headers = {
        'accept': '*/*',
        'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }
    get_top_categories(headers=headers)


if __name__ == '__main__':
    main()
