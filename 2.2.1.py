import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    
    sum = int(browser.find_element(By.CSS_SELECTOR, 'h2>span.nowrap#num1').text) + int(browser.find_element(By.CSS_SELECTOR, 'h2>span.nowrap#num2').text)
    # print(sum)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_visible_text(str(sum)) # ищем элемент с текстом "Python"


    # # Отправляем заполненную форму
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()