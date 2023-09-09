from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .serializers import TodoSerializer, TodoToggleCompleteSerializer
from todo.models import Todo


class TodoListCreate(generics.ListCreateAPIView):
    # queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user).order_by('-created')


class TodoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)



    

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TodoToggleComplete(generics.UpdateAPIView):
    # queryset = Todo.objects.all()
    serializer_class = TodoToggleCompleteSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)


    def perform_update(self, serializer):
        serializer.instance.completed = not serializer.instance.completed
        serializer.save()
