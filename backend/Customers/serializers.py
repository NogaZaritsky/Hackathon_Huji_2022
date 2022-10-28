from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('name', 'family_name', 'age', 'courses', 'home','study_year', 
        'preferred_study_locations','preferred_study_habits', 
        'preferred_study_group_size', 'weight_for_each_preference')