from django.utils import timezone
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Property (models.Model):
    owner = models.ForeignKey(User, related_name='property_owner', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property/images/')
    title = models.CharField(max_length=30, verbose_name='Title', unique=True)
    description = models.TextField(max_length=10000, verbose_name='Text')
    price = models.DecimalField(max_digits=19,decimal_places=2, verbose_name='Price')
    place = models.ForeignKey('Place',related_name='property_place', on_delete=models.CASCADE)
    category = models.ForeignKey('Category',related_name='property_category', on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True,
                            editable=False, allow_unicode=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta :
        ordering = ['-id']
        verbose_name_plural = 'Properties'

    def get_absolute_url(self):
        return reverse('property:property_detail' , args={self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Property, self).save(*args, **kwargs)

    def check_availability(self):
        Availability = self.book_property.all()
        now = timezone.now().date()
        for reservation in Availability:
            if now > reservation.end_date:
                return 'Available'
                
            elif now > reservation.start_date and now < reservation.end_date:
                time = reservation.end_date
                return f'Not Available To ({time})'
        else:
            return 'Available'

    def check_rating(self):
        ratings = self.property_reviews.all()
        if ratings:
            return round(sum(r.rating for r in ratings) / len(ratings),2)
        else:
            return 0

    def __str__(self):
        return self.title


# Create Property Images
class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='property_image', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property/images/')
    
    class Meta :
            ordering = ['-id']
            verbose_name_plural = 'Property Image'

    def __str__(self):
        return self.property.title


# Create Property Place
class Place (models.Model):
    image = models.ImageField(upload_to='Place/images/')
    title = models.CharField(max_length=30, verbose_name='Title')

    #Metadata
    class Meta :
        ordering = ['-id']
        verbose_name_plural = 'Places'

    def __str__(self):
        return self.title



# Create Property Category
class Category (models.Model):
    title = models.CharField(max_length=30, verbose_name='Title')

    #Metadata
    class Meta :
        ordering = ['-id']
        verbose_name_plural = 'category"s'

    def __str__(self):
        return self.title




# Create Property Review
class PropertyReview(models.Model):
    user = models.ForeignKey(User, related_name='user_reviews', on_delete=models.CASCADE)
    property = models.ForeignKey(Property, related_name='property_reviews', on_delete=models.CASCADE)
    review = models.TextField(max_length=500, verbose_name='Text')
    rating = models.IntegerField(default=0, verbose_name='Rating', validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta :
        verbose_name_plural = 'Property Review"s'  

    def __str__(self):
        return self.property.title


PEOPLE_TYPE = (
    (1,1),
    (2,2),
    (3,3),
    (4,4)
)

# Create Property Booking
class PropertyBook (models.Model):
    users = models.ForeignKey(User, related_name='book_user', on_delete=models.CASCADE)
    property = models.ForeignKey(Property, related_name='book_property', on_delete=models.CASCADE)
    start_date = models.DateField(default=timezone.now,verbose_name='Start Date')
    end_date = models.DateField(default=timezone.now,verbose_name='End Date')
    guest = models.IntegerField(default=1 , choices=PEOPLE_TYPE)
    children = models.IntegerField(default=0 , choices=PEOPLE_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta :
        ordering = ['-id']

    def in_progress(self):
        now = timezone.now().date()
        return now > self.start_date and now < self.end_date

    in_progress.boolean = True

    def __str__(self):
        return str(self.property)