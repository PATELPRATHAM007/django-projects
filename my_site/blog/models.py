from django.db import models
from django.core.validators import MinLengthValidator


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return f" {self.caption} "


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def fullName(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.fullName()


class Posts(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    imageName = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.title} {self.date} {self.slug} {self.author} "
