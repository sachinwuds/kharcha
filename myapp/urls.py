from django.urls import path
from .views import *

urlpatterns = [
    path('',   ExpensesView.as_view(),  name="check")
]