from page_objects.base_page import BasePage
from page_objects.filter_block import FilterBlockInputs, FilterBlockCheckboxes


class MobileDevices(BasePage):
    def __init__(self, driver_wrapper):
        super().__init__(driver_wrapper)
        self.apply_button_selector = "button.button_action_n-filter-apply"
        self.cell_element_selector = "div.snippet-cell"
        self.sort_filter_selector = "div.n-filter-panel-dropdown__main"
        self.cell_title_selector = "h4.title"
        self.cell_element_link = "a.snippet-cell__image"
        self.loading_selector = "div.preloadable__preloader_visibility_visible"
        self.next_page_selector = "a.n-pager__button-next"

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
        self.wait_until_filtered(self.loading_selector)
        return self

    def change_sorting_by_name(self, name):
        self.click_element_by_link_text(self.sort_filter_selector, name)
        self.wait_until_filtered(self.loading_selector)
        return self

    def click_next_page(self):
        self.click_element_by_selector(self.next_page_selector)
        self.wait_until_filtered(self.loading_selector)
        return self

    def get_name_of_cell_by_number(self, number):
        el_group = self.get_group_of_elements_by_selector(self.cell_element_selector)
        el = el_group[number-1]
        title_el = self.get_one_element_in_element_by_selector(el, self.cell_title_selector)
        return title_el.text
    
    def click_cell_element_by_name(self, name):
        el = self.get_element_contains_text_in_area(self.cell_element_selector, self.cell_title_selector, name)
        if el is None:
            print('{} not found on this page, going for the next...'.format(name))
            self.click_next_page()
            self.click_cell_element_by_name(name)
        else:
            self.click_element_in_element_by_selector(el, self.cell_element_link)
        return self

    def get_count_of_found_elements(self):
        return self.get_count_of_elements_by_selector(self.cell_element_selector)