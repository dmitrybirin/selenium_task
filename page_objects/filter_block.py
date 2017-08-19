from page_objects.base_page import BasePage

class FilterBlock(BasePage):

    def __init__(self, driver_wrapper, name):
        super().__init__(driver_wrapper)
        self.filter_block_selector = "div.n-filter-block_type_normal"
        self.filter_block_text_selector = "span.title__content"
        self.filter_block_header = "h4.title"
        self.block_closed_class = 'n-filter-block_closed_yes'
        self.block_open_class = 'n-filter-block_closed_no'
        self.input_selector = "input.input__control"
        self.name = name
        self.block = self._get_block_by_name(name)

    def _get_block_by_name(self, name):
        return self.get_element_contains_text_in_area(self.filter_block_selector, self.filter_block_text_selector, name)

    def change_text_inputs(self, fr=None, to=None):
        if fr is None and to is None:
            raise Exception('Someting should be change in change method')
        else:
            if fr is not None:
                el = self.get_first_element_by_tag_text_in_attr('input', 'from', 'id', self.block)
                self.send_text_by_element(el, fr)
            if to is not None:
                el = self.get_first_element_by_tag_text_in_attr('input', 'to', 'id', self.block)
                self.send_text_by_element(el, to)

    def open_block_if_closed(self):
        classes = self.block.get_attribute('class')
        if self.block_closed_class in classes:
            self.click_element_in_element_by_selector(self.block, self.filter_block_header)
        else: 
            if self.block_open_class in classes:
                print('filter block {} is already open'.format(self.name))
            else:
                raise Exception('Filter block {} nor close nor open!'.format(self.name))
        return self