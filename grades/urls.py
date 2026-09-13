from django.urls import path

from grades.views import GradeDetailView, GradeListCreateView

urlpatterns = [
    path("", GradeListCreateView.as_view(), name="grade-list"),
    path("<int:pk>/", GradeDetailView.as_view(), name="grade-detail"),
]
