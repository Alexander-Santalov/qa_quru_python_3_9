from selene import have


class DropdownFactory:

    def __init__(self, element, elements):
        self.element = element
        self.elements = elements

    def select_value_from_drop_down_list(self, value):
        self.element.click()
        self.elements.element_by(have.exact_text(value)).click()
