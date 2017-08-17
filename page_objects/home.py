from page_objects.base_page import BasePage
from page_objects.market_home import MarketHome

class Home(BasePage):

	def __init__(self, driver_wrapper):
		super().__init__(driver_wrapper)
		self.market_link_selector = "a[data-id='market']"

	def go_to_market(self):
		self.click_element_by_selector(self.market_link_selector)
		return MarketHome(self.driver_wrapper)