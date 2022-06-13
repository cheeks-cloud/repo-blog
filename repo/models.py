from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Projects(models.Model):
    title = models.CharField(max_length=30)
    image= models.ImageField(upload_to='images/')
    description = models.TextField()
    link= models.URLField(max_length = 200)
    owner = models.ForeignKey('auth.User', related_name='projects', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def save_repo(self):
       self.save()

    def __str__(self):
      return self.title


class Profile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    projects = models.ManyToManyField(Projects)

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

    def __str__(self):
      return self.content