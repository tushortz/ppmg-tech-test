from teacher.models import Subject, Teacher
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class Index(LoginRequiredMixin, ListView):
    template_name = "teacher/index.html"
    context_object_name = "teachers"
    model = Teacher
    paginate_by = 25


class TeacherDetail(LoginRequiredMixin, DetailView):
    template_name = "teacher/detail.html"
    context_object_name = "teacher"
    model = Teacher


class TeacherListBySubject(LoginRequiredMixin, ListView):
    template_name = "teacher/index.html"
    context_object_name = "teachers"
    model = Teacher
    paginate_by = 25

    def get_queryset(self):
        subject = self.kwargs["subject"].strip()
        return self.model.objects.filter(subjects_taught__name__in=subject.split(","))