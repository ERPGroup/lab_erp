from django.db import models

# Create your models here.


class Account(models.Model):

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    birthday = models.DateField(null=True)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=200)
    activity_merchant = models.BooleanField(default=False)
    name_shop = models.CharField(max_length=200)
    q_post = models.IntegerField(default=0)
    q_vip = models.IntegerField(default=0)

    def __str__(self):
        return self.email

class Product (models.Model):
    name = models.CharField(max_length=200)
    detail = models.TextField(max_length=2000)
    origin = models.CharField(max_length=200)
    type_product = models.CharField(max_length=200)
    is_visible = models.BooleanField(default=True)
    is_activity = models.BooleanField(default=True)
    archive = models.BooleanField(default=False)
    account_created = models.ForeignKey('Account', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Category (models.Model):
    name_category = models.CharField(max_length=200)
    quantity = models.IntegerField()
    is_activity = models.BooleanField(default=True)

    def __str__(self):
        return self.name_category

class Product_Category(models.Model):
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE)

class Attribute (models.Model):
    code = models.CharField(max_length=200)
    label = models.CharField(max_length=200)
    type_attr = models.CharField(max_length=200)
    is_required = models.BooleanField(default=True)
    is_unique = models.BooleanField(default=True)

    def __str__(self):
        return self.label

class Product_Attribute (models.Model):
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    attribute_id = models.ForeignKey('Attribute', on_delete=models.CASCADE)
    value = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now=True)

class Discount (models.Model):
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    percent = models.IntegerField()
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()

    def __str__(self):
        return self.product_id__name

class Post_Product (models.Model):
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created = models.DateTimeField(auto_now=True)
    is_vip = models.BooleanField()
    is_activity = models.BooleanField()

    def __str__(self):
        return self.product_id__name


