from page_objects.base_page import BasePage

class MobileDevices(BasePage):
    def __init__(self, driver_wrapper):
        super().__init__(driver_wrapper)
        self.filter_block_selector = "div.n-filter-block_type_normal"
        self.filter_block_text_selector = "span.title__content"
        self.price_to_selector = "input#glf-priceto-var"
        self.price_from_selector = "input#glf-pricefrom-var"
        category_display_size = 4925721
        self.display_size_to_selector = "input#glf-%s-to" % category_display_size
        self.display_size_from_selector = "input#glf-%s-from" % category_display_size
        self.block_closed_class = 'n-filter-block_closed_yes'
        self.block_open_class = 'n-filter-block_closed_no'

    def open_block_by_name(self, name):
        block_el = self.get_element_contains_text_in_area(self.filter_block_selector, self.filter_block_text_selector, name)
        classes = block_el.get_attribute('class')
        if self.block_closed_class in classes:
            self.click_element_in_element_by_selector(block_el, self.filter_block_text_selector)
        else: 
            if self.block_open_class in classes:
                print('filter block {} is already open'.format(name))
            else:
                raise Exception('Filter block {} nor close nor open!'.format(name))
        return self