import datetime
from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import Literal, List


class Student:

    def __init__(self, first_name, last_name, email, phone, address, birthday, gender, subject, hobby, image,
                 state, city):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address
        self.birthday = birthday
        self.gender = gender
        self.subject = subject
        self.hobby = hobby
        self.image = image
        self.state = state
        self.city = city


class Hobby(Enum):
    Music = 1,
    Reading = 2,
    Sports = 3


@dataclass
class Student_:
    first_name: str
    last_name: str
    email: str
    phone: str
    address: str
    birthday: datetime.date
    gender: Literal['Male', 'Female', 'Other']
    subject: Literal['Maths', 'Accounting', 'Arts', 'Social Studies', 'English', 'Chemistry', 'Physics',
                     'Computer Science', 'Economics', 'History', 'Civics', 'Commerce', 'Biology', 'Hindi']
    hobby: List[Hobby]
    image: str
    state: Literal['NCR', 'Uttar Pradesh', 'Haryana', 'Rajasthan']
    city: Literal['Karnal', 'Panipat', 'Delhi', 'Gurgaon', 'Noida', 'Agra', 'Merrut', 'Lucknow', 'Jaipur', 'Jaiselmer']


a_santalov = Student_(
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
