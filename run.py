from driver_wrapper import DriverWrapper
from page_objects.home import Home

yandex_url = 'https://yandex.ru'

# 'https://github.com/mozilla/geckodriver/releases'
# 'https://chromedriver.storage.googleapis.com/index.html?path=2.31/'

DriverWrapper('chrome') \
.go_to(yandex_url, Home) \
.go_to_market() \
.choose_main_menu_item('Электроника') \
.click_on_submenu_item('Мобильные телефоны') \
.change_filter_to_by_name('Цена', '20000') \
.change_filter_from_by_name('Диагональ экрана', '3')