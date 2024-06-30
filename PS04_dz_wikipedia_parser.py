from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import random


'''def ask_topic():
    topic = input("Введите название статьи на Википедии:\n")
    browser.get(f"https://ru.wikipedia.org/wiki/{topic}")
    return topic
'''


def get_paragraphs(browser):
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    #Для перебора пишем цикл
    for paragraph in paragraphs:
        print(paragraph.text)
        input()


def random_article(browser):
    hatnotes = []
    for element in browser.find_elements(By.TAG_NAME, "div"):
    # Чтобы искать атрибут класса
        cl = element.get_attribute("class")
        if cl == "hatnote navigation-not-searchable":
            hatnotes.append(element)

    if hatnotes != []:
        hatnote = random.choice(hatnotes)
        link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
        print(link)
        browser.get(link)
        browse(browser, topic)
    else:
        print("В этой статье нет связанных ссылок, придётся читать...")
        browse(browser, topic)
    # Для получения ссылки мы должны найти на сайте тег "a" внутри тега "div"



def browse(browser, topic):
    #browser.get(f"https://ru.wikipedia.org/wiki/{topic}")
    print(f"Название этой статьи - {browser.title}")
    choice = input("Выберите дальнейшие действия:\nХотите читать статью по одному параграфу? Нажмите 1\nХотите перейти в связанную статью? Нажмите 2\nХотите выйти из программы? нажмите любую другую клавишу\n")
    if choice == "1":
        get_paragraphs(browser)
    elif choice == "2":
        random_article(browser)
    else:
        browser.close()
        exit()

#topic=ask_topic()
topic = input("Введите название статьи на Википедии:\n")
browser = webdriver.Firefox()
browser.get(f"https://ru.wikipedia.org/wiki/{topic}")
browse(browser, topic)





#assert f"{topic} — Википедия" in browser.title, "Wikipedia не открылся"
#time.sleep(2)
#searchbox = browser.find_element(By.NAME, "search")
#searchbox.send_keys(topic)
#searchbox.send_keys(Keys.RETURN)
#time.sleep(10)
#browser.quit()