from teacher.models import Subject
from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


class Index(LoginRequiredMixin, ListView):
    template_name = "home/index.html"
    context_object_name = "subjects"
    queryset = Subject.objects.all()
    paginate_by = 20
