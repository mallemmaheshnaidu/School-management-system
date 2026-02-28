from django.db import models
from django.utils import timezone


class ClassRoom(models.Model):
	name = models.CharField(max_length=100)
	year = models.CharField(max_length=20, blank=True)

	def __str__(self):
		return f"{self.name} {self.year}" if self.year else self.name


class Subject(models.Model):
	name = models.CharField(max_length=100)
	code = models.CharField(max_length=20, blank=True)
	description = models.TextField(blank=True)

	def __str__(self):
		return self.name


class Book(models.Model):
	subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='books')
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=200, blank=True)
	link = models.URLField(blank=True)

	def __str__(self):
		return f"{self.title} ({self.subject})"


class Student(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	student_id = models.CharField(max_length=30, unique=True)
	email = models.EmailField(blank=True)
	dob = models.DateField(null=True, blank=True)
	classroom = models.ForeignKey(ClassRoom, on_delete=models.SET_NULL, null=True, blank=True, related_name='students')
	subjects = models.ManyToManyField(Subject, blank=True, related_name='students')

	def __str__(self):
		return f"{self.first_name} {self.last_name} ({self.student_id})"


class Attendance(models.Model):
	STATUS_CHOICES = [
		('present', 'Present'),
		('absent', 'Absent'),
		('late', 'Late'),
		('excused', 'Excused'),
	]

	student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendances')
	subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True)
	date = models.DateField(default=timezone.now)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='present')
	note = models.TextField(blank=True)

	class Meta:
		ordering = ['-date']

	def __str__(self):
		return f"{self.student} - {self.date} - {self.status}"


class Mark(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='marks')
	subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='marks')
	obtained = models.DecimalField(max_digits=6, decimal_places=2)
	total = models.DecimalField(max_digits=6, decimal_places=2, default=100)
	exam_date = models.DateField(default=timezone.now)
	remark = models.CharField(max_length=200, blank=True)

	class Meta:
		ordering = ['-exam_date']

	def percentage(self):
		try:
			return (self.obtained / self.total) * 100
		except Exception:
			return 0

	def __str__(self):
		return f"{self.student} - {self.subject}: {self.obtained}/{self.total}"
