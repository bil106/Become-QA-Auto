from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class BasePage:
    PATH = r"D:\\QA Python\\QA_Auto"
    DRIVER_NAME = "chromedriver-win64.exe"

    def __init__(self) -> None:
        self.driver = webdriver.Chrome(
          service=Service(BasePage.PATH + BasePage.DRIVER_NAME)  
        )
    def close(self):
        self.driver.close()