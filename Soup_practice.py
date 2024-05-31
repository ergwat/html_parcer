from bs4 import BeautifulSoup
import requests
from googletrans import Translator

''' 
#===============================вытаскиваем просто все ссылки:

url = "http://quotes.toscrape.com/"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

links = soup.find_all("a")
for link in links:
    print(link.get('href'))
#===============================
'''

'''
#===============================достаём цитаты и авторов по тегам и классам:

url = "http://quotes.toscrape.com/"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

texts = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")
for i in range(len(texts)):
    print(f"Цитата №{i+1}: {texts[i].text}\nАвтор: {authors[i].text}\n")

#===============================
'''

#=============================== функция для поучения случайного слова с сайта
def get_english_word():
   url = "https://randomword.com/"
   try:
       response = requests.get(url)
       soup = BeautifulSoup(response.content, "html.parser")
       english_words = soup.find("div", id="random_word").text.strip()
       word_definition = soup.find("div", id="random_word_definition").text.strip()
       # Чтобы программа возвращала словарь
       return {
           "english_words": english_words,
           "word_definition": word_definition
       }
   except:
        print("Что-то пошло не так")


#=============================== функция самой игры "угадай слово"
def word_game():
    print("Добро пожаловать в игру")
    while True:
        # Создаём функцию, чтобы использовать результат функции-словаря
        word_dict = get_english_word()
        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        # Начинаем игру
        translator = Translator()
        definition_translation = translator.translate(word_definition, src="en", dest="ru")
        word_translation = translator.translate(word, src="en", dest="ru")
        print(f"Значение слова - {definition_translation.text}")
        user = input("Что это за слово? ")
        if user == word_translation:
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {word_translation.text}")

        # Создаём возможность закончить игру
        play_again = input("Хотите сыграть еще раз? д/н  ")
        if play_again != "д":
            print("Спасибо за игру!")
            break

#=============================== вызываем функцию старта игры
word_game()

'''
translator = Translator()
translation = translator.translate("Hello", src="en", dest="ru")
print(translation.text)
'''