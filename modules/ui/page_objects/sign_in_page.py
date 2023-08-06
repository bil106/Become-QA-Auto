from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    URL = "https://github.com/login"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):
         #Ищем поле ввода имени
        login_elem = self.driver.find_element(By.ID, "login_field")

    #Вводим неправильное имя
        login_elem.send_keys(username)
  

    #Ищем поле ввода пароля
        pass_elem = self.driver.find_element(By.ID, "password")
   
   #Вводим неправильный пароль
        pass_elem.send_keys(password)
   

   #Ищем кнопку Sign in
        btn_elem = self.driver.find_element(By.NAME, "commit")

   #Нажимаем на кнопку через команду click
        btn_elem.click()    

    def check_title(self, expected_title):
        return self.driver.title == expected_title