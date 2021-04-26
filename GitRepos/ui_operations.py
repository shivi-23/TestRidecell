from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from GitRepos.data import ui_data
import os

DRIVER_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'executable'))

class UIOps:

    @staticmethod
    def get_driver():
        global driver
        if ui_data.browser == "chrome":
            chrome_driver_path = os.path.abspath(os.path.join(DRIVER_PATH, ui_data.chrome_binary))
            driver = webdriver.Chrome(chrome_driver_path)
        elif ui_data.browser == "firefox":
            firefox_driver_path = os.path.abspath(os.path.join(DRIVER_PATH, ui_data.firefox_binary))
            driver = webdriver.Firefox(firefox_driver_path)
        return driver

    def open_browser(self):
        driver = self.get_driver()
        driver.get(ui_data.url)
        driver.maximize_window()
        driver.implicitly_wait(ui_data.wait)

    @staticmethod
    def click_element(locator, element_path):
        element = driver.find_element(locator, element_path).click()
        return element

    @staticmethod
    def get_element_text(locator, element_path):
        element_text = driver.find_element(locator, element_path).text
        return element_text

    @staticmethod
    def get_elements(locator, element_path):
        elements = driver.find_elements(locator, element_path)
        return elements

    @staticmethod
    def implicit_wait():
        driver.implicitly_wait(ui_data.wait)

    @staticmethod
    def explicit_wait_for_element_to_be_present(locator, element_path):
        WebDriverWait(driver, ui_data.wait).until(EC.visibility_of_element_located((locator, element_path)))

    @staticmethod
    def close_browser():
        driver.quit()





