from demoqa_tests.model.pages.practice_form import PracticePage
from demoqa_tests.model.data.Student import a_santalov


def test_registration():
    practice_form = PracticePage(a_santalov)
    practice_form.open()
    practice_form.fill_name()\
        .fill_contacts()\
        .set_gender()\
        .input_birthday()\
        .input_subject()\
        .set_hobby()\
        .send_image()\
        .input_address()\
        .select_state().\
        select_city()\
        .submit()
    practice_form.assert_results_registration(10)