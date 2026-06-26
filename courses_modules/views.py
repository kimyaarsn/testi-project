from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpRequest
from .forms import CourseCommentForm
from .models import Course, CourseCategory, CourseComment , Instructor
from django.views.generic import ListView, DetailView
from django.db.models import Q

# Create your views here.

class CourseListView(ListView):
    model = Course
    template_name = 'courses_modules/course_list.html'
    context_object_name = 'courses'
    paginate_by = 6

    def get_queryset(self):
        queryset = (
            Course.objects.filter(
                is_active=True,
                is_delete=False
            )
            .select_related(
                'category',
                'instructor'
            )
            .prefetch_related(
                'course_tag',
                'suggested_courses'
            )
        )

        # فیلتر دسته بندی
        category = self.kwargs.get('category')

        if category:
            queryset = queryset.filter(
                category__url_title__iexact=category
            )

        # جستجو
        search = self.request.GET.get('q')

        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) |
                Q(short_description__icontains=search) |
                Q(description__icontains=search)
            )

        return queryset

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses_modules/course_details.html'
    context_object_name = 'course'

    def get_queryset(self):
        return Course.objects.filter(
            is_active=True,
            is_delete=False
        ).select_related(
            'category',
            'instructor'
        ).prefetch_related(
            'course_tag',
            'suggested_courses',
            'comments'
        )

    def get_object(self, queryset=None):
        return get_object_or_404(
            Course,
            url_title=self.kwargs.get('url_title'),
            is_active=True,
            is_delete=False
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['categories'] = CourseCategory.objects.filter(
            is_active=True,
            is_delete=False
        )

        context['form'] = CourseCommentForm()

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        form = CourseCommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)

            comment.course = self.object

            if request.user.is_authenticated:
                comment.user = request.user

            comment.save()

            return redirect(self.object.get_absolute_url())

        context = self.get_context_data()
        context['form'] = form

        return self.render_to_response(context)

def course_categories_component(request):
    categories = CourseCategory.objects.filter(is_active=True,is_delete=False)

    return render(request, 'courses_modules/includes/course_categories.html', {'categories': categories})


class InstructorListView(ListView):
    model = Instructor
    template_name = 'courses_modules/instructor_list.html'
    context_object_name = 'instructors'

    def get_queryset(self):
        return Instructor.objects.filter(
            is_active=True
        ).annotate(
            total_students=Coalesce(
                Sum('courses__students_count'),
                0
            )
        )

class InstructorDetailView(DetailView):
    model = Instructor
    template_name = 'courses_modules/instructor_dateil.html'
    context_object_name = 'instructor'

    def get_object(self, queryset=None):
        return Instructor.objects.get(
            id=self.kwargs.get('id'),
            is_active=True
        )

