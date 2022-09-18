import json
import time
from aiogram.utils.markdown import hbold, hlink
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from tg_bot.keyboard import *
from scrapper import get_data


async def start_bot(message: types.Message):
    await message.answer('Привет! Давай найдем для тебя что-нибудь :)', reply_markup=keyboard)


async def show_categories(message: types.Message):
    await message.answer('Выбери категорию', reply_markup=top_inline_kb)


class Care:
    @staticmethod
    async def show_care(callback: types.CallbackQuery):
        await callback.message.answer('Теперь выбери подкатегорию', reply_markup=care_kb)

    @staticmethod
    async def show_face(callback: types.CallbackQuery):
        await callback.message.answer('Посмотри, что тебе нужно', reply_markup=face_care_kb)

    class Face:
        @staticmethod
        async def find_creams(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Уход_Лицо_Кремы')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_masks(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Уход_Лицо_Маски')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_skin(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Уход_Лицо_Для проблемной кожи')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_wash(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Уход_Лицо_Умывание')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_clear_makeup(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Уход_Лицо_Для снятия макияжа')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_tonics(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Уход_Лицо_Тоники и лосьоны')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_serums(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Уход_Лицо_Сыворотки')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_scrubs(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Уход_Лицо_Скрабы и пилинги')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_skin_around_eyes(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Уход_Лицо_Для кожи вокруг глаз')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_lips(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Уход_Лицо_Для губ')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

    @staticmethod
    async def show_body(callback: types.CallbackQuery):
        await callback.message.answer('Посмотри, что тебе нужно', reply_markup=body_care_kb)

    class Body:
        @staticmethod
        async def find_feeding(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Уход_Тело_Питание и увлажнение')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_shower(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Уход_Тело_Гели и кремы для душа')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_for_hands(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Уход_Тело_Для рук')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_scrubs(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Уход_Тело_Скрабы и пилинги')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_soap(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Уход_Тело_Мыло')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_deodorants(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Уход_Тело_Дезодоранты')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_clear_hair(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Уход_Тело_Удаление волос')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_sponges(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Уход_Тело_Мочалки и губки')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_for_legs(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Уход_Тело_Для ног')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_bath_salt(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Уход_Тело_Пена соль масла для ванны')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_handkerchief(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Уход_Тело_Носовые платки')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

    @staticmethod
    async def show_hair(callback: types.CallbackQuery):
        await callback.message.answer('Посмотри, что тебе нужно', reply_markup=hair_care_kb)

    class Hair:
        @staticmethod
        async def find_shampoo(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Уход_Волосы_Шампуни')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_balsams(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Уход_Волосы_Бальзамы и ополаскиватели')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_masks(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Уход_Волосы_Маски')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_special_means(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Уход_Волосы_Специальные средства')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_styling(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Уход_Волосы_Средства для укладки')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_staining(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Уход_Волосы_Окрашивание')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

    @staticmethod
    async def show_mouth(callback: types.CallbackQuery):
        await callback.message.answer('Посмотри, что тебе нужно', reply_markup=mouth_care_kb)

    class Mouth:
        @staticmethod
        async def find_tooth_brush(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Уход_Уход за полостью рта_Зубные щетки')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_tooth_paste(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Уход_Уход за полостью рта_Зубные пасты')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_conditioner(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Уход_Уход за полостью рта_Ополаскиватели')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_special_care(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Уход_Уход за полостью рта_Специальный уход')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

    @staticmethod
    async def show_tan(callback: types.CallbackQuery):
        await callback.message.answer('Посмотри, что тебе нужно', reply_markup=tan_care_kb)

    class Tan:
        @staticmethod
        async def find_sunscreens(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Уход_Загар_Защита от солнца')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_after_tan(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Уход_Загар_После загара')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_auto_tan(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Уход_Загар_Автозагар')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_tan_activation(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Уход_Загар_Активация загара')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

    @staticmethod
    async def show_hygiene(callback: types.CallbackQuery):
        await callback.message.answer('Посмотри, что тебе нужно', reply_markup=hygiene_care_kb)

    class Hygiene:
        @staticmethod
        async def find_gasket(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Уход_Личная гигиена здоровье_Прокладки')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_tampons(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Уход_Личная гигиена здоровье_Тампоны')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_intimate_hygiene(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Уход_Личная гигиена здоровье_Средства для интимной гигиены')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_cotton_buds_and_disks(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Уход_Личная гигиена здоровье_Ватные палочки и диски')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_wet_wipes(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Уход_Личная гигиена здоровье_Влажные салфетки')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_sanitizer(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Уход_Личная гигиена здоровье_Санитайзеры')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_goods_for_health(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Уход_Личная гигиена здоровье_Товары для здоровья')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)


class Makeup:
    @staticmethod
    async def show_makeup(callback: types.CallbackQuery):
        await callback.message.answer('Посмотри, что тебе нужно', reply_markup=makeup_kb)

    @staticmethod
    async def show_face(callback: types.CallbackQuery):
        await callback.message.answer('Посмотри, что тебе нужно', reply_markup=face_makeup_kb)

    class Face:
        @staticmethod
        async def find_corrector(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Макияж_Лицо_Корректор')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_foundation(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Макияж_Лицо_Тональные средства')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_powder(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Макияж_Лицо_Пудра')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_blush(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Макияж_Лицо_Румяна')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_highlighter(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Макияж_Лицо_Хайлайтеры')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_circuit(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Макияж_Лицо_Контурирование')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_other(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Макияж_Лицо_Прочее')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

    @staticmethod
    async def show_eyes(callback: types.CallbackQuery):
        await callback.message.answer('Посмотри, что тебе нужно', reply_markup=eyes_makeup_kb)

    class Eyes:
        @staticmethod
        async def find_base_for_shadows(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Макияж_Глаза_База под тени')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_pencil(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Макияж_Глаза_Карандаши')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_shadows(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Макияж_Глаза_Тени')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_ink(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Макияж_Глаза_Тушь')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_eyeliners(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Макияж_Глаза_Подводки')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_false_eyelashes(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Макияж_Глаза_Накладные ресницы')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

    @staticmethod
    async def show_lips(callback: types.CallbackQuery):
        await callback.message.answer('Посмотри, что тебе нужно', reply_markup=lips_makeup_kb)

    class Lips:
        @staticmethod
        async def find_sparkles(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Макияж_Губы_Блески')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_pencils(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Макияж_Губы_Карандаши')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_lipstick(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Макияж_Губы_Помада')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_tint(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Макияж_Губы_Тинт')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_other(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Макияж_Губы_Прочее')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

    @staticmethod
    async def show_nails(callback: types.CallbackQuery):
        await callback.message.answer('Посмотри, что тебе нужно', reply_markup=nails_makeup_kb)

    class Nails:
        @staticmethod
        async def find_nail_design(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Макияж_Ногти_Дизайн ногтей')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_lack_remover(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Макияж_Ногти_Средства для снятия лака')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_lack(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Макияж_Ногти_Лаки')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_nail_care(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Макияж_Ногти_Уход за ногтями')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

    @staticmethod
    async def show_brows(callback: types.CallbackQuery):
        await callback.message.answer('Посмотри, что тебе нужно', reply_markup=brows_makeup_kb)

    class Brows:
        @staticmethod
        async def find_paint_for_brows(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Макияж_Брови_Краска для ресниц и бровей')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_pencil_for_brows(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Макияж_Брови_Карандаш для бровей')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_ink_for_brows(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Макияж_Брови_Тушь для бровей')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_shadows_for_brows(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Макияж_Брови_Тени для бровей')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_set_for_brows(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Макияж_Брови_Набор для бровей')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_gel_for_brows(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Макияж_Брови_Гель для бровей')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_other(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Макияж_Брови_Прочее')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

    @staticmethod
    async def show_decorations(callback: types.CallbackQuery):
        await callback.message.answer('Посмотри, что тебе нужно', reply_markup=decorations_makeup_kb)

    class Decorations:
        @staticmethod
        async def find_applications(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Макияж_Украшения для тела и волос_Аппликации на тело тату')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)


class Accessories:
    @staticmethod
    async def show_accessories(callback: types.CallbackQuery):
        await callback.message.answer('Посмотри, что тебе нужно', reply_markup=accessories_kb)

    @staticmethod
    async def show_makeup_accessories(callback: types.CallbackQuery):
        await callback.message.answer('Посмотри, что тебе нужно', reply_markup=for_makeup_accessories_kb)

    class ForMakeUp:
        @staticmethod
        async def find_brushes(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Аксессуары_Для макияжа_Кисти')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_sponges(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Аксессуары_Для макияжа_Спонжи')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_applicators(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Аксессуары_Для макияжа_Аппликаторы')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_tweezers(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Аксессуары_Для макияжа_Пинцеты')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_other(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Аксессуары_Для макияжа_Прочее')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

    @staticmethod
    async def show_sub_accessories(callback: types.CallbackQuery):
        await callback.message.answer('Посмотри, что тебе нужно', reply_markup=accessories_accessories_kb)

    class SubAccessories:
        @staticmethod
        async def find_other(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Аксессуары_Аксессуары_Прочее')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_business_accessories(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Аксессуары_Аксессуары_Деловые аксессуары')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_cosmetic_bag(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Аксессуары_Аксессуары_Косметички')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_bag(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Аксессуары_Аксессуары_Сумки')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

    @staticmethod
    async def show_women_hair(callback: types.CallbackQuery):
        await callback.message.answer('Посмотри, что тебе нужно', reply_markup=for_hair_women_accessories_kb)

    class WomenHair:
        @staticmethod
        async def find_crabs(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Аксессуары_Для волос женские_Крабы')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_brush(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Аксессуары_Для волос женские_Щетки для брашинга')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_staining_hair(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Аксессуары_Для волос женские_Для окрашивания волос')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_hair_band(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Аксессуары_Для волос женские_Ободки')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_sets(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Аксессуары_Для волос женские_Наборы')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_hairpin(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Аксессуары_Для волос женские_Заколки')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_scrunchy(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Аксессуары_Для волос женские_Резинки')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_hair_comb(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Аксессуары_Для волос женские_Расчески')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_curlers(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Аксессуары_Для волос женские_Бигуди')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_other(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Аксессуары_Для волос женские_Прочее')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

    @staticmethod
    async def show_kids_hair(callback: types.CallbackQuery):
        await callback.message.answer('Посмотри, что тебе нужно', reply_markup=for_hair_kids_accessories_kb)

    class KidsHair:
        @staticmethod
        async def find_crabs(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Аксессуары_Для волос детские_Крабы')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_hair_band(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Аксессуары_Для волос детские_Ободки')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_sets(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Аксессуары_Для волос детские_Наборы')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_hairpin(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Аксессуары_Для волос детские_Заколки')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_scrunchy(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Аксессуары_Для волос детские_Резинки')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_other(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Аксессуары_Для волос детские_Прочее')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

    @staticmethod
    async def show_tights(callback: types.CallbackQuery):
        await callback.message.answer('Посмотри, что тебе нужно', reply_markup=tights_accessories_kb)

    class Tights:
        @staticmethod
        async def find_tights(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Аксессуары_Белье и колготки_Колготки')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_stockings(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Аксессуары_Белье и колготки_Чулки')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_socks(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Аксессуары_Белье и колготки_Носки')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_knee_socks(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Аксессуары_Белье и колготки_Гольфы')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_underwear(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Аксессуары_Белье и колготки_Белье')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

    @staticmethod
    async def show_bijouterie(callback: types.CallbackQuery):
        await callback.message.answer('Посмотри, что тебе нужно', reply_markup=bijouterie_accessories_kb)

    class Bijouterie:
        @staticmethod
        async def find_neck_decoration(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Аксессуары_Бижутерия_Украшения на шею')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_earrings(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Аксессуары_Бижутерия_Серьги')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_trinket(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Аксессуары_Бижутерия_Брелоки')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_for_kids(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Аксессуары_Бижутерия_Для детей')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_rings(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Аксессуары_Бижутерия_Кольца')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_bracer(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Аксессуары_Бижутерия_Браслеты')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_brooch(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Аксессуары_Бижутерия_Броши')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_other(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Аксессуары_Бижутерия_Прочее')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)


class HomeStuff:
    @staticmethod
    async def show_home_stuff(callback: types.CallbackQuery):
        await callback.message.answer('Посмотри, что тебе нужно', reply_markup=home_stuff_kb)

    @staticmethod
    async def show_chemicals(callback: types.CallbackQuery):
        await callback.message.answer('Посмотри, что тебе нужно', reply_markup=chemical_home_stuff_kb)

    class Chemical:
        @staticmethod
        async def find_air_fresher(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Для дома_Бытовая химия_Освежители воздуха')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_for_bath(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Для дома_Бытовая химия_Для ванных и туалетов')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_for_wash(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Для дома_Бытовая химия_Для стирки')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_for_insects(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Для дома_Бытовая химия_Средства от насекомых')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_clothes_care(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Для дома_Бытовая химия_Для ухода за одеждой')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_shoes_care(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Для дома_Бытовая химия_Для ухода за обувью')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_fro_kitchen(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Для дома_Бытовая химия_Для кухни')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_for_rooms(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Для дома_Бытовая химия_Для комнат')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

    @staticmethod
    async def show_paper_stuff(callback: types.CallbackQuery):
        await callback.message.answer('Посмотри, что тебе нужно', reply_markup=paper_product_home_stuff_kb)

    class PaperProduct:
        @staticmethod
        async def find_toilet_paper(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Для дома_Бумажная продукция_Туалетная бумага')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)

        @staticmethod
        async def find_napkins(callback: types.CallbackQuery):
            await callback.message.answer('Сейчас найдем...')

            get_data('Для дома_Бумажная продукция_Салфетки и полотенца')

            with open('result.json', encoding='utf-8') as file:
                data = json.load(file)

            if not data:
                await callback.message.answer('Нет результатов.')

            for index, product in enumerate(data):
                card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                       f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                       f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                       f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

                if index % 20 == 0:
                    time.sleep(3)

                await callback.message.answer(card)


class FoodAndDrinks:
    @staticmethod
    async def show_food_and_drinks(callback: types.CallbackQuery):
        await callback.message.answer('Посмотри, что тебе нужно', reply_markup=food_and_drinks)

    @staticmethod
    async def find_bar(callback: types.CallbackQuery):
        await callback.message.answer('Сейчас найдем...')

        get_data('Еда и напитки_Батончики')

        with open('result.json', encoding='utf-8') as file:
            data = json.load(file)

        if not data:
            await callback.message.answer('Нет результатов.')

        for index, product in enumerate(data):
            card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                   f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                   f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                   f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

            if index % 20 == 0:
                time.sleep(3)

            await callback.message.answer(card)

    @staticmethod
    async def find_cookies(callback: types.CallbackQuery):
        await callback.message.answer('Сейчас найдем...')

        get_data('Еда и напитки_Печенье и пирожные')

        with open('result.json', encoding='utf-8') as file:
            data = json.load(file)

        if not data:
            await callback.message.answer('Нет результатов.')

        for index, product in enumerate(data):
            card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                   f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                   f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                   f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

            if index % 20 == 0:
                time.sleep(3)

            await callback.message.answer(card)

    @staticmethod
    async def find_snacks(callback: types.CallbackQuery):
        await callback.message.answer('Сейчас найдем...')

        get_data('Еда и напитки_Снеки')

        with open('result.json', encoding='utf-8') as file:
            data = json.load(file)

        if not data:
            await callback.message.answer('Нет результатов.')

        for index, product in enumerate(data):
            card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                   f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                   f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                   f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

            if index % 20 == 0:
                time.sleep(3)

            await callback.message.answer(card)

    @staticmethod
    async def find_gum(callback: types.CallbackQuery):
        await callback.message.answer('Сейчас найдем...')

        get_data('Еда и напитки_Драже и жевательная резинка')

        with open('result.json', encoding='utf-8') as file:
            data = json.load(file)

        if not data:
            await callback.message.answer('Нет результатов.')

        for index, product in enumerate(data):
            card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                   f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                   f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                   f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

            if index % 20 == 0:
                time.sleep(3)

            await callback.message.answer(card)

    @staticmethod
    async def find_drinks(callback: types.CallbackQuery):
        await callback.message.answer('Сейчас найдем...')

        get_data('Еда и напитки_Напитки')

        with open('result.json', encoding='utf-8') as file:
            data = json.load(file)

        if not data:
            await callback.message.answer('Нет результатов.')

        for index, product in enumerate(data):
            card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                   f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                   f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                   f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

            if index % 20 == 0:
                time.sleep(3)

            await callback.message.answer(card)


class ForMen:
    @staticmethod
    async def show_for_men(callback: types.CallbackQuery):
        await callback.message.answer('Посмотри, что тебе нужно', reply_markup=for_men_kb)

    @staticmethod
    async def find_for_shaving(callback: types.CallbackQuery):
        await callback.message.answer('Сейчас найдем...')

        get_data('Для мужчин_Для бритья')

        with open('result.json', encoding='utf-8') as file:
            data = json.load(file)

        if not data:
            await callback.message.answer('Нет результатов.')

        for index, product in enumerate(data):
            card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                   f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                   f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                   f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

            if index % 20 == 0:
                time.sleep(3)

            await callback.message.answer(card)

    @staticmethod
    async def find_machine_for_shaving(callback: types.CallbackQuery):
        await callback.message.answer('Сейчас найдем...')

        get_data('Для мужчин_Станки')

        with open('result.json', encoding='utf-8') as file:
            data = json.load(file)

        if not data:
            await callback.message.answer('Нет результатов.')

        for index, product in enumerate(data):
            card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                   f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                   f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                   f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

            if index % 20 == 0:
                time.sleep(3)

            await callback.message.answer(card)

    @staticmethod
    async def find_after_shave(callback: types.CallbackQuery):
        await callback.message.answer('Сейчас найдем...')

        get_data('Для мужчин_После бритья')

        with open('result.json', encoding='utf-8') as file:
            data = json.load(file)

        if not data:
            await callback.message.answer('Нет результатов.')

        for index, product in enumerate(data):
            card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                   f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                   f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                   f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

            if index % 20 == 0:
                time.sleep(3)

            await callback.message.answer(card)

    @staticmethod
    async def find_deodorant(callback: types.CallbackQuery):
        await callback.message.answer('Сейчас найдем...')

        get_data('Для мужчин_Дезодоранты')

        with open('result.json', encoding='utf-8') as file:
            data = json.load(file)

        if not data:
            await callback.message.answer('Нет результатов.')

        for index, product in enumerate(data):
            card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                   f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                   f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                   f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

            if index % 20 == 0:
                time.sleep(3)

            await callback.message.answer(card)

    @staticmethod
    async def find_cassettes(callback: types.CallbackQuery):
        await callback.message.answer('Сейчас найдем...')

        get_data('Для мужчин_Сменные кассеты')

        with open('result.json', encoding='utf-8') as file:
            data = json.load(file)

        if not data:
            await callback.message.answer('Нет результатов.')

        for index, product in enumerate(data):
            card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                   f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                   f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                   f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

            if index % 20 == 0:
                time.sleep(3)

            await callback.message.answer(card)

    @staticmethod
    async def find_for_shower(callback: types.CallbackQuery):
        await callback.message.answer('Сейчас найдем...')

        get_data('Для мужчин_Средства для душа')

        with open('result.json', encoding='utf-8') as file:
            data = json.load(file)

        if not data:
            await callback.message.answer('Нет результатов.')

        for index, product in enumerate(data):
            card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                   f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                   f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                   f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

            if index % 20 == 0:
                time.sleep(3)

            await callback.message.answer(card)


class ForKids:
    @staticmethod
    async def show_for_kids(callback: types.CallbackQuery):
        await callback.message.answer('Посмотри, что тебе нужно', reply_markup=for_kids_kb)

    @staticmethod
    async def find_care_means(callback: types.CallbackQuery):
        await callback.message.answer('Сейчас найдем...')

        get_data('Для детей_Средства по уходу')

        with open('result.json', encoding='utf-8') as file:
            data = json.load(file)

        if not data:
            await callback.message.answer('Нет результатов.')

        for index, product in enumerate(data):
            card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                   f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                   f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                   f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

            if index % 20 == 0:
                time.sleep(3)

            await callback.message.answer(card)

    @staticmethod
    async def find_tooth_brush(callback: types.CallbackQuery):
        await callback.message.answer('Сейчас найдем...')

        get_data('Для детей_Зубные щетки')

        with open('result.json', encoding='utf-8') as file:
            data = json.load(file)

        if not data:
            await callback.message.answer('Нет результатов.')

        for index, product in enumerate(data):
            card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                   f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                   f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                   f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

            if index % 20 == 0:
                time.sleep(3)

            await callback.message.answer(card)

    @staticmethod
    async def find_tooth_paste(callback: types.CallbackQuery):
        await callback.message.answer('Сейчас найдем...')

        get_data('Для детей_Зубные пасты')

        with open('result.json', encoding='utf-8') as file:
            data = json.load(file)

        if not data:
            await callback.message.answer('Нет результатов.')

        for index, product in enumerate(data):
            card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                   f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                   f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                   f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

            if index % 20 == 0:
                time.sleep(3)

            await callback.message.answer(card)

    @staticmethod
    async def find_sunscreen(callback: types.CallbackQuery):
        await callback.message.answer('Сейчас найдем...')

        get_data('Для детей_Защита от солнца')

        with open('result.json', encoding='utf-8') as file:
            data = json.load(file)

        if not data:
            await callback.message.answer('Нет результатов.')

        for index, product in enumerate(data):
            card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                   f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                   f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                   f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

            if index % 20 == 0:
                time.sleep(3)

            await callback.message.answer(card)


class ForPets:
    @staticmethod
    async def show_for_pets(callback: types.CallbackQuery):
        await callback.message.answer('Посмотри, что тебе нужно', reply_markup=for_pets_kb)

    @staticmethod
    async def find_care_means(callback: types.CallbackQuery):
        await callback.message.answer('Сейчас найдем...')

        get_data('Для животных_Уход за животными')

        with open('result.json', encoding='utf-8') as file:
            data = json.load(file)

        if not data:
            await callback.message.answer('Нет результатов.')

        for index, product in enumerate(data):
            card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                   f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                   f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                   f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

            if index % 20 == 0:
                time.sleep(3)

            await callback.message.answer(card)

    @staticmethod
    async def find_accessories(callback: types.CallbackQuery):
        await callback.message.answer('Сейчас найдем...')

        get_data('Для животных_Аксессуары и амуниция')

        with open('result.json', encoding='utf-8') as file:
            data = json.load(file)

        if not data:
            await callback.message.answer('Нет результатов.')

        for index, product in enumerate(data):
            card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                   f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                   f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                   f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

            if index % 20 == 0:
                time.sleep(3)

            await callback.message.answer(card)


class GiftsAndPerfumes:
    @staticmethod
    async def show_gifts_and_perfumes(callback: types.CallbackQuery):
        await callback.message.answer('Посмотри, что тебе нужно', reply_markup=gifts_and_perfumes_kb)

    @staticmethod
    async def find_gift_wrap(callback: types.CallbackQuery):
        await callback.message.answer('Сейчас найдем...')

        get_data('Для животных_Подарочная упаковка')

        with open('result.json', encoding='utf-8') as file:
            data = json.load(file)

        if not data:
            await callback.message.answer('Нет результатов.')

        for index, product in enumerate(data):
            card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                   f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                   f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                   f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

            if index % 20 == 0:
                time.sleep(3)

            await callback.message.answer(card)

    @staticmethod
    async def find_magnet_toys(callback: types.CallbackQuery):
        await callback.message.answer('Сейчас найдем...')

        get_data('Магниты игрушки')

        with open('result.json', encoding='utf-8') as file:
            data = json.load(file)

        if not data:
            await callback.message.answer('Нет результатов.')

        for index, product in enumerate(data):
            card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                   f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                   f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                   f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

            if index % 20 == 0:
                time.sleep(3)

            await callback.message.answer(card)

    @staticmethod
    async def find_open_cards(callback: types.CallbackQuery):
        await callback.message.answer('Сейчас найдем...')

        get_data('Открытки')

        with open('result.json', encoding='utf-8') as file:
            data = json.load(file)

        if not data:
            await callback.message.answer('Нет результатов.')

        for index, product in enumerate(data):
            card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                   f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                   f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                   f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

            if index % 20 == 0:
                time.sleep(3)

            await callback.message.answer(card)

    @staticmethod
    async def find_sets_for_women(callback: types.CallbackQuery):
        await callback.message.answer('Сейчас найдем...')

        get_data('Подарки и парфюмерия_Подарочные наборы_Подарочные наборы женские')

        with open('result.json', encoding='utf-8') as file:
            data = json.load(file)

        if not data:
            await callback.message.answer('Нет результатов.')

        for index, product in enumerate(data):
            card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                   f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                   f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                   f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

            if index % 20 == 0:
                time.sleep(3)

            await callback.message.answer(card)

    @staticmethod
    async def find_female(callback: types.CallbackQuery):
        await callback.message.answer('Сейчас найдем...')

        get_data('Подарки и парфюмерия_Парфюмерия_Женская')

        with open('result.json', encoding='utf-8') as file:
            data = json.load(file)

        if not data:
            await callback.message.answer('Нет результатов.')

        for index, product in enumerate(data):
            card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                   f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                   f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                   f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

            if index % 20 == 0:
                time.sleep(3)

            await callback.message.answer(card)

    @staticmethod
    async def find_male(callback: types.CallbackQuery):
        await callback.message.answer('Сейчас найдем...')

        get_data('Подарки и парфюмерия_Парфюмерия_Мужская')

        with open('result.json', encoding='utf-8') as file:
            data = json.load(file)

        if not data:
            await callback.message.answer('Нет результатов.')

        for index, product in enumerate(data):
            card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                   f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                   f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                   f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

            if index % 20 == 0:
                time.sleep(3)

            await callback.message.answer(card)

    @staticmethod
    async def find_unisex(callback: types.CallbackQuery):
        await callback.message.answer('Сейчас найдем...')

        get_data('Подарки и парфюмерия_Парфюмерия_Унисекс')

        with open('result.json', encoding='utf-8') as file:
            data = json.load(file)

        if not data:
            await callback.message.answer('Нет результатов.')

        for index, product in enumerate(data):
            card = f'{hlink(product.get("product_name"), product.get("product_href"))}\n' \
                   f'{hbold("Старая цена: ")}{product.get("old_price")} рублей\n' \
                   f'{hbold("Новая цена: ")}{product.get("current_price")} рублей\n' \
                   f'{hbold("Скидка: ")}{product.get("sale_percent")} %.'

            if index % 20 == 0:
                time.sleep(3)

            await callback.message.answer(card)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_bot, commands='start')
    dp.register_message_handler(show_categories, Text(equals='Давай, подружка'))
    dp.register_callback_query_handler(Care.show_care, text='Уход')
    dp.register_callback_query_handler(Care.show_face, text='Лицо_Уход')
    dp.register_callback_query_handler(Care.Face.find_creams, text='У_Л_Кремы')
    dp.register_callback_query_handler(Care.Face.find_masks, text='У_Л_Маски')
    dp.register_callback_query_handler(Care.Face.find_skin, text='У_Л_Для_кожи')
    dp.register_callback_query_handler(Care.Face.find_wash, text='У_Л_Умывание')
    dp.register_callback_query_handler(Care.Face.find_clear_makeup, text='У_Л_снятие')
    dp.register_callback_query_handler(Care.Face.find_tonics, text='У_Л_Тоники')
    dp.register_callback_query_handler(Care.Face.find_serums, text='У_Л_Скрабы')
    dp.register_callback_query_handler(Care.Face.find_scrubs, text='У_Л_Скрабы')
    dp.register_callback_query_handler(Care.Face.find_skin_around_eyes, text='У_Л_глаз')
    dp.register_callback_query_handler(Care.Face.find_lips, text='У_Л_Губ')
    dp.register_callback_query_handler(Care.show_body, text='Тело_Уход')
    dp.register_callback_query_handler(Care.Body.find_feeding, text='У_Т_Питание')
    dp.register_callback_query_handler(Care.Body.find_shower, text='У_Т_Гели')
    dp.register_callback_query_handler(Care.Body.find_for_hands, text='У_Т_рук')
    dp.register_callback_query_handler(Care.Body.find_scrubs, text='У_Т_Скрабы')
    dp.register_callback_query_handler(Care.Body.find_soap, text='У_Т_Мыло')
    dp.register_callback_query_handler(Care.Body.find_deodorants, text='У_Т_Дезодоранты')
    dp.register_callback_query_handler(Care.Body.find_clear_hair, text='У_Т_Удаление волос')
    dp.register_callback_query_handler(Care.Body.find_sponges, text='У_Т_Мочалки')
    dp.register_callback_query_handler(Care.Body.find_for_legs, text='У_Т_ног')
    dp.register_callback_query_handler(Care.Body.find_bath_salt, text='У_Т_Пена')
    dp.register_callback_query_handler(Care.Body.find_handkerchief, text='У_Т_платки')
    dp.register_callback_query_handler(Care.show_hair, text='Волосы_Уход')
    dp.register_callback_query_handler(Care.Hair.find_shampoo, text='У_В_Шампуни')
    dp.register_callback_query_handler(Care.Hair.find_balsams, text='У_В_Бальзамы')
    dp.register_callback_query_handler(Care.Hair.find_masks, text='У_В_Маски')
    dp.register_callback_query_handler(Care.Hair.find_special_means, text='У_В_средства')
    dp.register_callback_query_handler(Care.Hair.find_styling, text='У_В_укладки')
    dp.register_callback_query_handler(Care.Hair.find_staining, text='У_В_Окрашивание')
    dp.register_callback_query_handler(Care.show_mouth, text='Уход_рот_Ух')
    dp.register_callback_query_handler(Care.Mouth.find_tooth_brush, text='Ух_щетки')
    dp.register_callback_query_handler(Care.Mouth.find_tooth_brush, text='Ух_пасты')
    dp.register_callback_query_handler(Care.Mouth.find_tooth_brush, text='Ух_Ополаскиватели')
    dp.register_callback_query_handler(Care.Mouth.find_tooth_brush, text='Ух_Специальный')
    dp.register_callback_query_handler(Care.show_tan, text='Загар_Уход')
    dp.register_callback_query_handler(Care.Tan.find_sunscreens, text='Загар_Защита')
    dp.register_callback_query_handler(Care.Tan.find_after_tan, text='Загар_После')
    dp.register_callback_query_handler(Care.Tan.find_auto_tan, text='Загар_Автозагар')
    dp.register_callback_query_handler(Care.Tan.find_tan_activation, text='Загар_Активация')
    dp.register_callback_query_handler(Care.show_hygiene, text='Гигиена_Ух')
    dp.register_callback_query_handler(Care.Hygiene.find_gasket, text='У_г_Прокладки')
    dp.register_callback_query_handler(Care.Hygiene.find_tampons, text='У_г_Тампоны')
    dp.register_callback_query_handler(Care.Hygiene.find_intimate_hygiene, text='У_г_интимной')
    dp.register_callback_query_handler(Care.Hygiene.find_cotton_buds_and_disks, text='У_г_Ватные')
    dp.register_callback_query_handler(Care.Hygiene.find_wet_wipes, text='У_г_Влажные')
    dp.register_callback_query_handler(Care.Hygiene.find_sanitizer, text='У_г_Санитайзеры')
    dp.register_callback_query_handler(Care.Hygiene.find_goods_for_health, text='У_г_здоровья')
    dp.register_callback_query_handler(Makeup.show_makeup, text='Макияж')
    dp.register_callback_query_handler(Makeup.show_face, text='Лицо_Макияж')
    dp.register_callback_query_handler(Makeup.Face.find_corrector, text='М_Л_Корректор')
    dp.register_callback_query_handler(Makeup.Face.find_foundation, text='М_Л_Тональные')
    dp.register_callback_query_handler(Makeup.Face.find_powder, text='М_Л_Пудра')
    dp.register_callback_query_handler(Makeup.Face.find_blush, text='М_Л_Румяна')
    dp.register_callback_query_handler(Makeup.Face.find_highlighter, text='М_Л_Хайлайтеры')
    dp.register_callback_query_handler(Makeup.Face.find_circuit, text='М_Л_Контурирование')
    dp.register_callback_query_handler(Makeup.Face.find_other, text='М_Л_Прочее')
    dp.register_callback_query_handler(Makeup.show_eyes, text='Глаза_Макияж')
    dp.register_callback_query_handler(Makeup.Eyes.find_base_for_shadows, text='М_Г_База')
    dp.register_callback_query_handler(Makeup.Eyes.find_pencil, text='М_Г_Карандаши')
    dp.register_callback_query_handler(Makeup.Eyes.find_shadows, text='М_Г_Тени')
    dp.register_callback_query_handler(Makeup.Eyes.find_ink, text='М_Г_Тушь')
    dp.register_callback_query_handler(Makeup.Eyes.find_eyeliners, text='М_Г_Подводки')
    dp.register_callback_query_handler(Makeup.Eyes.find_false_eyelashes, text='М_Г_Накладные')
    dp.register_callback_query_handler(Makeup.show_lips, text='Губы_Макияж')
    dp.register_callback_query_handler(Makeup.Lips.find_sparkles, text='М_Г_Блески')
    dp.register_callback_query_handler(Makeup.Lips.find_pencils, text='М_Г_Карандаши')
    dp.register_callback_query_handler(Makeup.Lips.find_lipstick, text='М_Г_Помада')
    dp.register_callback_query_handler(Makeup.Lips.find_tint, text='М_Г_Тинт')
    dp.register_callback_query_handler(Makeup.Lips.find_other, text='М_Г_Прочее')
    dp.register_callback_query_handler(Makeup.show_nails, text='Ногти_Макияж')
    dp.register_callback_query_handler(Makeup.Nails.find_nail_design, text='М_Н_Дизайн')
    dp.register_callback_query_handler(Makeup.Nails.find_lack_remover, text='М_Н_Средства')
    dp.register_callback_query_handler(Makeup.Nails.find_lack, text='М_Н_Лаки')
    dp.register_callback_query_handler(Makeup.Nails.find_nail_care, text='М_Н_Уход')
    dp.register_callback_query_handler(Makeup.show_brows, text='Брови_Макияж')
    dp.register_callback_query_handler(Makeup.Brows.find_paint_for_brows, text='М_Б_Краска')
    dp.register_callback_query_handler(Makeup.Brows.find_pencil_for_brows, text='М_Б_Карандаш')
    dp.register_callback_query_handler(Makeup.Brows.find_ink_for_brows, text='М_Б_Тушь')
    dp.register_callback_query_handler(Makeup.Brows.find_shadows_for_brows, text='М_Б_Тени')
    dp.register_callback_query_handler(Makeup.Brows.find_set_for_brows, text='М_Б_Набор')
    dp.register_callback_query_handler(Makeup.Brows.find_gel_for_brows, text='М_Б_Гель')
    dp.register_callback_query_handler(Makeup.Brows.find_other, text='М_Б_Прочее')
    dp.register_callback_query_handler(Makeup.show_decorations, text='Украшения_Макияж')
    dp.register_callback_query_handler(Makeup.Decorations.find_applications, text='М_У_Аппликации')
    dp.register_callback_query_handler(Accessories.show_accessories, text='Аксессуары')
    dp.register_callback_query_handler(Accessories.show_makeup_accessories, text='Макияжа_Акс')
    dp.register_callback_query_handler(Accessories.ForMakeUp.find_brushes, text='А_м_Кисти')
    dp.register_callback_query_handler(Accessories.ForMakeUp.find_sponges, text='А_м_Спонжи')
    dp.register_callback_query_handler(Accessories.ForMakeUp.find_applicators, text='А_м_Аппликаторы')
    dp.register_callback_query_handler(Accessories.ForMakeUp.find_tweezers, text='А_м_Пинцеты')
    dp.register_callback_query_handler(Accessories.ForMakeUp.find_other, text='А_м_Прочее')
    dp.register_callback_query_handler(Accessories.show_sub_accessories, text='Аксессуары_Акс')
    dp.register_callback_query_handler(Accessories.SubAccessories.find_other, text='А_А_Прочее')
    dp.register_callback_query_handler(Accessories.SubAccessories.find_business_accessories, text='А_А_Деловые')
    dp.register_callback_query_handler(Accessories.SubAccessories.find_cosmetic_bag, text='А_А_Косметички')
    dp.register_callback_query_handler(Accessories.SubAccessories.find_bag, text='А_А_Сумки')
    dp.register_callback_query_handler(Accessories.show_women_hair, text='ВЖ_Акс')
    dp.register_callback_query_handler(Accessories.WomenHair.find_crabs, text='А_ВЖ_Крабы')
    dp.register_callback_query_handler(Accessories.WomenHair.find_brush, text='А_ВЖ_брашинга')
    dp.register_callback_query_handler(Accessories.WomenHair.find_staining_hair, text='А_ВЖ_Окрашивания')
    dp.register_callback_query_handler(Accessories.WomenHair.find_hair_band, text='А_ВЖ_Ободки')
    dp.register_callback_query_handler(Accessories.WomenHair.find_sets, text='А_ВЖ_Наборы')
    dp.register_callback_query_handler(Accessories.WomenHair.find_hairpin, text='А_ВЖ_Заколки')
    dp.register_callback_query_handler(Accessories.WomenHair.find_scrunchy, text='А_ВЖ_Резинки')
    dp.register_callback_query_handler(Accessories.WomenHair.find_hair_comb, text='А_ВЖ_Расчески')
    dp.register_callback_query_handler(Accessories.WomenHair.find_curlers, text='А_ВЖ_Бигуди')
    dp.register_callback_query_handler(Accessories.WomenHair.find_other, text='А_ВЖ_Прочее')
    dp.register_callback_query_handler(Accessories.show_kids_hair, text='ВД_Акс')
    dp.register_callback_query_handler(Accessories.KidsHair.find_crabs, text='А_ВД_Крабы')
    dp.register_callback_query_handler(Accessories.KidsHair.find_hair_band, text='А_ВД_Ободки')
    dp.register_callback_query_handler(Accessories.KidsHair.find_sets, text='А_ВД_Наборы')
    dp.register_callback_query_handler(Accessories.KidsHair.find_hairpin, text='А_ВД_Заколки')
    dp.register_callback_query_handler(Accessories.KidsHair.find_scrunchy, text='А_ВД_Резинки')
    dp.register_callback_query_handler(Accessories.KidsHair.find_other, text='А_ВД_Прочее')
    dp.register_callback_query_handler(Accessories.show_tights, text='Белье_Акс')
    dp.register_callback_query_handler(Accessories.Tights.find_tights, text='А_Б_Колготки')
    dp.register_callback_query_handler(Accessories.Tights.find_stockings, text='А_Б_Чулки')
    dp.register_callback_query_handler(Accessories.Tights.find_socks, text='А_Б_Носки')
    dp.register_callback_query_handler(Accessories.Tights.find_knee_socks, text='А_Б_Гольфы')
    dp.register_callback_query_handler(Accessories.Tights.find_underwear, text='А_Б_Белье')
    dp.register_callback_query_handler(Accessories.show_bijouterie, text='Бижутерия_Акс')
    dp.register_callback_query_handler(Accessories.Bijouterie.find_neck_decoration, text='А_Бж_шею')
    dp.register_callback_query_handler(Accessories.Bijouterie.find_earrings, text='А_Бж_Серьги')
    dp.register_callback_query_handler(Accessories.Bijouterie.find_trinket, text='А_Бж_Брелоки')
    dp.register_callback_query_handler(Accessories.Bijouterie.find_for_kids, text='А_Бж_Для детей')
    dp.register_callback_query_handler(Accessories.Bijouterie.find_rings, text='А_Бж_Кольца')
    dp.register_callback_query_handler(Accessories.Bijouterie.find_bracer, text='А_Бж_Браслеты')
    dp.register_callback_query_handler(Accessories.Bijouterie.find_brooch, text='А_Бж_Броши')
    dp.register_callback_query_handler(Accessories.Bijouterie.find_other, text='А_Бж_Прочее')
    dp.register_callback_query_handler(HomeStuff.show_home_stuff, text='Для дома')
    dp.register_callback_query_handler(HomeStuff.show_chemicals, text='БХ_Для дома')
    dp.register_callback_query_handler(HomeStuff.Chemical.find_air_fresher, text='БХ_Освежители')
    dp.register_callback_query_handler(HomeStuff.Chemical.find_for_bath, text='БХ_ванных')
    dp.register_callback_query_handler(HomeStuff.Chemical.find_for_wash, text='БХ_стирки')
    dp.register_callback_query_handler(HomeStuff.Chemical.find_for_insects, text='БХ_насекомых')
    dp.register_callback_query_handler(HomeStuff.Chemical.find_clothes_care, text='БХ_одеждой')
    dp.register_callback_query_handler(HomeStuff.Chemical.find_shoes_care, text='БХ_обувью')
    dp.register_callback_query_handler(HomeStuff.Chemical.find_fro_kitchen, text='БХ_кухни')
    dp.register_callback_query_handler(HomeStuff.Chemical.find_for_rooms, text='БХ_комнат')
    dp.register_callback_query_handler(HomeStuff.show_paper_stuff, text='БП_Для дома')
    dp.register_callback_query_handler(HomeStuff.PaperProduct.find_toilet_paper, text='БП_Туалетная')
    dp.register_callback_query_handler(HomeStuff.PaperProduct.find_napkins, text='БП_Салфетки')
    dp.register_callback_query_handler(FoodAndDrinks.show_food_and_drinks, text='Еда и напитки')
    dp.register_callback_query_handler(FoodAndDrinks.find_bar, text='ЕН_Батончики')
    dp.register_callback_query_handler(FoodAndDrinks.find_cookies, text='ЕН_Печенье')
    dp.register_callback_query_handler(FoodAndDrinks.find_snacks, text='ЕН_Снеки')
    dp.register_callback_query_handler(FoodAndDrinks.find_gum, text='ЕН_Драже')
    dp.register_callback_query_handler(FoodAndDrinks.find_drinks, text='ЕН_Напитки')
    dp.register_callback_query_handler(ForMen.show_for_men, text='Для мужчин')
    dp.register_callback_query_handler(ForMen.find_for_shaving, text='ДМ_бритья')
    dp.register_callback_query_handler(ForMen.find_machine_for_shaving, text='ДМ_Станки')
    dp.register_callback_query_handler(ForMen.find_after_shave, text='ДМ_После')
    dp.register_callback_query_handler(ForMen.find_deodorant, text='ДМ_Дезодоранты')
    dp.register_callback_query_handler(ForMen.find_cassettes, text='ДМ_Сменные')
    dp.register_callback_query_handler(ForMen.find_for_shower, text='ДМ_Средства')
    dp.register_callback_query_handler(ForKids.show_for_kids, text='Для детей')
    dp.register_callback_query_handler(ForKids.find_care_means, text='ДД_Средства')
    dp.register_callback_query_handler(ForKids.find_tooth_brush, text='ДД_щетки')
    dp.register_callback_query_handler(ForKids.find_tooth_paste, text='ДД_пасты')
    dp.register_callback_query_handler(ForKids.find_sunscreen, text='ДД_Защита')
    dp.register_callback_query_handler(ForPets.show_for_pets, text='Для животных')
    dp.register_callback_query_handler(ForPets.find_care_means, text='ДЖ_Уход')
    dp.register_callback_query_handler(ForPets.find_accessories, text='ДЖ_Акс')
    dp.register_callback_query_handler(GiftsAndPerfumes.show_gifts_and_perfumes, text='Подарки и парфюмерия')
    dp.register_callback_query_handler(GiftsAndPerfumes.find_sets_for_women, text='ПП_женские')
    dp.register_callback_query_handler(GiftsAndPerfumes.find_female, text='ПП_Парф_Женская')
    dp.register_callback_query_handler(GiftsAndPerfumes.find_male, text='ПП_Парф_Мужская')
    dp.register_callback_query_handler(GiftsAndPerfumes.find_unisex, text='ПП_Парф_Унисекс')
