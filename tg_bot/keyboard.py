from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton('Давай, подружка'))

top_inline_kb = InlineKeyboardMarkup(row_width=1).add(
    *[InlineKeyboardButton(text='Уход', callback_data='Уход'),
      InlineKeyboardButton(text='Макияж', callback_data='Макияж'),
      InlineKeyboardButton(text='Аксессуары', callback_data='Аксессуары'),
      InlineKeyboardButton(text='Для дома', callback_data='Для дома'),
      InlineKeyboardButton(text='Еда и напитки', callback_data='Еда и напитки'),
      InlineKeyboardButton(text='Для мужчин', callback_data='Для мужчин'),
      InlineKeyboardButton(text='Для детей', callback_data='Для детей'),
      InlineKeyboardButton(text='Для животных', callback_data='Для животных'),
      InlineKeyboardButton(text='Подарки и парфюмерия', callback_data='Подарки и парфюмерия')])

care_kb = InlineKeyboardMarkup(row_width=2).add(
    *[InlineKeyboardButton(text='Лицо', callback_data='Лицо_Уход'),
      InlineKeyboardButton(text='Тело', callback_data='Тело_Уход'),
      InlineKeyboardButton(text='Волосы', callback_data='Волосы_Уход'),
      InlineKeyboardButton(text='Уход за полостью рта', callback_data='Уход_рот_Ух'),
      InlineKeyboardButton(text='Загар', callback_data='Загар_Уход'),
      InlineKeyboardButton(text='Личная гигиена', callback_data='Гигиена_Ух')])

face_care_kb = InlineKeyboardMarkup(row_width=2).add(
    *[InlineKeyboardButton(text='Кремы', callback_data='У_Л_Кремы'),
      InlineKeyboardButton(text='Маски', callback_data='У_Л_Маски'),
      InlineKeyboardButton(text='Для проблемной кожи', callback_data='У_Л_Для_кожи'),
      InlineKeyboardButton(text='Умывание', callback_data='У_Л_Умывание'),
      InlineKeyboardButton(text='Для снятия макияжа', callback_data='У_Л_снятие'),
      InlineKeyboardButton(text='Тоники и лосьоны', callback_data='У_Л_Тоники'),
      InlineKeyboardButton(text='Сыворотки', callback_data='У_Л_Сыворотки'),
      InlineKeyboardButton(text='Скрабы и пилинги', callback_data='У_Л_Скрабы'),
      InlineKeyboardButton(text='Для кожи вокруг глаз', callback_data='У_Л_глаз'),
      InlineKeyboardButton(text='Для губ', callback_data='У_Л_Губ')])

body_care_kb = InlineKeyboardMarkup(row_width=2).add(
    *[InlineKeyboardButton(text='Питание и увлажнение', callback_data='У_Т_Питание'),
      InlineKeyboardButton(text='Гели и кремы для душа', callback_data='У_Т_Гели'),
      InlineKeyboardButton(text='Для рук', callback_data='У_Т_рук'),
      InlineKeyboardButton(text='Скрабы и пилинги', callback_data='У_Т_Скрабы'),
      InlineKeyboardButton(text='Мыло', callback_data='У_Т_Мыло'),
      InlineKeyboardButton(text='Дезодоранты', callback_data='У_Т_Дезодоранты'),
      InlineKeyboardButton(text='Удаление волос', callback_data='У_Т_Удаление'),
      InlineKeyboardButton(text='Мочалки и губки', callback_data='У_Т_Мочалки'),
      InlineKeyboardButton(text='Для ног', callback_data='У_Т_ног'),
      InlineKeyboardButton(text='Пена соль масла для ванны', callback_data='У_Т_Пена'),
      InlineKeyboardButton(text='Носовые платки', callback_data='У_Т_платки')])

hair_care_kb = InlineKeyboardMarkup(row_width=2).add(
    *[InlineKeyboardButton(text='Шампуни', callback_data='У_В_Шампуни'),
      InlineKeyboardButton(text='Бальзамы и ополаскиватели', callback_data='У_В_Бальзамы'),
      InlineKeyboardButton(text='Маски', callback_data='У_В_Маски'),
      InlineKeyboardButton(text='Специальные средства', callback_data='У_В_средства'),
      InlineKeyboardButton(text='Средства для укладки', callback_data='У_В_укладки'),
      InlineKeyboardButton(text='Окрашивание', callback_data='У_В_Окрашивание')])

mouth_care_kb = InlineKeyboardMarkup(row_width=1).add(
    *[InlineKeyboardButton(text='Зубные щетки', callback_data='Ух_щетки'),
      InlineKeyboardButton(text='Зубные пасты', callback_data='Ух_пасты'),
      InlineKeyboardButton(text='Ополаскиватели', callback_data='Ух_Ополаскиватели'),
      InlineKeyboardButton(text='Специальный уход', callback_data='Ух_Специальный')])

