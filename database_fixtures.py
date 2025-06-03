from Students.models import Faculty,Groups, Student
from Staffs.models import Staff
from Courses.models import Course, Enrollment
from Books.models import Book, BookLoan
from Exams.models import Exam, ExamResult
from ClassSchedule.models import ClassSchedule
from datetime import date, time

# Fakultetlar
ict = Faculty.objects.create(name="Informatika", description="IT va dasturlash")
eco = Faculty.objects.create(name="Iqtisodiyot", description="Iqtisodiy fanlar")
# Groups
ab_218 = Groups.objects.create(name="AB-218", description="Logistika",faculty=ict)
em_205 = Groups.objects.create(name="EM-205", description="Energitika",faculty=eco)

# Talabalar
sanjar = Student.objects.create(
    first_name="Sanjar", last_name="Aliyev",
    birth_date=date(2002, 5, 14),
    email="sanjar@uni.uz", phone="998901234567",
    group=ab_218, enrollment_year=2020
)
dilnoza = Student.objects.create(
    first_name="Dilnoza", last_name="Karimova",
    birth_date=date(2001, 3, 22),
    email="dilnoza@uni.uz", phone="998939876543",
    group=em_205, enrollment_year=2019
)

# Professorlar
akmal = Staff.objects.create(
    first_name="Akmal", last_name="Qodirov",
    email="akmal@uni.uz", phone="998901111111",
    role="professor", department="Informatika"
)
gulbahor = Staff.objects.create(
    first_name="Gulbahor", last_name="Toshpulatova",
    email="gulbahor@uni.uz", phone="998902222222",
    role="professor", department="Iqtisodiyot"
)

# Kurslar
python_course = Course.objects.create(
    name="Python Dasturlash", code="CS101",
    description="Django va Python asoslari",
    credits=4, semester=2, teacher=akmal
)
economics = Course.objects.create(
    name="Mikroiqtisodiyot", code="EC201",
    description="Iqtisodiy nazariya", credits=3,
    semester=3, teacher=gulbahor
)

# Kursga yozilish
Enrollment.objects.create(student=sanjar, course=python_course, grade=95.0)
Enrollment.objects.create(student=dilnoza, course=economics, grade=88.0)

# Kutubxona kitoblari
book1 = Book.objects.create(
    title="Python for Beginners", author="Mark Lutz",
    isbn="1234567890123", published_year=2015,
    available_copies=3
)
book2 = Book.objects.create(
    title="Basic Economics", author="Thomas Sowell",
    isbn="1234567890124", published_year=2011,
    available_copies=2
)

# Kitob olish
BookLoan.objects.create(student=sanjar, book=book1)
BookLoan.objects.create(student=dilnoza, book=book2)

# Imtihonlar
exam1 = Exam.objects.create(
    course=python_course, exam_date=date(2024, 12, 1),
    duration_minutes=90, total_marks=100
)
exam2 = Exam.objects.create(
    course=economics, exam_date=date(2024, 12, 5),
    duration_minutes=60, total_marks=100
)

# Imtihon natijalari
ExamResult.objects.create(exam=exam1, student=sanjar, score=91.5)
ExamResult.objects.create(exam=exam2, student=dilnoza, score=86.0)

# Dars jadvali
ClassSchedule.objects.create(
    course=python_course, day_of_week='Mon',
    start_time=time(9, 0), end_time=time(10, 30), room='A101'
)
ClassSchedule.objects.create(
    course=economics, day_of_week='Wed',
    start_time=time(13, 0), end_time=time(14, 30), room='B202'
)
