from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category, Expenses, Users
from .Serializer import UserSerializer, CategorySerializer


def home(request):
    return HttpResponse('working....')

class UsersApi(APIView):
    def get(self, request):
        users = Users.objects.all()
        serializedUser=UserSerializer(users,many=True)

        return Response(serializedUser.data,status=200)

    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def delete(self, request, user_id):
        user = Users.objects.filter(user_id=user_id).first()

        if not user:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        user.delete()
        return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, user_id):
        user = Users.objects.filter(user_id=user_id).first()

        if not user:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        data = request.data
        serializer = UserSerializer(instance=user, data=data,partial=True)  # Pass the existing user instance
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class CategoryApi(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serialized_category = CategorySerializer(categories, many=True)
        return Response(serialized_category.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, category_id):
        category = Category.objects.filter(category_id=category_id).first()

        if not category:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

        category.delete()
        return Response({'message': 'Category deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, category_id):
        category = Category.objects.filter(category_id=category_id).first()

        if not category:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

        data = request.data
        serializer = CategorySerializer(instance=category, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)