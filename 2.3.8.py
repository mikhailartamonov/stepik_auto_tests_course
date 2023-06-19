import time
import math
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(formula,x):
  return eval(formula)

ln = math.log
sin = math.sin

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 50).until(EC.text_to_be_present_in_element((By.ID, "price"),'$100'))
    browser.find_element(By.CSS_SELECTOR, "button#book").click()




    # # -----------------
    # browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    # # browser.switch_to.alert.accept()
    # browser.switch_to.window(browser.window_handles[1])
    formula_element = browser.find_element(By.CSS_SELECTOR, 'label span.nowrap:nth-child(1)')
    formula = formula_element.text
    formula = formula[formula.find('is')+3:-formula[::-1].find(')')]

    x_element = int(browser.find_element(By.CSS_SELECTOR, '#input_value').text)

    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(calc(formula, x_element))

    browser.find_element(By.CSS_SELECTOR, "button#solve").click()

    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()

    


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    # time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()