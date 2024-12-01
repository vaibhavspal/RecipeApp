from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Recipe(models.Model):
    title=models.CharField(max_length=100)
    description= models.TextField()

    author= models.ForeignKey(User , on_delete=models.CASCADE)

    created_at= models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    image= models.ImageField(upload_to='recipe_images/',null=True ,blank=True)

    def get_absolute_url(self):
        return reverse("recipe-detail", kwargs={"pk": self.pk})


# dunder string mthd

    def __str__(self):
        return self.title