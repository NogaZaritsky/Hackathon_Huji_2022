
class Student():
    def __init__(self, student_id, age, study_year, courses, home,
        preferred_study_locations, preferred_study_habits,
                 preferred_study_group_size, weight_for_each_preference):
        self.id = student_id
        self.age = age
        self.courses = courses
        self.home = home
        self.study_year = study_year
        self.preferred_study_locations = preferred_study_locations
        self.preferred_study_habits = preferred_study_habits
        self.preferred_study_group_size = preferred_study_group_size
        self.weight_for_each_preference = weight_for_each_preference
        self.age_difference = 0
        self.year_difference = 0
        self.common_courses = 0
        self.closer_home = 0
        self.place_match = 0
        self.technic_match = 0
        self.group_match = 0

    def _str_(self):
        print(self.age)
        print(self.courses)
        print(self.home)
        print(self.study_year)
        print(self.preferred_study_locations)
        print(self.preferred_study_habits)
        print(self.preferred_study_group_size)
        print(self.weight_for_each_preference)


# class Student():
#     def __init__(self, customer):
#         self.name = customer.name
#         self.family_name = customer.family_name
#         self.age = customer.age
#         self.courses = ",".split(customer.courses)
#         self.home = customer.home
#         self.study_year = customer.study_year
#         self.preferred_study_locations = ",".split(
#             customer.preferred_study_locations)
#         self.preferred_study_habits = ",".split(
#             customer.preferred_study_habits)
#         self.preferred_study_group_size = ",".split(
#             customer.preferred_study_group_size)
#         self.weight_for_each_preference = ",".split(
#             customer.weight_for_each_preference)
#         self.age_difference = 0