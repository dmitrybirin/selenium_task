from page_objects.base_page import BasePage
from page_objects.mobile_devices import MobileDevices

class MarketHome(BasePage):
    def __init__(self, driver_wrapper):
        super().__init__(driver_wrapper)
        self.electronika_link_selector_template = "li[data-department='%s'] a"
        self.submenu_items_selector = "div.topmenu__sublist"
        
    def choose_main_menu_item(self, name):
        self.hover_element_by_selector(self.electronika_link_selector_template % name)
        return self

    def click_on_submenu_item(self, name):
        self.click_element_by_link_text(self.submenu_items_selector, name)
        return MobileDevices(self.driver_wrapper)