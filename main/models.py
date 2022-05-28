from django.db import models

# Create your models here.

class Website (models.Model):
    site_name = models.CharField(max_length=30, verbose_name='Site Name')
    logo = models.ImageField(upload_to='logo', verbose_name='Logo')
    description = models.TextField(verbose_name='Description', max_length=500)
    address = models.CharField(verbose_name='Address', max_length=50)
    phone = models.CharField(verbose_name='Phone', max_length=20)
    email = models.EmailField(verbose_name='Email', max_length=50)
    facebook = models.URLField(verbose_name='Facebook', max_length=50 , blank=True, null=True)
    twitter = models.URLField(verbose_name='Twitter', max_length=50 , blank=True, null=True)
    instagram = models.URLField(verbose_name='Instagram', max_length=50 , blank=True, null=True)

    class Meta :
        verbose_name_plural = 'Website'

    def __str__(self):
        return self.site_name



class Contact (models.Model):
    name = models.CharField(max_length=30, verbose_name='Name')
    email = models.EmailField(verbose_name='Email', max_length=50)
    subject = models.CharField(verbose_name='Subject', max_length=50)
    message = models.TextField(verbose_name='Message', max_length=500)

    #Metadata
    class Meta :
        ordering = ['-id']
        verbose_name_plural = 'Contact'

    def __str__(self):
        return self.name

