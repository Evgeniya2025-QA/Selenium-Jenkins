import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
# Генерация случайных данных
fake = Faker(["ru_RU"])
randomName = fake.name()
randomLastName = fake.last_name()
randomNumber = fake.phone_number()
# Настройка драйвера
link = "https://orion10.ru/"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)
# -------------------------------------
print("ОР: Клик на ссылку 'Вход'")
auth = browser.find_element(By.XPATH, "//nav[@class='auth_menu']//li[1]/a").click()
print("ФР: Переход на страницу 'Вход / Регистрация' выполнен успешно")
print("ОР: Ввод адреса электронной почты")
email = browser.find_element(By.ID, "login-email").send_keys('1kv2j@edny.net')
print("ФР: Введён адрес электронной почты")
print("ОР: Ввод пароля")
password = browser.find_element(By.ID, "login-password").send_keys('Vj9H7tLw4Aj6mQjR')
print("ФР: Пароль введён")
print("ОР: Клик на кнопку 'Войти'")
submit = browser.find_element(By.XPATH, "//input[@value='Войти']").click()
print("ФР: Авторизация выполнена успешно, осуществлён переход на страницу 'Мои заказы'")
time.sleep(10)
print("ОР: Проверка, что мы находимся на странице 'Мои заказы'")
check = WebDriverWait(browser, 3).until(
    EC.visibility_of_element_located((By.XPATH, "//h1"))).text
check1 = "Мои заказы"
assert check ==check1, f"Тест не прошел проверку, есть альтернатива {check}"
print("ФР: Мы находимся на странице 'Мои заказы'")
