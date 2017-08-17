from driver_wrapper import DriverWrapper
from page_objects.home import Home

yandex_url = 'https://yandex.ru'

# 'https://github.com/mozilla/geckodriver/releases'
# 'https://chromedriver.storage.googleapis.com/index.html?path=2.31/'

DriverWrapper('chrome').go_to(yandex_url, Home).go_to_market().choose_electronic_menu().click_on_mobile_devices()