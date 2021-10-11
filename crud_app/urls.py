from django.urls import path

from . import views


urlpatterns = [

    path('',views.home,name='home'),
    path('crud_app/register',views.register,name='register'),
    path('crud_app/login',views.login,name='login'),
    path('task_view',views.task_view,name='task_view'),
    path('crud_app/logout',views.logout,name='logout'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),

    ]
