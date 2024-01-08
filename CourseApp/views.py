from django.shortcuts import render,redirect
from CourseApp.models import course
from CourseApp.models import student

def home(request):
    return render(request,'home.html')

def courses(request):
    return render(request,'course.html')

def course_submission(request):
    if request.method == 'POST':
        coursename = request.POST['cname']
        coursefee = request.POST['cfee']
        crs = course(course_name = coursename,course_fee = coursefee)
        crs.save()
        return render(request,'student.html')
    
def students(request):
    courses = course.objects.all()
    return render(request,'student.html',{'crs':courses})

def registration(request):
    if request.method == 'POST':
        name = request.POST['sname']
        mail = request.POST['smail']
        age = request.POST['sage']
        date = request.POST['sdate']
        courses = request.POST['sselect']
        crs = course.objects.get(id=courses)
        std = student(student_name=name,student_age=age,student_email=mail,student_date=date,student_course=crs)
        std.save()
        return redirect('details')

def details(request):
    stud = student.objects.all()
    return render(request,'details.html',{'std':stud})

def delete(request,pk):
    dele = student.objects.get(id=pk)
    dele.delete()
    return redirect('details')

def edit(request,pk):
    edt = student.objects.get(id=pk)
    crss = course.objects.all()
    return render(request,'edit.html',{'std':edt,'crs':crss})

def updation(request,pk):
    if request.method == 'POST':
        std = student.objects.get(id=pk)
        crs = course.objects.all()
        std.student_name= request.POST['sname']
        std.student_age = request.POST['sage']
        std.student_email = request.POST['smail']
        std.student_date = request.POST['sdate']
        sel = request.POST['sselect']
        crs = course.objects.get(id=sel)
        std.student_course = crs
        std.save()
        return redirect('details')
        
    
