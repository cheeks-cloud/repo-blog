from sys import setprofile
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save 
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.core.exceptions import ObjectDoesNotExist

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

# Create your models here.

class Projects(models.Model):
    title = models.CharField(max_length=30)
    image= models.ImageField(upload_to='images/')
    description = models.TextField()
    link= models.URLField(max_length = 200)
    owner = models.ForeignKey('auth.User', related_name='projects', on_delete=models.CASCADE,blank=True, null=True,)
    created = models.DateTimeField(auto_now_add=True)

    def save_repo(self):
       self.save()

    def __str__(self):
      return self.title
class Profile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    projects = models.ForeignKey(Projects, on_delete=models.CASCADE,blank=True, null=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        try:
          instance.profile.save()
        except ObjectDoesNotExist:
          Profile.objects.create(user=instance)

    @receiver(post_save, sender=User) 
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
   

class Review(models.Model):
    CHOICES1 = [
        ('Excellent', 'Excellent'),
        ('Good', 'Good'),
        ('Average', 'Average'),
        ('Not Good', 'Not Good'),      
    ]
    design= models.CharField( choices=CHOICES1, max_length=30)

    CHOICES = [
        ('Excellent', 'Excellent'),
        ('Good', 'Good'),
        ('Average', 'Average'),
        ('Not Good', 'Not Good'),      
    ]
    usability = models.CharField( choices=CHOICES, max_length=30)
    project_on_review = models.ForeignKey(Projects,on_delete=models.CASCADE)
    content = models.TextField()
    
    def save_review(self):
       self.save()

    def __str__(self):
      return self.content