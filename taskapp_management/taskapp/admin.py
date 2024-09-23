from django.contrib import admin
from .models import Importance_task,Task


class TaskAdmin(admin.ModelAdmin):
  list_display  = ('title','iportance_task','created_by')
  search_fields = ('title','created_by',)
  list_filter   = ('title','iportance_task','created_by')

class Importance_taskAdmin(admin.ModelAdmin):
  list_display  = ('importance',)

admin.site.register(Importance_task,Importance_taskAdmin)
admin.site.register(Task,TaskAdmin)