import sys
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


yandex_url = 'https://yandex.ru'
CLICK_TIMEOUT = 30


# 'https://github.com/mozilla/geckodriver/releases'
# https://chromedriver.storage.googleapis.com/index.html?path=2.31/

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

	# def click_link(link_selector: str, return_page=None):
		

	# 	if return_page is not None:
	# 		return return_page(self.driver_wrapper)

class YandexHome(BasePage):

	def __init__(self, driver_wrapper):
		super().__init__(driver_wrapper)
		self.market_link_selector = "a[data-id='market']"

	def go_to_market(self):
		self.click_element_by_selector(self.market_link_selector)
		return YandexMarketHome(self.driver_wrapper)


class YandexMarketHome(BasePage):
	def __init__(self, driver_wrapper):
		super().__init__(driver_wrapper)
		self.electronika_link_selector = "li[data-department='Электроника'] a"
		self.submenu_items_selector = "div.topmenu__sublist"

	def choose_electronic_menu(self):
		self.hover_element(self.electronika_link_selector)
		return self

	def click_on_mobile_devices(self):
		self.click_element_by_name(self.submenu_items_selector, 'Мобильные телефоны')
		

class DriverWrapper():
	def __init__(self, browser_name: str):
		try:
			if browser_name.lower() == 'chrome':
				self.chrome_options = webdriver.ChromeOptions()
				# self.browser_options.add_argument("--incognito")
				# self.browser_options.add_argument("--start-maximized")
				self.driver = webdriver.Chrome(chrome_options=self.chrome_options)
			if browser_name.lower() == 'firefox':
				self.firefox_options = webdriver.FirefoxProfile()
				self.driver = webdriver.Firefox(firefox_profile=self.firefox_options)
		except selenium.common.exceptions.WebDriverException as e:
			print('Cannot get the driver for the {}.\n{}'.format(browser_name.capitalize(), e))
			sys.exit(1)
			
	
	def go_to(self, url: str, return_page=None):
		self.driver.get(url)
		if return_page is not None:
			return return_page(self)


DriverWrapper('chrome').go_to(yandex_url, YandexHome).go_to_market().choose_electronic_menu().click_on_mobile_devices()

# submitButton = driver.find_element_by_css_selector("button.login-form-button")
# submitButton.click()

# so1 = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button.o365button._hl_2._hl_e .wf-owa-triangle-down-small')))
# so1.click()
# so2 = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.headerMenuDropShadow div.o365button span[aria-label="Sign out"]')))
# so2.click()
