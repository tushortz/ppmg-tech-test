from django.urls import path
from home import views as home_view
from django.contrib.auth.views import LoginView


app_name = "home"

urlpatterns = [
    path('login/', view=LoginView.as_view(), name='login'),
    path('', view=home_view.Index.as_view(), name='index'),
]
