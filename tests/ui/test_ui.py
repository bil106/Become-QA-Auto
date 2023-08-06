import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



@pytest.mark.ui
def test_check_incorrect_username():
    #Создаем обьект для управлением браузером
    driver = webdriver.Chrome(
    service=Service(r"D:\\QA Python\\QA_Auto" + "chromedriver-win64.exe")
    )

    #Открываем страницу https://github.com
    driver.get("https://github.com/login")

    #Ищем поле ввода имени
    login_elem = driver.find_element(By.ID, "login_field")

    #Вводим неправильное имя
    login_elem.send_keys("sergiibutenko@mistakeinemail.com")
  

    #Ищем поле ввода пароля
    pass_elem = driver.find_element(By.ID, "password")
   
   #Вводим неправильный пароль
    pass_elem.send_keys("wrong password")
   

   #Ищем кнопку Sign in
    btn_elem = driver.find_element(By.NAME, "commit")

   #Нажимаем на кнопку через команду click
    btn_elem.click()
    

    #Проверяем что мы после всех вводов и нажатия кнопки находимся на стр гитхаб и никуда не перешли
    assert driver.title == "Sign in to GitHub · GitHub"
   

    #Закрываем браузер
    driver.close()