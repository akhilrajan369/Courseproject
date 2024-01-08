from django.db import models

class course(models.Model):
    course_name = models.CharField(max_length=50)
    course_fee = models.IntegerField()
    
class student(models.Model):
    student_course = models.ForeignKey(course,on_delete=models.CASCADE)
    student_name = models.CharField(max_length=50)
    student_age = models.IntegerField()
    student_email = models.EmailField(null=True)
    student_date = models.DateField()

