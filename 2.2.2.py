import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(formula,x):
  return eval(formula)

ln = math.log
sin = math.sin

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    
    formula_element = browser.find_element(By.CSS_SELECTOR, 'div.form-group span.nowrap:nth-child(1)')
    formula = formula_element.text
    formula = formula[formula.find('is')+3:-formula[::-1].find(')')]

    x_element = int(browser.find_element(By.CSS_SELECTOR, '#input_value').text)



    input = browser.find_element(By.CSS_SELECTOR, '#answer')

    browser.execute_script("return arguments[0].scrollIntoView(true);", input)

    input.send_keys(calc(formula,x_element))

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