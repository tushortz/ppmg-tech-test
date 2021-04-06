from django.db import models, OperationalError

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    phone_no = models.CharField(max_length=50)
    room_no = models.CharField(max_length=10)
    
    profile_pic = models.CharField(max_length=300)
    subjects_taught = models.ManyToManyField('teacher.Subject')

    class Meta:
        ordering = ['first_name', 'last_name']

    def str(self):
        return f"{self.last_name} {self.first_name}"
        
    def save(self, *args, **kwargs):
        if self.id and self.subjects_taught.count() > 5:
            raise OperationalError("Subjects taught cannot be more than 5")
        return super().save(*args, **kwargs)

class Subject(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']