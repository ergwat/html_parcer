import requests
from bs4 import BeautifulSoup
import re

def remove_non_digits(text): # удаляет из строки всё, кроме цифр
    return re.sub(r'\D', '', text)

def get_prices(url):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    names = soup.find_all("a", class_="name")
    prices = soup.find_all("a", class_="price")
    for i in range(len(names)):
        if names[i].text:
            print(f"Товар №{i+1}: {names[i].text.strip()}\nЦена: {remove_non_digits(prices[i].text)}\n")

def get_urls(url):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a", class_="catalog-section-list-link")
    full_links = []
    for link in links:
        full_link = "https://mvi-rus.ru" + str(link.get('href'))
        full_links.append(full_link)
        #print(full_link)
    return full_links


url = "https://mvi-rus.ru/catalog/krany-mvi/"

for i in get_urls(url):
    get_prices(i)
