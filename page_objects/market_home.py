from page_objects.base_page import BasePage

class MarketHome(BasePage):
    def __init__(self, driver_wrapper):
        super().__init__(driver_wrapper)
        self.electronika_link_selector = "li[data-department='Электроника'] a"
        self.submenu_items_selector = "div.topmenu__sublist"
        self.mobile_devices_text = "Мобильные телефоны"
        
    def choose_electronic_menu(self):
        self.hover_element(self.electronika_link_selector)
        return self

    def click_on_mobile_devices(self):
        self.click_element_by_name(self.submenu_items_selector, self.mobile_devices_text)