from django.db import models
from django.utils import timezone

class Category(models.Model):
	name = models.CharField(max_length=100) 
	useruid = models.IntegerField(blank=True, null=True, default=0)

	class Meta:
		verbose_name = ("Category")
		verbose_name_plural = ("Categories")

	def __str__(self):
		return self.name 

class Todo(models.Model): 
	title = models.CharField(max_length=250) 
	content = models.TextField(blank=True) 
	created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) 
	due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
	category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True) 
	is_complete = models.BooleanField(default=False)	
	useruid = models.IntegerField(blank=True, null=True, default=0)

	class Meta:
		verbose_name = ("TODO")
		verbose_name_plural = ("TODOS")
		ordering = ["-created"] 

	def __str__(self):
		return f'{self.title} [{self.is_complete}]'