import time


class TestProduct:
    def test_add_to_basket_button_is_present(self, browser):
        browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
        time.sleep(10)  # for language checking
        assert browser.find_element('class name', 'btn-add-to-basket'), "There is no 'Add to basket' button"
