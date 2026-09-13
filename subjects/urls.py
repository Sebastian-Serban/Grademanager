from django.urls import path

from subjects.views import SubjectDetailView, SubjectListCreateView

urlpatterns = [
    path("", SubjectListCreateView.as_view, name="subject-list"),
    path("<int:pk>/", SubjectDetailView.as_view, name="subject-detail"),
]
