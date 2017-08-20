from config import LOCATE_TIMEOUT
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class BasePage(object):
    def __init__(self, driver_wrapper):
        self.driver_wrapper = driver_wrapper

    def get_group_of_elements_by_selector(self, selector):
        """
        Get all elements by selector

        Args:
            selector (str): css selector of the elements to find
        """
        WebDriverWait(self.driver_wrapper.driver, LOCATE_TIMEOUT).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
        return self.driver_wrapper.driver.find_elements(By.CSS_SELECTOR, selector)

    def get_count_of_elements_by_selector(self, selector):
        """
        Get count of the elements

        Args:
            selector (str): css selector
        """
        return len(self.get_group_of_elements_by_selector(selector))

    def get_elements_in_element_by_selector(self, parentElement, selector):
        """
        Search for all elements within parent element and return it

        Args:
            parentElement (WebElement): parent element, where all elements should be found
            selector (str): css selector of the element to find
        """
        return parentElement.find_elements(By.CSS_SELECTOR, selector)

    def get_one_element_in_element_by_selector(self, parentElement, selector):
        """
        Search for the first element within parent element and return it

        Args:
            parentElement (WebElement): parent element, where element should be found
            selector (str): css selector of the element to find
        """
        return parentElement.find_element(By.CSS_SELECTOR, selector)

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
        """
        Get the first element in group with the with specific text within specific area

        Args:
            area_selector (str): selector to find area of elements to search
            text_selector (str): element that should contain text to search
            text (str): text to search
        """
        el_group = self.get_group_of_elements_by_selector(area_selector)
        for el in el_group:
            try:
                text_element = el.find_element(By.CSS_SELECTOR, text_selector)
            except NoSuchElementException as e: 
                print('No element with selector {} was found in {} element'.format(text_selector, el.tag_name))
                pass
            if text in text_element.text:
                return el

    def hover_element_by_selector(self, selector):
        """
        Hover mouse upon the element with selector

        Args:
            selector (str): css selector of the element to find
        """
        el = WebDriverWait(self.driver_wrapper.driver, LOCATE_TIMEOUT).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
        builder = webdriver.ActionChains(self.driver_wrapper.driver)
        builder.move_to_element(el).perform()
    
    def click_element_by_selector(self, selector):
        """
        Click element by selector with waiting to be clickable

        Args:
            selector (str): css selector
        """
        el = WebDriverWait(self.driver_wrapper.driver, LOCATE_TIMEOUT).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
        el.click()

    def click_element_by_link_text(self, area_selector, text):
        """
        Click element by link text in some area

        Args:
            area_selector (str): css selector of the area for link
            text (str): text to find
        """
        el_group = WebDriverWait(self.driver_wrapper.driver, LOCATE_TIMEOUT).until(EC.visibility_of_element_located((By.CSS_SELECTOR, area_selector)))
        el = el_group.find_element_by_link_text(text)
        el.click()

    def click_element_in_element_by_selector(self, parentElement, selector):
        """
        Search for element within parent element and click it

        Args:
            parentElement (WebElement): parent element, where next element should be found
            selector (str): css selector of the element to click
        """
        el = self.get_one_element_in_element_by_selector(parentElement, selector)
        el.click()

    def send_text_by_selector(self, selector, text):
        """
        Send text to the element by selector

        Args:
            selector (str): css selector of the element to find
            text (str): text to send to the element
        """
        el = WebDriverWait(self.driver_wrapper.driver, LOCATE_TIMEOUT).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
        el.send_keys(text)
    
    def send_text_by_element(self, element, text):
        """
        Send text to the element

        Args:
            element (WebElement): element to send text
            text (str): text to send to the element
        """
        element.send_keys(text)

    def wait_until_filtered(self, selector):
        """
        Waiting for the element with selector will disappear

        Args:
            selector (str): css selector of the element to wait
        """
        WebDriverWait(self.driver_wrapper.driver, LOCATE_TIMEOUT).until_not(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))