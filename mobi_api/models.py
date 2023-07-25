from django.db import models


class Colors(models.TextChoices):
    red = "red"
    blue = "blue"
    black = "black"
    white = "white"
    yellow = "yellow"
    green = "green"

# Create your models here.
class mobile(models.Model):
    name = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    slug = models.SlugField(allow_unicode=True, unique=True, max_length=200, default="")
    display = models.CharField(max_length=100, blank=True, default="")
    display_size = models.CharField(max_length=100, blank=True, default="")
    resolution = models.CharField(max_length=100, blank=True)
    os = models.CharField(max_length=100, blank=True)
    Weight = models.IntegerField(null=True, blank=True)
    batery = models.CharField(max_length=30, blank=True)
    colors = models.CharField(max_length=100, choices=Colors.choices, default=Colors.black)
    Introduction = models.TextField(blank=True)
    expert_check = models.TextField(blank=True)
    image = models.ImageField(upload_to='pics', blank=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateField()

    def __str__(self) -> str:
        return self.name

    