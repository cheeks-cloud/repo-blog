from django.db import models
from django.contrib.auth.models import User
# Create your models here.






class Profile(models.Model):   #add this class and the following fields
	user = models.OneToOneField(User, on_delete=models.CASCADE)
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