tan_care_kb = InlineKeyboardMarkup(row_width=2).add(
    *[InlineKeyboardButton(text='Защита от солнца', callback_data='Загар_Защита'),
      InlineKeyboardButton(text='После загара', callback_data='Загар_После'),
      InlineKeyboardButton(text='Автозагар', callback_data='Загар_Автозагар'),
      InlineKeyboardButton(text='Активация загара', callback_data='Загар_Активация')])

hygiene_care_kb = InlineKeyboardMarkup(row_width=2).add(
    *[InlineKeyboardButton(text='Прокладки', callback_data='У_г_Прокладки'),
      InlineKeyboardButton(text='Тампоны', callback_data='У_г_Тампоны'),
      InlineKeyboardButton(text='Средства для интимной гигиены', callback_data='У_г_интимной'),
      InlineKeyboardButton(text='Ватные палочки и диски', callback_data='У_г_Ватные'),
      InlineKeyboardButton(text='Влажные салфетки', callback_data='У_г_Влажные'),
      InlineKeyboardButton(text='Санитайзеры', callback_data='У_г_Санитайзеры'),
      InlineKeyboardButton(text='Товары для здоровья', callback_data='У_г_здоровья')])


makeup_kb = InlineKeyboardMarkup(row_width=2).add(
    *[InlineKeyboardButton(text='Лицо', callback_data='Лицо_Макияж'),
      InlineKeyboardButton(text='Глаза', callback_data='Глаза_Макияж'),
      InlineKeyboardButton(text='Губы', callback_data='Губы_Макияж'),
      InlineKeyboardButton(text='Ногти', callback_data='Ногти_Макияж'),
      InlineKeyboardButton(text='Брови', callback_data='Брови_Макияж'),
      InlineKeyboardButton(text='Украшения для тела и волос', callback_data='Украшения_Макияж')])

face_makeup_kb = InlineKeyboardMarkup(row_width=2).add(
    *[InlineKeyboardButton(text='Корректор', callback_data='М_Л_Корректор'),
      InlineKeyboardButton(text='Тональные средства', callback_data='М_Л_Тональные'),
      InlineKeyboardButton(text='Пудра', callback_data='М_Л_Пудра'),
      InlineKeyboardButton(text='Румяна', callback_data='М_Л_Румяна'),
      InlineKeyboardButton(text='Хайлайтеры', callback_data='М_Л_Хайлайтеры'),
      InlineKeyboardButton(text='Контурирование', callback_data='М_Л_Контурирование'),
      InlineKeyboardButton(text='Прочее', callback_data='М_Л_Прочее')])

eyes_makeup_kb = InlineKeyboardMarkup(row_width=2).add(
    *[InlineKeyboardButton(text='База под тени', callback_data='М_Г_База'),
      InlineKeyboardButton(text='Карандаши', callback_data='М_Г_Карандаши'),
      InlineKeyboardButton(text='Тени', callback_data='М_Г_Тени'),
      InlineKeyboardButton(text='Тушь', callback_data='М_Г_Тушь'),
      InlineKeyboardButton(text='Подводки', callback_data='М_Г_Подводки'),
      InlineKeyboardButton(text='Накладные ресницы', callback_data='М_Г_Накладные')])

lips_makeup_kb = InlineKeyboardMarkup(row_width=2).add(
    *[InlineKeyboardButton(text='Блески', callback_data='М_Г_Блески'),
      InlineKeyboardButton(text='Карандаши', callback_data='М_Г_Карандаши'),
      InlineKeyboardButton(text='Помада', callback_data='М_Г_Помада'),
      InlineKeyboardButton(text='Тинт', callback_data='М_Г_Тинт'),
      InlineKeyboardButton(text='Прочее', callback_data='М_Г_Прочее')])

nails_makeup_kb = InlineKeyboardMarkup(row_width=1).add(
    *[InlineKeyboardButton(text='Дизайн ногтей', callback_data='М_Н_Дизайн'),
      InlineKeyboardButton(text='Средства для снятия лака', callback_data='М_Н_Средства'),
      InlineKeyboardButton(text='Лаки', callback_data='М_Н_Лаки'),
      InlineKeyboardButton(text='Уход за ногтями', callback_data='М_Н_Уход')])

