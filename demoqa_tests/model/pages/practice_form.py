from selene import have, be
from selene.support.shared import browser

from demoqa_tests.model.methods.checkbox import CheckboxFactory
from demoqa_tests.model.methods.datepicker import DatepickerFactory
from demoqa_tests.model.methods.dropdown import DropdownFactory
from demoqa_tests.model.methods.radio import RadioFactory
from demoqa_tests.utils import path_generate, config


class PracticePage:
    def __init__(self, student):
        self.student = student

    def open(self):
        browser.open('/automation-practice-form')
        return self

    def fill_name(self):
        browser.element('#firstName').set_value(self.student.first_name)
        browser.element('#lastName').set_value(self.student.last_name)
        return self

    def fill_contacts(self):
        browser.element('#userEmail').set_value(self.student.email)
        browser.element('#userNumber').set_value(self.student.phone)
        return self

    def set_gender(self):
        gender = RadioFactory(browser.all('[name=gender]'))
        gender.set_radio(self.student.gender)
        return self

    def input_birthday(self):
        birthday_datepicker = DatepickerFactory(browser.element('#dateOfBirthInput'))
        birthday_datepicker.set_date(self.student.birthday)
        return self

    def input_subject(self):
        browser.element('#subjectsInput').type(self.student.subject)
        browser.all('.subjects-auto-complete__option').element_by(have.exact_text(
            self.student.subject)).should(be.visible)
        browser.element('#subjectsInput').press_tab()
        return self

    def set_hobby(self):
        select_hobby = CheckboxFactory(browser.all('[for^=hobbies-checkbox]'))
        select_hobby.set_checkboxes(self.student.hobby)
        return self

    def send_image(self):
        browser.element('#uploadPicture').set_value(path_generate.generate_path_upload(self.student.image))
        return self

    def input_address(self):
        browser.element('#currentAddress').set_value(self.student.address)
        return self

    def select_state(self):
        dropdown_state = DropdownFactory(browser.element('#state'), browser.all('[id^=react-select][id*=option]'))
        dropdown_state.select_value_from_drop_down_list(self.student.state)
        return self

    def select_city(self):
        dropdown_city = DropdownFactory(browser.element('#city'), browser.all('[id^=react-select][id*=option]'))
        dropdown_city.select_value_from_drop_down_list(self.student.city)
        return self

    def submit(self):
        browser.element('#submit').press_enter()
        return self

    def assert_results_registration(self, equal: int, ):
        browser.all('tbody tr').should(have.size(equal))
        browser.all('tbody tr td:last-child').should(have.exact_texts(
            self.student.first_name + ' ' + self.student.last_name,
            self.student.email,
            self.student.gender,
            self.student.phone,
            self.student.birthday.strftime(config.datetime_view_format),
            self.student.subject,
            ', '.join(hobby.name for hobby in self.student.hobby),
            self.student.image,
            self.student.address,
            self.student.state + ' ' + self.student.city))
        return self
