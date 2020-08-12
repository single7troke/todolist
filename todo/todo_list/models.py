from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxLengthValidator


class ToDo(models.Model):
	content = models.CharField(max_length=255)
	date = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	complete = models.BooleanField(default=False)

	def __str__(self):
		return f'{self.author} - {self.content}'
