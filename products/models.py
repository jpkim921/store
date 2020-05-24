from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)
    primaryCategory = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    preview_text = models.TextField(
        max_length=200, null=True, blank=True, verbose_name="Preview Text")
    detail_text = models.TextField(
        max_length=1000, null=True, blank=True, verbose_name="Detail Text")
    price = models.FloatField()
    slug = models.SlugField()
    timestamp = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to="static/products/images", blank=True)
    mainimage = models.ImageField(upload_to="static/products/images", blank=True)

    def __str__(self):
        return self.name
