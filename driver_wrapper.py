import sys
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

class DriverWrapper():
    def __init__(self, browser_name: str):
        try:
            if browser_name.lower() == 'chrome':
                self.chrome_options = webdriver.ChromeOptions()
                self.chrome_options.add_argument('--kiosk')
                self.chrome_options.add_argument('--start-maximized')
                self.driver = webdriver.Chrome(chrome_options=self.chrome_options)
            else:
                print('{} is not supported'.format(browser_name))
                sys.exit(1)    
        except WebDriverException as e:
            print('Cannot get the driver for the {}.\n{}'.format(browser_name.capitalize(), e))
            sys.exit(1)

    def go_to(self, url: str, return_page=None):
        self.driver.get(url)
        if return_page is not None:
            return return_page(self)