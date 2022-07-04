from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

# Create your models here

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to = 'avatars/', blank = True)
    about = models.TextField()

    def __str__(self):
        return self.user.username

class Gigs(models.Model):
    CATETORY_CHOICES = [
        ('PC', 'Pest Control'),
        ('HC', 'Home Cleaners'),
        ('GL', 'Gardening and Landscaping'),
        ('LS', 'LockSmith'),
        ('EL', 'Electricians'),
        ('PL', 'Plumbing'),
        ('MO', 'Moving'),
        ('CO', 'Contractors'),
        ('OT', 'Others'),
    ]
    title = models.CharField(max_length=100, default='', blank=False)
    category = models.CharField(max_length=2, choices=CATETORY_CHOICES)
    description = models.TextField()
    status = models.BooleanField(default=True)
    picture = models.ImageField(upload_to = 'gigPics/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    phoneNumber = models.CharField(max_length=10)
    email = models.EmailField(max_length=254)
    address = models.TextField()

    def __str__(self):
        return self.title

class Reviews(models.Model):
    RATING_CHOICES = [
        ('1', 'Very Poor'),
        ('2', 'Poor'),
        ('3', 'Average'),
        ('4', 'Good'),
        ('5', 'Excellent')
    ]
    gig = models.ForeignKey(Gigs, on_delete=models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE)
    rating = models.CharField(max_length=1, choices=RATING_CHOICES)
    content = models.TextField()

    def __str__(self):
        return self.content