brows_makeup_kb = InlineKeyboardMarkup(row_width=2).add(
    *[InlineKeyboardButton(text='Краска для ресниц и бровей', callback_data='М_Б_Краска'),
      InlineKeyboardButton(text='Карандаш для бровей', callback_data='М_Б_Карандаш'),
      InlineKeyboardButton(text='Тушь для бровей', callback_data='М_Б_Тушь'),
      InlineKeyboardButton(text='Тени для бровей', callback_data='М_Б_Тени'),
      InlineKeyboardButton(text='Набор для бровей', callback_data='М_Б_Набор'),
      InlineKeyboardButton(text='Гель для бровей', callback_data='М_Б_Гель'),
      InlineKeyboardButton(text='Прочее', callback_data='М_Б_Прочее')])

decorations_makeup_kb = InlineKeyboardMarkup(row_width=1).add(
      InlineKeyboardButton(text='Аппликации на тело тату',
                           callback_data='М_У_Аппликации'))

accessories_kb = InlineKeyboardMarkup(row_width=2).add(
    *[InlineKeyboardButton(text='Для макияжа', callback_data='Макияжа_Акс'),
      InlineKeyboardButton(text='Аксессуары', callback_data='Аксессуары_Акс'),
      InlineKeyboardButton(text='Для волос женские', callback_data='ВЖ_Акс'),
      InlineKeyboardButton(text='Для волос детские', callback_data='ВД_Акс'),
      InlineKeyboardButton(text='Белье и колготки', callback_data='Белье_Акс'),
      InlineKeyboardButton(text='Бижутерия', callback_data='Бижутерия_Акс')])

for_makeup_accessories_kb = InlineKeyboardMarkup(row_width=2).add(
    *[InlineKeyboardButton(text='Кисти', callback_data='А_м_Кисти'),
      InlineKeyboardButton(text='Спонжи', callback_data='А_м_Спонжи'),
      InlineKeyboardButton(text='Аппликаторы', callback_data='А_м_Аппликаторы'),
      InlineKeyboardButton(text='Пинцеты', callback_data='А_м_Пинцеты'),
      InlineKeyboardButton(text='Прочее', callback_data='А_м_Прочее')])

accessories_accessories_kb = InlineKeyboardMarkup(row_width=1).add(
    *[InlineKeyboardButton(text='Прочее', callback_data='А_А_Прочее'),
      InlineKeyboardButton(text='Деловые аксессуары', callback_data='А_А_Деловые'),
      InlineKeyboardButton(text='Косметички', callback_data='А_А_Косметички'),
      InlineKeyboardButton(text='Сумки', callback_data='А_А_Сумки')])

for_hair_women_accessories_kb = InlineKeyboardMarkup(row_width=2).add(
    *[InlineKeyboardButton(text='Крабы', callback_data='А_ВЖ_Крабы'),
      InlineKeyboardButton(text='Щетки для брашинга', callback_data='А_ВЖ_брашинга'),
      InlineKeyboardButton(text='Для окрашивания волос', callback_data='А_ВЖ_Окрашивания'),
      InlineKeyboardButton(text='Ободки', callback_data='А_ВЖ_Ободки'),
      InlineKeyboardButton(text='Наборы', callback_data='А_ВЖ_Наборы'),
      InlineKeyboardButton(text='Заколки', callback_data='А_ВЖ_Заколки'),
      InlineKeyboardButton(text='Резинки', callback_data='А_ВЖ_Резинки'),
      InlineKeyboardButton(text='Расчески', callback_data='А_ВЖ_Расчески'),
      InlineKeyboardButton(text='Бигуди', callback_data='А_ВЖ_Бигуди'),
      InlineKeyboardButton(text='Прочее', callback_data='А_ВЖ_Прочее')])

for_hair_kids_accessories_kb = InlineKeyboardMarkup(row_width=2).add(
    *[InlineKeyboardButton(text='Крабы', callback_data='А_ВД_Крабы'),
      InlineKeyboardButton(text='Ободки', callback_data='А_ВД_Ободки'),
      InlineKeyboardButton(text='Наборы', callback_data='А_ВД_Наборы'),
      InlineKeyboardButton(text='Заколки', callback_data='А_ВД_Заколки'),
      InlineKeyboardButton(text='Резинки', callback_data='А_ВД_Резинки'),
      InlineKeyboardButton(text='Прочее', callback_data='А_ВД_Прочее')])

tights_accessories_kb = InlineKeyboardMarkup(row_width=2).add(
    *[InlineKeyboardButton(text='Колготки', callback_data='А_Б_Колготки'),
      InlineKeyboardButton(text='Чулки', callback_data='А_Б_Чулки'),
      InlineKeyboardButton(text='Носки', callback_data='А_Б_Носки'),
      InlineKeyboardButton(text='Гольфы', callback_data='А_Б_Гольфы'),
      InlineKeyboardButton(text='Белье', callback_data='А_Б_Белье')])

