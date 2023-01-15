from datetime import date

from demoqa_tests.model.pages.practice_form import PracticePage
from demoqa_tests.model.data.student import Student, Hobby

practice_form = PracticePage()


def test_registration():
    student = Student(
        first_name='Alexander',
        last_name='Santalov',
        email='asantalov@bolid.ru',
        phone='8916777665',
        address='Zelenograd',
        birthday=date(1986, 8, 3),
        gender='Male',
        subject='Chemistry',
        hobby=[Hobby.Music, Hobby.Sports],
        image='Toolsqa.jpg',
        state='Haryana',
        city='Panipat')

    practice_form.open()
    practice_form.fill(student).submit()
    practice_form.assert_results_registration(student)
