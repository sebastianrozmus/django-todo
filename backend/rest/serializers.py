from rest_framework import serializers
from rest.models import Todo, Category

class TodoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Todo
		fields = ['id', 'title', 'content', 'due_date', 'category', 'is_complete', 'useruid']

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ['id', 'name', 'useruid']
