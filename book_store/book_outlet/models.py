from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.urls import reverse
class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinLengthValidator(1),MaxLengthValidator(5)])
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)


    def get_absolute_url(self):
        return reverse("book-details", args=[self.id])
    
    def __str__(self):
        return f"{self.title} ({self.rating}) {self.author} {self.is_bestselling}"
    