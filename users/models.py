from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    about_text = models.TextField(
        blank=True, max_length=50,  verbose_name='About', null=True, default='Hi There')
    phone = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def created(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
