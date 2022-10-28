

# Create your models here.
from django.db import models


#TODO add restrictions
class Customer(models.Model):
    name = models.CharField(max_length=100)
    family_name = models.CharField(max_length=100)
    age = models.IntegerField()
    courses = models.CharField(max_length=200)
    home = models.IntegerField()
    study_year = models.IntegerField()
    preferred_study_locations = models.CharField(max_length=200)
    preferred_study_habits = models.CharField(max_length=200)
    preferred_study_group_size = models.IntegerField() 
    weight_for_each_preference = models.CharField(max_length=200)
    
    def _str_(self):
        return self.name