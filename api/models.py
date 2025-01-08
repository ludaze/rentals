from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = 'username'

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',  # Use a unique related_name
        blank=True,
        help_text='The groups this user belongs to.'
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  # Use a unique related_name
        blank=True,
        help_text='Specific permissions for this user.'
    )
    
    def __str__(self):
        return self.username
    
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10, unique=True)
    verification_document = models.ImageField(upload_to='id_images')
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name
    
def create_user_profile(sender,instance,created,**kwawrgs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=CustomUser)
post_save.connect(save_user_profile, sender=CustomUser)

