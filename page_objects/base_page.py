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

    def get_count_of_elements_by_selector(self, selector):
        return len(self.find_group_of_elements_by_selector(selector))

    def click_element_in_element_by_selector(self, parentElement, selector):
        el = self.get_one_element_in_element_by_selector(parentElement, selector)
        el.click()

    def get_elements_in_element_by_selector(self, parentElement, selector):
        return parentElement.find_elements(By.CSS_SELECTOR, selector)

    def get_one_element_in_element_by_selector(self, parentElement, selector):
        return parentElement.find_element(By.CSS_SELECTOR, selector)

    def hover_element_by_selector(self, selector):
        el = WebDriverWait(self.driver_wrapper.driver, LOCATE_TIMEOUT).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
        builder = webdriver.ActionChains(self.driver_wrapper.driver)
        builder.move_to_element(el).perform()
    
    def hover_element_by_element(self, element):
        builder = webdriver.ActionChains(self.driver_wrapper.driver)
        builder.move_to_element(element).perform()

    def send_text_by_selector(self, selector, text):
        el = WebDriverWait(self.driver_wrapper.driver, LOCATE_TIMEOUT).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
        el.send_keys(text)

    def wait_until_filtered(self, selector):
        WebDriverWait(self.driver_wrapper.driver, LOCATE_TIMEOUT).until_not(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))

    def send_text_by_element(self, element, text):
        element.send_keys(text)

    def find_group_of_elements_by_selector(self, selector):
        WebDriverWait(self.driver_wrapper.driver, LOCATE_TIMEOUT).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
        return self.driver_wrapper.driver.find_elements(By.CSS_SELECTOR, selector)

    def get_first_element_by_tag_text_in_attr(self, tag, text, attr, parentElement=None):
        """
        Get the first element in group with the tag with specific text in attribute

        Args:
            tag (str): tag to search group of elements
            text (str): text to search in the attribute
            attr (str): attribute type to search (id, class...)
            parentElement (WebElement): optional parent element to search within
        """
        if parentElement is None:
            WebDriverWait(self.driver_wrapper.driver, LOCATE_TIMEOUT).until(EC.visibility_of_element_located((By.TAG_NAME, tag)))
            el_group = self.driver_wrapper.driver.find_elements_by_tag_name(tag)
        else:
            el_group = parentElement.find_elements_by_tag_name(tag)
        for el in el_group:
            attributes = el.get_attribute(attr)
            if type(attributes) == 'list':
                for attribute in attributes:
                    if text in attribute:
                        return el
            else:
                if text in attributes:
                    return el
    
    def get_element_contains_text_in_area(self, area_selector, text_selector, text):
        el_group = self.find_group_of_elements_by_selector(area_selector)
        for el in el_group:
            try:
                text_element = el.find_element(By.CSS_SELECTOR, text_selector)
            except NoSuchElementException as e: 
                print('No element with selector {} was found in {} element'.format(text_selector, el.tag_name))
                pass
            if text in text_element.text:
                return el