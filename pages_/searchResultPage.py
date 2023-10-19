from selenium.webdriver.common.by import By
from selenium import webdriver


class SearchResultPage():
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_to_add_to_cart_button(self):
        addToCartButtonElement = self.driver.find_element(By.XPATH, "//span[@id = 'submit.add-to-cart']")
        addToCartButtonElement.click()