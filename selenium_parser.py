from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox()
browser.get("https://wordstat.yandex.ru/")
assert "Вордстат" in browser.title, "Вордстат не открылся"
time.sleep(5)
searchbox = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div[2]/span/input")
searchbox.send_keys("MVI")
searchbox.send_keys(Keys.ENTER)
time.sleep(10)
browser.quit()
