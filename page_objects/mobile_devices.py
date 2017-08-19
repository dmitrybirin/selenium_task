from page_objects.base_page import BasePage
from page_objects.filter_block import FilterBlock


class MobileDevices(BasePage):
    def __init__(self, driver_wrapper):
        super().__init__(driver_wrapper)
        self.price_to_selector = "input#glf-priceto-var"
        self.price_from_selector = "input#glf-pricefrom-var"
        display_size_category = 4925721
        self.display_size_to_selector = "input#glf-%s-to" % display_size_category
        self.display_size_from_selector = "input#glf-%s-from" % display_size_category

    def change_filter_to_by_name(self, name, text):
        FilterBlock(self.driver_wrapper, name).open_block_if_closed().change_text_inputs(to=text)
    
    def change_filter_from_by_name(self, name, text):
        FilterBlock(self.driver_wrapper, name).open_block_if_closed().change_text_inputs(from=text)