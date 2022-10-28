from typing import *
from copy import *
from .management.commands import Student 
Student = Student.Student

AGE_RANGE = 5
YEAR_RANGE = 3
COURSES_RANGE = 15
HOME_RANGE = 8
PLACE_RANGE = 3
STUDY_TECHNIC_RANGE = 4
GROUP_RANGE = 5
OTHER = 7
OUT_OF_JERUSALEM = 8


def main_func(users_list: List[Student]) -> List[List[int]]:
    final_list = []
    for student in users_list:
        student_final_list = [student.id]
        student_favorite_list = make_favorite(users_list, student)
        for user in student_favorite_list:
            student_final_list.append(user.id)
        final_list.append(student_final_list)
    return final_list


def make_favorite(users_list: List[Student], student: Student):
    student_favorite_list = users_list.copy()
    student_favorite_list.remove(student)
    for factor_ind in range(len(student.weight_for_each_preference) - 1, -1, -1):
        if student.weight_for_each_preference[factor_ind] == "age":
            age_sort(student_favorite_list, student)
        elif student.weight_for_each_preference[factor_ind] == "year":
            year_sort(student_favorite_list, student)
        elif student.weight_for_each_preference[factor_ind] == "courses":
            courses_sort(student_favorite_list, student)
        elif student.weight_for_each_preference[factor_ind] == "home":
            home_sort(student_favorite_list, student)
        elif student.weight_for_each_preference[factor_ind] == "place":
            place_sort(student_favorite_list, student)
        elif student.weight_for_each_preference[factor_ind] == "study_technic":
            study_technic_sort(student_favorite_list, student)
        elif student.weight_for_each_preference[factor_ind] == "group":
            group_sort(student_favorite_list, student)
    return student_favorite_list[:10]


def age_sort(student_favorite_list: List[Student], student: Student):
    for user in student_favorite_list:
        user.age_difference = abs(user.age - student.age)
    n = len(student_favorite_list)
    output_array = [0] * n
    count_array = [0] * AGE_RANGE
    for i in range(n):
        count_array[student_favorite_list[i].age_difference] += 1
    for j in range(1, AGE_RANGE):
        count_array[j] += count_array[j - 1]
    i = n - 1
    while i >= 0:
        output_array[count_array[student_favorite_list[i].age_difference] - 1]\
            = student_favorite_list[i]
        count_array[student_favorite_list[i].age_difference] -= 1
        i -= 1
    for j in range(n):
        student_favorite_list[j] = output_array[j]


def year_sort(student_favorite_list, student):
    for user in student_favorite_list:
        user.year_difference = abs(user.study_year - student.study_year)
    n = len(student_favorite_list)
    output_array = [0] * n
    count_array = [0] * YEAR_RANGE
    for i in range(n):
        count_array[student_favorite_list[i].year_difference] += 1
    for j in range(1, YEAR_RANGE):
        count_array[j] += count_array[j - 1]
    i = n - 1
    while i >= 0:
        output_array[count_array[student_favorite_list[i].year_difference] - 1]\
            = student_favorite_list[i]
        count_array[student_favorite_list[i].year_difference] -= 1
        i -= 1
    for j in range(n):
        student_favorite_list[j] = output_array[j]


def courses_sort(student_favorite_list, student):
    for user in student_favorite_list:
        for course in user.courses:
            if course in student.courses:
                user.common_courses += 1
    n = len(student_favorite_list)
    output_array = [0] * n
    count_array = [0] * COURSES_RANGE
    for i in range(n):
        count_array[student_favorite_list[i].common_courses] += 1
    for j in range(1, COURSES_RANGE):
        count_array[j] += count_array[j - 1]
    i = n - 1
    while i >= 0:
        output_array[count_array[student_favorite_list[i].common_courses] - 1] \
            = student_favorite_list[i]
        count_array[student_favorite_list[i].common_courses] -= 1
        i -= 1
    for j in range(n):
        student_favorite_list[j] = output_array[j]
    student_favorite_list.reverse()
    for user in student_favorite_list:
        user.common_courses = 0


def home_sort(student_favorite_list, student):
    if student.home == (OTHER or OUT_OF_JERUSALEM):
        for user in student_favorite_list:
            if user.home != student.home:
                user.closer_home = 1
    else:
        for user in student_favorite_list:
            user.closer_home = abs(user.home - student.home)
    n = len(student_favorite_list)
    output_array = [0] * n
    count_array = [0] * HOME_RANGE
    for i in range(n):
        count_array[student_favorite_list[i].closer_home] += 1
    for j in range(1, HOME_RANGE):
        count_array[j] += count_array[j - 1]
    i = n - 1
    while i >= 0:
        output_array[count_array[student_favorite_list[i].closer_home] - 1] \
            = student_favorite_list[i]
        count_array[student_favorite_list[i].closer_home] -= 1
        i -= 1
    for j in range(n):
        student_favorite_list[j] = output_array[j]


def place_sort(student_favorite_list, student):
    for user in student_favorite_list:
        for number in user.preferred_study_locations:
            if number in student.preferred_study_locations:
                user.place_match += 1
    n = len(student_favorite_list)
    output_array = [0] * n
    count_array = [0] * PLACE_RANGE
    for i in range(n):
        count_array[student_favorite_list[i].place_match] += 1
    for j in range(1, PLACE_RANGE):
        count_array[j] += count_array[j - 1]
    i = n - 1
    while i >= 0:
        output_array[count_array[student_favorite_list[i].place_match] - 1] \
            = student_favorite_list[i]
        count_array[student_favorite_list[i].place_match] -= 1
        i -= 1
    for j in range(n):
        student_favorite_list[j] = output_array[j]
    student_favorite_list.reverse()
    for user in student_favorite_list:
        user.place_match = 0


def study_technic_sort(student_favorite_list, student):
    for user in student_favorite_list:
        for number in user.preferred_study_habits:
            if number in student.preferred_study_habits:
                user.technic_match += 1
    n = len(student_favorite_list)
    output_array = [0] * n
    count_array = [0] * STUDY_TECHNIC_RANGE
    for i in range(n):
        count_array[student_favorite_list[i].technic_match] += 1
    for j in range(1, STUDY_TECHNIC_RANGE):
        count_array[j] += count_array[j - 1]
    i = n - 1
    while i >= 0:
        output_array[count_array[student_favorite_list[i].technic_match] - 1] \
            = student_favorite_list[i]
        count_array[student_favorite_list[i].technic_match] -= 1
        i -= 1
    for j in range(n):
        student_favorite_list[j] = output_array[j]
    student_favorite_list.reverse()
    for user in student_favorite_list:
        user.technic_match = 0

def group_sort(student_favorite_list, student):
    for user in student_favorite_list:
        user.group_match = abs(user.preferred_study_group_size - student.preferred_study_group_size)
    n = len(student_favorite_list)
    output_array = [0] * n
    count_array = [0] * GROUP_RANGE
    for i in range(n):
        count_array[student_favorite_list[i].group_match] += 1
    for j in range(1, GROUP_RANGE):
        count_array[j] += count_array[j - 1]
    i = n - 1
    while i >= 0:
        output_array[count_array[student_favorite_list[i].group_match] - 1] \
            = student_favorite_list[i]
        count_array[student_favorite_list[i].group_match] -= 1
        i -= 1
    for j in range(n):
        student_favorite_list[j] = output_array[j]
    return