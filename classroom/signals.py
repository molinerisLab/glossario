from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Student

#students can be defined before the user creation, in this case update de user field in the student,
#otherwise a proper studet is created on sing up
@receiver(post_save, sender=User)
def create_or_update_student(sender, instance, created, **kwargs):
    if created:
        student, _ = Student.objects.get_or_create(email=instance.email)
        student.user = instance
        student.save()


    def __str__(self):
        return self.name
