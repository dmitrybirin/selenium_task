from config import LOCATE_TIMEOUT
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class BasePage(object):
    def __init__(self, driver_wrapper):
        self.driver_wrapper = driver_wrapper

    def click_element_by_selector(self, selector):
        el = WebDriverWait(self.driver_wrapper.driver, LOCATE_TIMEOUT).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
        el.click()

    def click_element_by_name(self, area_selector, text):
        el_group = WebDriverWait(self.driver_wrapper.driver, LOCATE_TIMEOUT).until(EC.visibility_of_element_located((By.CSS_SELECTOR, area_selector)))
        el = el_group.find_element_by_link_text(text)
        el.click()

    def hover_element(self, selector):
        el = WebDriverWait(self.driver_wrapper.driver, LOCATE_TIMEOUT).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
        builder = webdriver.ActionChains(self.driver_wrapper.driver)
        builder.move_to_element(el).perform()

    def send_text_by_selector(self, selector, text):
        el = WebDriverWait(self.driver_wrapper.driver, LOCATE_TIMEOUT).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
        el.send_keys(text)

    def click_element_in_element_by_selector(self, parentElement, selector):
        el = parentElement.find_element(By.CSS_SELECTOR, selector)
        el.click()

    def get_element_contains_text_in_area(self, area_selector, text_selector, text):
        WebDriverWait(self.driver_wrapper.driver, LOCATE_TIMEOUT).until(EC.visibility_of_element_located((By.CSS_SELECTOR, area_selector)))
        el_group = self.driver_wrapper.driver.find_elements(By.CSS_SELECTOR, area_selector)
        
        for el in el_group:
            try:
                text_element = el.find_element(By.CSS_SELECTOR, text_selector)
            except NoSuchElementException as e: 
                print('No element with selector {} was found in {}'.format(text_selector, el))
                pass
            if text in text_element.text:
                return el