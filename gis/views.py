from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm

# Employee
def index(request):
    return render(request, 'employee/index.html')
def employee(request):
    return render(request, 'employee/employee.html')
def card(request):
    return render(request, 'employee/card.html')
def attendanceStudent(request):
    return render(request, 'employee/attendance_student.html')
def attendanceEmployee(request):
    return render(request, 'employee/attendance_employee.html')
def calender(request):
    return render(request, 'employee/calender.html')
def schedule(request):
    return render(request, 'employee/schedule.html')
def learning(request):
    return render(request, 'employee/learning.html')
def raport(request):
    return render(request, 'employee/raport.html')
def exam(request):
    return render(request, 'employee/exam.html')

# Student
def student(request):
    return render(request, 'student/student.html')
def studentCard(request):
    return render(request, 'student/student_card.html')
def studentCalender(request):
    return render(request, 'student/student_calender.html')
def studentSchedule(request):
    return render(request, 'student/student_schedule.html')
def studentLearning(request):
    return render(request, 'student/student_learning.html')
def studentRaport(request):
    return render(request, 'student/student_raport.html')
def studentExam(request):
    return render(request, 'student/student_exam.html')

# Parent
def parent(request):
    return render(request, 'parent/parent.html')
def calenderParent(request):
    return render(request, 'parent/calender_parent.html')
def scheduleParent(request):
    return render(request, 'parent/schedule_parent.html')
def parentAttendanceStudent(request):
    return render(request, 'parent/parent_attendance_student.html')
def Parentcard(request):
    return render(request, 'parent/parent_card.html')
def parentRaport(request):
    return render(request, 'parent/parent_raport.html')
def bookParental(request):
    return render(request, 'parent/book_parental.html')

def owner(request):
    return render(request, 'owner/owner.html')
def ownerAttendance(request):
    return render(request, 'owner/attendance.html')
def ownerCalendar(request):
    return render(request, 'owner/owner_calender.html')
def ownerPayment(request):
    return render(request, 'owner/payment.html')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/home/')
    else:
        form = LoginForm

    return render(request, 'registration/home.html')

def register(request):
    return render(request, 'registration/register.html')