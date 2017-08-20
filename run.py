from driver_wrapper import DriverWrapper
from page_objects.home import Home

filteredResults = DriverWrapper('chrome') \
.go_to('https://yandex.ru', Home) \
.go_to_market() \
.choose_main_menu_item('Электроника') \
.click_on_submenu_item('Мобильные телефоны') \
.change_filter_to_by_name('Цена', '20000') \
.change_filter_from_by_name('Диагональ экрана', '3') \
.check_random_visible_checkboxes('Производитель', 5) \
.apply_filters()

count = filteredResults.get_count_of_found_elements()
print(count)

cell_name = filteredResults.get_name_of_cell_by_number(1)
filteredResults.change_sorting_by_name("по цене")
filteredResults.click_cell_element_by_name(cell_name)