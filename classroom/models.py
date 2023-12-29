from django.db import models
from django.contrib.auth.models import User
from moxutils.models import WithDateAndOwner

class Teacher(WithDateAndOwner):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    email = models.EmailField(unique=True)
    # Aggiungi altri campi specifici del docente, come titolo, dipartimento, ecc.

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(unique=True)
    # Aggiungi altri campi specifici dello studente

    def __str__(self):
        return self.user.username if self.user else self.email

class Course(WithDateAndOwner):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name
