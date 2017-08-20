from page_objects.base_page import BasePage
from page_objects.filter_block import FilterBlockInputs, FilterBlockCheckboxes


class MobileDevices(BasePage):
    def __init__(self, driver_wrapper):
        super().__init__(driver_wrapper)
        self.apply_button_selector = "button.button_action_n-filter-apply"
        self.cell_element_selector = "div.snippet-cell"
        self.sort_filter_selector = "div.n-filter-panel-dropdown__main"
        self.cell_title_selector = "h4.title"

    def change_filter_to_by_name(self, name, text):
        FilterBlockInputs(self.driver_wrapper, name).open_block_if_closed().change_text_inputs(to=text)
        return self

    def check_random_visible_checkboxes(self, name, number):
        FilterBlockCheckboxes(self.driver_wrapper, name).open_block_if_closed().check_random_visible_checkboxes(number)
        return self
    
    def change_filter_from_by_name(self, name, text):
        FilterBlockInputs(self.driver_wrapper, name).open_block_if_closed().change_text_inputs(fr=text)
        return self

    def apply_filters(self):
        self.click_element_by_selector(self.apply_button_selector)
        return self

    def change_sorting_by_name(self, name):
        self.click_element_by_name(self.sort_filter_selector, name)
        return self

    def get_name_of_cell_by_number(self, number):
        el_group = self.find_group_of_elements_by_selector(self.cell_element_selector)
        el = el_group[number-1]
        title_el = self.get_one_element_in_element_by_selector(el, self.cell_title_selector)
        print(title_el.text)
        return self

    def get_count_of_found_elements(self):
        return self.get_count_of_elements_by_selector(self.cell_element_selector)