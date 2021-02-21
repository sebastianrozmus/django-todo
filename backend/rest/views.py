from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest.serializers import TodoSerializer, CategorySerializer
from rest.models import Todo, Category
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

class CategoryList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        category = Category.objects.filter(useruid = self.request.user.id)
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        request.data['useruid'] = self.request.user.id
        serializer = CategorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()   
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class TodoList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        todos = Todo.objects.filter(useruid = self.request.user.id)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        request.data['useruid'] = self.request.user.id
        serializer = TodoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()   
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class TodoDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Todo.objects.get(id=pk, useruid=self.request.user.id)
        except ObjectDoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        todo = self.get_object(pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        todo = self.get_object(pk)
        request.data['useruid'] = self.request.user.id
        serializer = TodoSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            if self.request.user.id == todo.useruid:
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        todo = self.get_object(pk)
        try:
            if self.request.user.id == todo.useruid:
                todo.delete()
                return Response(status = status.HTTP_204_NO_CONTENT)
        except:
            return Response(data = {"error" : "Wrong"},status = status.HTTP_400_BAD_REQUEST)
        return Response(data = {"error" : "Wrong"},status = status.HTTP_400_BAD_REQUEST)
