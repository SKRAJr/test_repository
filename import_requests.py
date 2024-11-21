import requests
import time

API_URL = 'https://api.telegram.org/bot'
API_CATS_URL = 'https://api.thecatapi.com/v1/images/search'
BOT_TOKEN = '8092597380:AAGH1CcVFGYbvzFOnvhSlNHbfkeMvSiWQiw'
TEXT = 'Принял, понял, обработал\nПока ничего не умею, держи кота!'
ERROR_TEXT = 'Бля, а где кот? :('
MAX_COUNTER = 100

offset = -2     # Установка картеки на предпоследнее обновление в боте
counter = 0
chat_id: int
cat_response: requests.Response
cat_link: str

while counter < MAX_COUNTER:

    print('attemp =', counter) #Для отслеживания рабочего состояния бота

    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json() # Проверяем наличие обновлений в боте

    if updates['result']:                       # Если изменения есть
        for result in updates['result']:        # В словаре итерируем вложенный словарь с ключем 'result'
            offset = result['update_id']        # Устанавливаем нидентификатор обновления, с которым будем работать
            chat_id = result['message']['from']['id']   # Сохраняем идентификатор чата, для ответного запроса в этот чат
            requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')     # Отвечаем текстовым сообщением на любое изменение в чате
            cat_response = requests.get(API_CATS_URL)   # Присваиваем ссылку в переменную
            if cat_response.status_code == 200:         # Если запрос по ссылке прошел удачно
                cat_link = cat_response.json()[0]['url']    # Присваиваем ссылку на рандомную картинку
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')  # Отправляем фото в чат пользователя
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}') # Иначе отправляем сообщение с текстом об ошибке


    time.sleep(1)
    counter += 1


response = requests.get(f'{API_URL}{BOT_TOKEN}/getMe')