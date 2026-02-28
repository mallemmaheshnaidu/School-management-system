from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Student, Attendance, Mark, Subject, Book


class StudentListView(ListView):
	model = Student
	template_name = 'school/student_list.html'
	context_object_name = 'students'
	paginate_by = 20


class StudentDetailView(DetailView):
	model = Student
	template_name = 'school/student_detail.html'
	context_object_name = 'student'

	def get_context_data(self, **kwargs):
		ctx = super().get_context_data(**kwargs)
		student = self.get_object()
		ctx['attendances'] = student.attendances.all()[:50]
		ctx['marks'] = student.marks.select_related('subject').all()[:50]
		ctx['subjects'] = student.subjects.all()
		# books grouped by subject
		books = Book.objects.filter(subject__in=ctx['subjects']).select_related('subject')
		grouped = {}
		for b in books:
			grouped.setdefault(b.subject, []).append(b)
		ctx['books_by_subject'] = grouped
		# compute skipped classes per subject
		skipped = {}
		for subject in ctx['subjects']:
			skipped_count = student.attendances.filter(subject=subject, status='absent').count()
			skipped[subject] = skipped_count
		ctx['skipped'] = skipped
		return ctx


# simple page views for dashboard and informational pages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


@login_required
def dashboard(request):
	# counts for overview table
	student_count = Student.objects.count()
	subject_count = Subject.objects.count()
	book_count = Book.objects.count()
	attendance_count = Attendance.objects.count()
	mark_count = Mark.objects.count()
	return render(request, 'school/dashboard.html', {
		'student_count': student_count,
		'subject_count': subject_count,
		'book_count': book_count,
		'attendance_count': attendance_count,
		'mark_count': mark_count,
	})


def about(request):
	return render(request, 'school/about.html')


def contact(request):
	return render(request, 'school/contact.html')


def reviews(request):
	return render(request, 'school/reviews.html')

