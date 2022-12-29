from selene import have


class RadioFactory:

    def __init__(self, element):
        self.element = element

    def set_radio(self, value):
        self.element.element_by(have.value(value)).element('..').click()