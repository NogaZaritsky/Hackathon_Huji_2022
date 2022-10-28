import re
import logging
from django.shortcuts import render
from Customers.algo import main_func
from .serializers import CustomerSerializer
from rest_framework import viewsets
from .models import Customer
from django.http import HttpResponse
import datetime
from .management.commands.Student import Student
import json


class CustomerView(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


def funk_tion(request):
    list_students = []
    string_all_names = ""
    for customer_callable in Customer.objects.all():
        student = Student.Student(customer_callable)
        string_all_names += customer_callable.name+"<br></br>"
        list_students.append(student)
    now = datetime.datetime.now()
    html = f"<html><body>It is now %s.<br></br>{string_all_names}</body></html>" % now
    return HttpResponse(html)


def make_match(request):
    # print(request.GET.get('want_match',2))
    want_match = int(request.GET.get('want_match', 2))
    users_list = []
    for customer_callable in Customer.objects.all():
        users_list.append(customer_callable)
    student_favorite_list = main_func(users_list)

    for list_user in student_favorite_list:
        if list_user[0] == want_match:
            result = {}
            for user_id in list_user[1:]:
                user = Student(Customer.objects.get(id=user_id))
                result[user_id] = [user.name, user.family_name]
            return HttpResponse(json.dumps(result))
    return HttpResponse('')


def meeting_happiness(request):
    pass


def student_to_json(student: Student) -> list:
    pass


# def match_request(request):
#     if request.method == "GET":
#         user = request.GET.get('name')
#     return JsonResponse("Success match!", safe=False)
