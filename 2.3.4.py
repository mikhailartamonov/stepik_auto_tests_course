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
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # -----------------
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    browser.switch_to.alert.accept()

    formula_element = browser.find_element(By.CSS_SELECTOR, 'label span.nowrap:nth-child(1)')
    formula = formula_element.text
    formula = formula[formula.find('is')+3:-formula[::-1].find(')')]

    x_element = int(browser.find_element(By.CSS_SELECTOR, '#input_value').text)

    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(calc(formula, x_element))

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()
    


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()