import datetime
from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import Literal, List


class Hobby(Enum):
    Music = 1,
    Reading = 2,
    Sports = 3


@dataclass
class Student:
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


a_santalov = Student(
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
