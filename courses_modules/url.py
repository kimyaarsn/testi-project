from django.urls import path

from .views import CourseListView, CourseDetailView,InstructorListView,InstructorDetailView

urlpatterns = [
    path('', CourseListView.as_view(), name='course_list'),
    path('instructors/',InstructorListView.as_view(),name='instructors_list'),
    path(
        'course/<str:url_title>/', CourseDetailView.as_view(), name='course_detail'),
    path(
    'category/<str:category>/',CourseListView.as_view(),name='course_category'),
    path('instructor/<int:id>/',InstructorDetailView.as_view(),name='instructor_detail')
]