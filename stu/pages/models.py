from django.db import models
from django.utils import timezone

# Tasks:--------------
# Due Date
# label   =   'Personal’, ‘Work’, ‘Shopping’ and ‘Others’.
# Status  =  ‘New’, ‘In progress’ and ‘Completed’. 

# archive completed tasks

class TodoList(models.Model):
    title    = models.CharField(max_length=150)
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    label    = models.CharField(max_length = 10,default='Others')
    status   = models.CharField(max_length = 10,default='New')

    def __str__(self):
        return self.title
