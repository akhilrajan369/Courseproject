from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('courses',views.courses,name='courses'),
    path('course_submission',views.course_submission,name='course_submission'),
    path('students',views.students,name='students'),
    path('registration',views.registration,name='registration'),
    path('details',views.details,name='details'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('updation/<int:pk>',views.updation,name='updation'),
    
]
