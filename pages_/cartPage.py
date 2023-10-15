from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class CartPage():
    def __init__(self,driver: webdriver.Chrome):
        self.driver = driver


    def delete_firstProduct_from_cart(self):
        firstProductDeleteButtonElement = self.driver.find_element(By.XPATH, "(//input[@value ='Delete'])[1]")
        firstProductDeleteButtonElement.click()
        sleep(6)