from django.urls import path
from teacher import views as teacher_view


app_name = "teacher"

urlpatterns = [
    path('subject/<slug:subject>', view=teacher_view.TeacherListBySubject.as_view(), name='list-by-subject'),
    path('<int:pk>', view=teacher_view.TeacherDetail.as_view(), name='detail'),
    path('', view=teacher_view.Index.as_view(), name='index'),
]
