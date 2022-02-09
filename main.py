import telebot
import time
from bs4 import BeautifulSoup as BS
from selenium import webdriver

token = '1751383993:AAFQDKPAYHq_dbeHOtRAH3pEjCo6CD84vuQ'

# Создаем экземпляр бота
bot = telebot.TeleBot(token)

driver = webdriver.Chrome('chromedriver') 
driver.get("https://e-learning.bmstu.ru/kaluga/login/index.php")

login = "shza21ki274"
password = "n68sxfui"
data = []
# status = ""

def printArray(array):
    for i in range(len(array)):
        print(array[i], end = " ")
        print('\n')

def getwiki(s):
    driver.find_elements_by_css_selector('a.btn-secondary')[0].click()
    driver.find_element_by_id('username').send_keys(login)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_elements_by_css_selector('input.btn')[0].click()
    return 'Авторизация прошла успешно'
def getdata(s):
    driver.find_elements_by_css_selector('div.popover-region-toggle')[0].click()
    time.sleep(3)
    soup = BS(driver.page_source, 'lxml')
    # orgs = soup.find_all('div', class_='content-item-container')
    # for org in orgs:
    #     name = org.find('a', class_='context-link').text.strip()
    #     data.append([name])
    # printArray(data)
    # return len(data)
    data_str = str(soup.find('div', class_='count-container').text)
    return "Новых уведомлений на сайте: " + data_str
    
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(message, res=False):
    bot.send_message(message.chat.id, 'Салам алейкум, братик, представься')
    get_message_bot = message.text.strip().lower()
    if get_message_bot != "zakhar":
        bot.polling(none_stop=False, interval=0)
    else:
        bot.polling(none_stop=True, interval=0)
        bot.send_message(message.chat.id, 'Заходи родной')
# Получение сообщений от юзера
@bot.message_handler(commands=['auth'])
def handle_text(message):
    if password != "" and login != "":
        bot.send_message(message.chat.id, getwiki(message.text))
        bot.send_message(message.chat.id, 'Чтобы выгрузить данные, нажми /gg')
    else:
        bot.send_message(message.chat.id, "Сначала введи логин и пароль с помощью команд /pass и /log")
@bot.message_handler(commands=['gg'])
def handle_text(message):
    bot.send_message(message.chat.id, "Ожидай 5 секунд, я выгружаю данные")
    bot.send_message(message.chat.id, getdata(message.text))
# @bot.message_handler(commands=['log'])
# def handle_text(message):
#     global status
#     bot.send_message(message.chat.id, "введи логин")
#     status = "log"
# @bot.message_handler(commands=['pass'])
# def handle_text(message):
#     global status
#     bot.send_message(message.chat.id, "введи пароль")
#     status = "pass"
# @bot.message_handler(content_types=['text'])
# def handle_text(message):
#     global login
#     global password
#     if status == "log":
#         login = message.text
#         status == ""
#     elif status == "pass":
#         password = message.text
#         status == ""
#     else:
#         bot.send_message(message.chat.id, "Сначала введи логин и пароль с помощью команд /pass и /log")
bot.polling(none_stop=True, interval=0)