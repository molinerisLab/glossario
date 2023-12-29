from django.db import models
from django.conf import settings

from moxutils.models import WithDateAndOwner
from django.db.models.signals import pre_save, post_save, m2m_changed
from .views import create_user_by_email, validate_simple_name

class Group(WithDateAndOwner):
    name = models.CharField(max_length=64, primary_key=True)
    code = models.SlugField(max_length=2, null=False, blank=False, default='GP')

    def __str__(self):
        return self.name

class Customer(WithDateAndOwner):
    #dati ottenuti dalla compilazione del form
    name = models.SlugField(null=True, blank=True)
    surname = models.SlugField(validators=(validate_simple_name,))
    email = models.EmailField(max_length=254, null=True, unique=True)
    user =  models.OneToOneField("auth.User",null=True, blank=True, on_delete=models.PROTECT,related_name='related_customer')
    group = models.ForeignKey(Group, null=False, blank=False, on_delete=models.CASCADE,related_name='related_group_customer')
    class Meta:
        ordering = ['surname',]

    def __str__(self):
        a=self.name
        if a:
            a=a[0]
        else:
            a=""

        return "%s%s" % (self.surname, a)

    def create_user(self):
        return create_user_by_email(self.email,is_staff=True,groups=[settings.CUSTOMER_DEFAULT_GROUP,])

def customer_create_and_set_user(sender, instance, **kwargs):
    if instance.user is None:
        post_save.disconnect(customer_create_and_set_user, sender=sender)
        user=instance.create_user()
        instance.user=user
        instance.save()
        post_save.connect(customer_create_and_set_user, sender=sender)
post_save.connect(customer_create_and_set_user, Customer)
