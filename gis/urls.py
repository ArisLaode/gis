from django.urls import path, include
from . import views

urlpatterns = [
    # employee
    path('', views.index, name='home'),
    path('employee', views.employee, name='employee'),
    path('card', views.card, name='card'),
    path('attendance/employee', views.attendanceEmployee, name='attendance_employee'),
    path('attendance/student', views.attendanceStudent, name='attendance_student'),
    path('book-parental', views.bookParental, name='book_parental'),
    path('calender', views.calender, name='calender'),
    path('schedule', views.schedule, name='schedule'),
    path('learning', views.learning, name='learning'),
    path('raport', views.raport, name='raport'),
    path('exam', views.exam, name='exam'),

    # Student
    path('student', views.student, name='student'),
    path('student/calender', views.studentCalender, name='student_calender'),
    path('student/schedule', views.studentSchedule, name='student_schedule'),
    path('student/card', views.studentCard, name='student_card'),
    path('student/learning', views.studentLearning, name='student_learning'),
    path('student/raport', views.studentRaport, name='student_raport'),
    path('student/exam', views.studentExam, name='student_exam'),

    # Parent
    path('parent', views.parent, name='parent'),
    path('parent/parent-calender', views.calenderParent, name='parent_calender'),
    path('parent/parent-schedule', views.scheduleParent, name='parent_schedule'),
    path('parent/attendance-student', views.parentAttendanceStudent, name='parent_attendance_student'),
    path('parent/parent-card', views.Parentcard, name='parent_card'),
    path('parent/parent-raport', views.parentRaport, name='parent_raport'),

    # Owner
    path('owner', views.owner, name='owner'),
    path('owner/owner-calendar', views.ownerCalendar, name='owner_calendar'),
    path('owner/owner-attendance', views.ownerAttendance, name='owner_attendance'),
    path('owner/owner-payment', views.ownerPayment, name='owner_payment'),


    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
]