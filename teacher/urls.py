from django.urls import path, re_path
from teacher import views as teacher_view


app_name = "teacher"

urlpatterns = [
    re_path(r'subject/(?P<subject>[-a-zA-Z0-9_\s]+)$', view=teacher_view.TeacherListBySubject.as_view(), name='list-by-subject'),
    path('<int:pk>', view=teacher_view.TeacherDetail.as_view(), name='detail'),
    path('', view=teacher_view.Index.as_view(), name='index'),
]
