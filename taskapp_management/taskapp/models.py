from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError
from datetime import date


class  Importance_task (models.Model):
  importance = models.CharField(max_length=50,null=False)
  importance_value = models.IntegerField(default=1,null=False)
  def __str__(self):
      return self.importance
  

class Task (models.Model):
  title = models.CharField(max_length=50 , null=False)
  description = models.TextField(blank=True)
  created_by = models.ForeignKey(User , on_delete=models.CASCADE , null=False)
  iportance_task = models.ForeignKey(Importance_task , on_delete=models.CASCADE , null=False)
  create_task  = models.DateField(null=True , blank=False , default=timezone.now)
  completation_date = models.DateField(null=True , blank=True)
  completed = models.BooleanField(default=False)  
  limit_date = models.DateField(null=True , blank=True)

  def clean(self):
    if self.limit_date is not None and self.limit_date < date.today():
      raise ValidationError("Limit cannot be in the past.")

  def __str__(self):
    return self.title