bijouterie_accessories_kb = InlineKeyboardMarkup(row_width=2).add(
    *[InlineKeyboardButton(text='Украшения на шею', callback_data='А_Бж_шею'),
      InlineKeyboardButton(text='Серьги', callback_data='А_Бж_Серьги'),
      InlineKeyboardButton(text='Брелоки', callback_data='А_Бж_Брелоки'),
      InlineKeyboardButton(text='Для детей', callback_data='А_Бж_Для детей'),
      InlineKeyboardButton(text='Кольца', callback_data='А_Бж_Кольца'),
      InlineKeyboardButton(text='Браслеты', callback_data='А_Бж_Браслеты'),
      InlineKeyboardButton(text='Броши', callback_data='А_Бж_Броши'),
      InlineKeyboardButton(text='Прочее', callback_data='А_Бж_Прочее')])

home_stuff_kb = InlineKeyboardMarkup(row_width=1).add(
    *[InlineKeyboardButton(text='Бытовая химия', callback_data='БХ_Для дома'),
      InlineKeyboardButton(text='Бумажная продукция', callback_data='БП_Для дома')])

chemical_home_stuff_kb = InlineKeyboardMarkup(row_width=2).add(
    *[InlineKeyboardButton(text='Освежители воздуха', callback_data='БХ_Освежители'),
      InlineKeyboardButton(text='Для ванных и туалетов', callback_data='БХ_ванных'),
      InlineKeyboardButton(text='Для стирки', callback_data='БХ_стирки'),
      InlineKeyboardButton(text='Средства от насекомых', callback_data='БХ_насекомых'),
      InlineKeyboardButton(text='Для ухода за одеждой', callback_data='БХ_одеждой'),
      InlineKeyboardButton(text='Для ухода за обувью', callback_data='БХ_обувью'),
      InlineKeyboardButton(text='Для кухни', callback_data='БХ_кухни'),
      InlineKeyboardButton(text='Для комнат', callback_data='БХ_комнат')])

paper_product_home_stuff_kb = InlineKeyboardMarkup(row_width=1).add(
    *[InlineKeyboardButton(text='Туалетная бумага', callback_data='БП_Туалетная'),
      InlineKeyboardButton(text='Салфетки и полотенца', callback_data='БП_Салфетки')])


food_and_drinks = InlineKeyboardMarkup(row_width=1).add(
    *[InlineKeyboardButton(text='Батончики', callback_data='ЕН_Батончики'),
      InlineKeyboardButton(text='Печенье и пирожные', callback_data='ЕН_Печенье'),
      InlineKeyboardButton(text='Снеки', callback_data='ЕН_Снеки'),
      InlineKeyboardButton(text='Драже и жевательная резинка', callback_data='ЕН_Драже'),
      InlineKeyboardButton(text='Напитки', callback_data='ЕН_Напитки')])

for_men_kb = InlineKeyboardMarkup(row_width=2).add(
    *[InlineKeyboardButton(text='Для бритья', callback_data='ДМ_бритья'),
      InlineKeyboardButton(text='Станки', callback_data='ДМ_Станки'),
      InlineKeyboardButton(text='После бритья', callback_data='ДМ_После'),
      InlineKeyboardButton(text='Дезодоранты', callback_data='ДМ_Дезодоранты'),
      InlineKeyboardButton(text='Сменные кассеты', callback_data='ДМ_Сменные'),
      InlineKeyboardButton(text='Средства для душа', callback_data='ДМ_Средства')])

for_kids_kb = InlineKeyboardMarkup(row_width=1).add(
    *[InlineKeyboardButton(text='Средства по уходу', callback_data='ДД_Средства'),
      InlineKeyboardButton(text='Зубные щетки', callback_data='ДД_щетки'),
      InlineKeyboardButton(text='Зубные пасты', callback_data='ДД_пасты'),
      InlineKeyboardButton(text='Защита от солнца', callback_data='ДД_Защита')])

for_pets_kb = InlineKeyboardMarkup(row_width=1).add(
    *[InlineKeyboardButton(text='Уход за животными', callback_data='ДЖ_Уход'),
      InlineKeyboardButton(text='Аксессуары и амуниция', callback_data='ДЖ_Акс')])

gifts_and_perfumes_kb = InlineKeyboardMarkup(row_width=2).add(
    *[InlineKeyboardButton(text='Подарочные наборы женские', callback_data='ПП_женские'),
      InlineKeyboardButton(text='Женская', callback_data='ПП_Парф_Женская'),
      InlineKeyboardButton(text='Мужская', callback_data='ПП_Парф_Мужская'),
      InlineKeyboardButton(text='Унисекс', callback_data='ПП_Парф_Унисекс')])
