from page_objects.base_page import BasePage
from page_objects.filter_block import FilterBlock


class MobileDevices(BasePage):
    def __init__(self, driver_wrapper):
        super().__init__(driver_wrapper)
        self.apply_button_selector = "button.button_action_n-filter-apply"
        self.found_element_selector = "div.snippet-cell"

    def change_filter_to_by_name(self, name, text):
        FilterBlock(self.driver_wrapper, name).open_block_if_closed().change_text_inputs(to=text)
        return self
    
    def change_filter_from_by_name(self, name, text):
        FilterBlock(self.driver_wrapper, name).open_block_if_closed().change_text_inputs(fr=text)
        return self

    def apply_filters(self):
        self.click_element_by_selector(self.apply_button_selector)
        return self

    def get_count_of_found_elements(self):
        return self.get_count_of_elements_by_selector(self.found_element_selector)