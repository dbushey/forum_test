from django.db import models
from django.utils import timezone


class Thread (models.Model):
	#author = models.ForeignKey('auth.User')
	subject = models.CharField(max_length=200)

	def __str__(self):
		return self.subject


class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
	        default=timezone.now)
	last_edited_date = models.DateTimeField(
	        auto_now=True)
	thread = models.ForeignKey(Thread)


	def __str__(self):
	    return self.title