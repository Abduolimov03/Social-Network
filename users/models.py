from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class User(AbstractUser):
    profile = models.ImageField(upload_to="profile_images/", default="defaults/profile.png")
    cover = models.ImageField(upload_to="cover_images/",default="defaults/cover.png")
    # followers = models.ManyToManyField("self", blank=True)
    # following  = models.ManyToManyField("self", blank=True)
    verified = models.BooleanField(default=False)
    bio = models.CharField(max_length=120, blank=True, null=True)
    birth_of_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username

class Follwing(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='followers')
    follower=models.ForeignKey(User,on_delete=models.CASCADE,related_name='followings')
    datatime=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.follower.username}  followed {self.user.username}"

    class Meta:
        unique_together=['user','follower']



