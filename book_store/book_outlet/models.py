from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import RegexValidator


class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(
        max_length=2,
    )



class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(
        max_length=6,
        validators=[RegexValidator(r'^\d{6}$', 'Enter exactly 6 digits.')],
        help_text="Enter a 6-digit number"
    )
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.street + " " + self.postal_code + " " + self.city

    class Meta:
        verbose_name_plural = "address entries"


class Author(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    Address = models.OneToOneField(
        Address, on_delete=models.CASCADE, null=True)

    def fullName(self):
        return self.firstName + " " + self.lastName

    def __str__(self):
        return self.fullName()


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, related_name="books")
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True, blank=True)
    published_countries = models.ManyToManyField(Country,null=False)   
    

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, *kwargs)

    def get_absolute_url(self):
        return reverse("book-details", args=[self.slug])

    def __str__(self):
        return f"{self.title} ({self.rating}) {self.author} {self.is_bestselling}"
