from config import CLICK_TIMEOUT
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
	def __init__(self, driver_wrapper):
		self.driver_wrapper = driver_wrapper

	def click_element_by_selector(self, selector):
		el = WebDriverWait(self.driver_wrapper.driver, CLICK_TIMEOUT).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
		el.click()

	def click_element_by_name(self, area_selector, text):
		el_group = WebDriverWait(self.driver_wrapper.driver, CLICK_TIMEOUT).until(EC.visibility_of_element_located((By.CSS_SELECTOR, area_selector)))
		el = el_group.find_element_by_link_text(text)
		el.click()

	def hover_element(self, selector):
		el = WebDriverWait(self.driver_wrapper.driver, CLICK_TIMEOUT).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
		builder = webdriver.ActionChains(self.driver_wrapper.driver)
		builder.move_to_element(el).perform()