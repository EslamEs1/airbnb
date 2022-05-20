from django.db import models


# Create your models here.
class About(models.Model):
    image = models.ImageField(upload_to='about/')
    vision = models.TextField(max_length=10000, verbose_name='what_we_do')
    mission = models.TextField(max_length=10000, verbose_name='our_mission')
    goals = models.TextField(max_length=10000, verbose_name='our_goal')

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'About'

    def __str__(self):
        return 'About'


class FAQ(models.Model):
    title = models.CharField(max_length=60, verbose_name='Title')
    Description = models.TextField(max_length=1000, verbose_name='Description')

    class Meta:
      verbose_name = 'FAQ'
      verbose_name_plural = 'FAQ'

    def __str__(self):
      return self.title
