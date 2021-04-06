from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    phone_no = models.CharField(max_length=50)
    room_no = models.CharField(max_length=10)
    
    profile_pic = models.TextField(max_length=300)
    subjects_taught = models.CharField(max_length=300)

    class Meta:
        ordering = ['first_name', 'last_name']