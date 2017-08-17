from page_objects.base_page import BasePage
from page_objects.yandex_market_home import YandexMarketHome

class YandexHome(BasePage):

	def __init__(self, driver_wrapper):
		super().__init__(driver_wrapper)
		self.market_link_selector = "a[data-id='market']"

	def go_to_market(self):
		self.click_element_by_selector(self.market_link_selector)
		return YandexMarketHome(self.driver_wrapper)