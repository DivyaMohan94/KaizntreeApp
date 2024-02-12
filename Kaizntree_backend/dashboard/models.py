from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name


class Tag(models.Model):
    tag_name = models.CharField(max_length=200)

    def __str__(self):
        return self.tag_name


class Items(models.Model):
    sku = models.CharField(max_length=200)
    item_name = models.CharField(max_length=200)
    category = models.ForeignKey(
        Category, null=True, on_delete=models.CASCADE, related_name="category")
    tags = models.ManyToManyField(Tag, null=True, related_name="tag")
    in_stock = models.IntegerField(default=0)
    available_stock = models.IntegerField(default=0)
    added_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.item_name
