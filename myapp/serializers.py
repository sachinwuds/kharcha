
from django.forms import models
from .models import Expenses

from rest_framework import serializers

class ExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields = '__all__'