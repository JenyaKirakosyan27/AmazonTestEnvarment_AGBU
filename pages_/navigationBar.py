from selenium.webdriver.common.by import By
from selenium import webdriver


class NavigationBar():


    def __init__(self,driver: webdriver.Chrome):
        self.driver = driver


    def click_to_cart_button(self):
        cartbuttonElement = self.driver.find_element(By.ID, "nav-cart-count-container")
        cartbuttonElement.click()