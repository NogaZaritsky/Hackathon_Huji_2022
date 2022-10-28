
from django.core.management.base import BaseCommand, CommandError
from Customers.models import Customer


class Student():
    def __init__(self, customer):
        self.id = customer.id
        self.name = customer.name
        self.family_name = customer.family_name
        self.age = customer.age
        self.courses = customer.courses.split(",")
        self.home = customer.home
        self.study_year = customer.study_year
        self.preferred_study_locations = customer.preferred_study_locations.split(",")
        self.preferred_study_habits = customer.preferred_study_habits.split(",")
        self.preferred_study_group_size = customer.preferred_study_group_size
        self.weight_for_each_preference = customer.weight_for_each_preference.split(",")
        self.age_difference = 0
        self.year_difference = 0
        self.common_courses = 0
        self.closer_home = 0
        self.place_match = 0
        self.technic_match = 0
        self.group_match = 0
    
    def __str__(self):
        return self.name +" "+self.family_name


# student1 = Student(209705292, 3, 1,[80116, 80135, 80132, 67315, 67109], 7, [1,2], [0,4,7], 2, ["year", "group", "study_technic", "place", "home", "courses", "age"])
# student2 = Student(459505381, 2, 1,[80116, 80135, 80131, 67101], 6, [2,1], [0,2,3], 4, ["year", "study_technic", "place", "age", "home","group", "courses"])
# student3 = Student(989346323, 2, 2,[67315, 80135, 80132, 80181], 2, [4,1], [1,3,4], 6, ["courses", "study_technic", "place", "year", "group", "age", "home"])
# student4 = Student(657326598, 5,3,[69174, 80134, 80132, 67101], 1, [3,2], [1,5,7], 2, ["group", "study_technic", "year", "courses", "place", "age", "home"])
# student5 = Student(953526521, 3,2,[80116, 80134, 80131, 72160], 3, [4,2], [0,2,9], 4, ["study_technic", "courses", "year", "age", "place", "home", "group"])
# student6 = Student(930526458, 3,1,[67315, 80135, 80131, 72160], 8, [2,4], [0,1,8], 6, ["home", "year", "study_technic", "group", "courses", "age", "place"])
# student7 = Student(435236790, 3,2,[80116, 80134, 80132, 67101], 4, [1,3], [6,7,8], 4, ["place", "age", "group", "home", "year", "study_technic", "courses"])
# student8 = Student(213236213, 2,3,[67315, 69174, 72160, 67101], 2, [2,3], [5,4,2], 2, ["year", "place", "age", "group", "courses", "home", "study_technic"])
# student9 = Student(101236325, 4,2,[67101, 69174, 80134, 67559, 80132], 7, [1,4], [4,9,6], 6, ["place", "group", "year", "age", "home", "study_technic", "courses"])
# student10 = Student(256236387, 4,1,[80116, 69174, 80134, 67559, 80131], 5, [1,4], [4,9,6], 4, ["place", "year", "age", "home", "study_technic", "courses", "group"])
# users_list = [student1, student2, student3, student4, student5, student6, student7, student8, student9, student10]




