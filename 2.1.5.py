import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(formula,x):
  return eval(formula)

ln = math.log
sin = math.sin

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    # link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    
    formula_element = browser.find_element(By.CSS_SELECTOR, 'div.form-group span.nowrap:nth-child(1)')
    formula = formula_element.text
    formula = formula[formula.find('is')+3:-formula[::-1].find(')')]

    x_element = browser.find_element(By.CSS_SELECTOR, '#treasure')
    x = int(x_element.get_attribute('valuex'))

    input = browser.find_element(By.CSS_SELECTOR, '#answer')
    input.send_keys(calc(formula,x))
    chk_box = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    chk_box.click()
    radio_btn = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    radio_btn.click()

    # Отправляем заполненную форму
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()