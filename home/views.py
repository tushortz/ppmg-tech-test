from django.http.response import HttpResponseRedirect
from django.views.generic.base import TemplateView
from teacher.models import Subject, Teacher
from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
import csv


class Index(LoginRequiredMixin, ListView):
    template_name = "home/index.html"
    context_object_name = "subjects"
    queryset = Subject.objects.all()
    paginate_by = 20


class BulkUpload(UserPassesTestMixin, TemplateView):
    template_name = "home/bulk_upload.html"

    def post(self, request, *args, **kwargs):
        subject_models = []
        data_to_save = []
        _subject_filter = set()

        # process uploaded file
        csv_file = request.FILES.get("file")
        csv_file = csv_file.read().decode('utf-8').splitlines()

        rows = csv.DictReader(csv_file)

        for row in rows:
            first_name = row.get("First Name")
            last_name = row.get("Last Name")
            email = row.get("Email Address")

            # check if we have required fields before processing. saves unnecessary processing
            if (first_name and last_name and email):
                profile_pic = row.get("Profile picture")
                phone_no = row.get("Phone Number")
                room_no = row.get("Room Number")
                subjects = [s.strip() for s in row.get("Subjects taught", '').lower().split(",")]

                for subject in subjects:
                    if subject == "maths":
                        subject = "mathematics"

                    if subject and not subject in _subject_filter: 
                        subject_models.append(Subject(name=subject))
                        _subject_filter.add(subject)

                data_to_save.append(
                    {
                        "first_name": first_name, 
                        "last_name": last_name, 
                        "profile_pic": profile_pic, 
                        "email": email, 
                        "phone_no": phone_no,
                        "room_no": room_no,
                        "subjects_taught": subjects[:5] # max item to save is 5
                    })

        Subject.objects.bulk_create(subject_models, ignore_conflicts=True)
        all_subjects = Subject.objects.all()

        for data in data_to_save:
            subjects_taught = all_subjects.filter(name__in=data["subjects_taught"])

            t, _ = Teacher.objects.get_or_create(
                email=data["email"],
                defaults={
                    "first_name": data["first_name"],
                    "last_name": data["last_name"],
                    "phone_no": data["phone_no"],
                    "room_no": data["room_no"],
                    "profile_pic": data["profile_pic"],
                }
            )
            t.subjects_taught.set(subjects_taught)


        return HttpResponseRedirect(reverse_lazy('teacher:index'))


    def dispatch(self, request, *args, **kwargs):
        user_test_result = self.request.user.is_superuser

        if not user_test_result:
            return HttpResponseRedirect(reverse_lazy('home:index'))
        return super().dispatch(request, *args, **kwargs)

    def test_func(self):
        return self.request.user.is_superuser