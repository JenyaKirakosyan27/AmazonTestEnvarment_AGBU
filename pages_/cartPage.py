from selenium import webdriver
from selenium.webdriver.common.by import By



class CartPage():
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver


    def delete_secondProduct_from_cart(self):
        secondProductDeleteButtonElement = self.driver.find_element(By.NAME, "submit.delete.321fc73c-27b5-4963-9062-d31698e70e9e")
        secondProductDeleteButtonElement.click()




    def save_for_later_firstProduct_from_cart(self):
        firstProductSaveForLeterButtonElement = self.driver.find_element(By.XPATH, "(//input[@name ='submit.save-for-later.8ac998b5-36b3-435b-8715-f53a826c6f1a'])[1]")
        firstProductSaveForLeterButtonElement.click()



