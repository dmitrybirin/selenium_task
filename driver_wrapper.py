import sys
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

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
		except WebDriverException as e:
			print('Cannot get the driver for the {}.\n{}'.format(browser_name.capitalize(), e))
			sys.exit(1)
			
	
	def go_to(self, url: str, return_page=None):
		self.driver.get(url)
		if return_page is not None:
			return return_page(self)