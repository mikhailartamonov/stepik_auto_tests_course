import time
import math
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(formula,x):
  return eval(formula)

ln = math.log
sin = math.sin

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    
    browser.find_element(By.NAME, 'firstname').send_keys("FN")
    browser.find_element(By.NAME, 'lastname').send_keys("LN")
    browser.find_element(By.NAME, 'email').send_keys("em@i.l")
 
    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'temp.txt') 
    browser.find_element(By.NAME, 'file').send_keys(file_path)

    # Отправляем заполненную форму
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()
    


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()