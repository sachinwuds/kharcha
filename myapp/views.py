from multiprocessing import managers
from operator import imod
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import ExpensesSerializer
from .models import  Expenses
# Create your views here.
# from rest_framework import ModelViewSet

class ExpensesView(APIView):
    permission_classes = (AllowAny,)
    """
        List All expenses Or Create a new Expense
    """

    def post(self, request, format=None):
        serializer = ExpensesSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        instance = Expenses.objects.all()
        serializer = ExpensesSerializer(instance,many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
