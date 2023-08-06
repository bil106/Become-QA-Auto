from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class PostOfficePage(BasePage):
    URL = "https://novoposhta.com/#top"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(PostOfficePage.URL)

    def try_numb_pack(self,number):
         #Ищем поле ввода номера
        pack_nub = self.driver.find_element(By.ID, "number")

    #Вводим неправильный номер
        pack_nub.send_keys(number)
   

   #Ищем кнопку Отследить
        btn_elem = self.driver.find_element(By.CLASS_NAME, "actions")

   #Нажимаем на кнопку через команду click
        btn_elem.click()    

    
    def check_massege(self,expected_title):
       return self.driver.title == expected_title