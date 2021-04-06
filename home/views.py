from django.http.response import HttpResponseRedirect
from django.views.generic.base import TemplateView
from teacher.models import Subject
from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

class Index(LoginRequiredMixin, ListView):
    template_name = "home/index.html"
    context_object_name = "subjects"
    queryset = Subject.objects.all()
    paginate_by = 20


class BulkUpload(UserPassesTestMixin, TemplateView):
    template_name = "home/bulk_upload.html"

    def post(self, request, *args, **kwargs):
        
        

        return render(request, self.template_name)


    def dispatch(self, request, *args, **kwargs):
        user_test_result = self.request.user.is_superuser

        if not user_test_result:
            return HttpResponseRedirect(reverse_lazy('home:index'))
        return super().dispatch(request, *args, **kwargs)

    def test_func(self):
        return self.request.user.is_superuser