
from django.urls import path
from . import views

urlpatterns  =  [
    path('',views.task_list,name='task_list'),
    path('form/',views.task_form,name='task_form'),
    path('list/<str:order>/<str:taskfilter>/',views.task_list),
    path('update/<int:task_id>/',views.task_update,name='task_update'),
    path('delete/<int:task_id>/',views.task_delete,name='task_delete'),
    path('complete/<int:task_id>/', views.task_complete,name='task_complete'),
    path('incomplete/<int:task_id>/', views.task_incomplete,name='task_incomplete'),
]
