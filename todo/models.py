from django.db import models

class todo(models.Model):
	todo_item = models.CharField(max_length=1200)
