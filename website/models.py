from django.db import models

# Create your models here.


class Account(models.Model):
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    birthday = models.DateField(null=True)
    phone = models.CharField(max_length=12)
    id_card = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    activity_account = models.BooleanField(default=False)
    activity_merchant = models.BooleanField(default=False)
    activity_advertiser = models.BooleanField(default=False)
    name_shop = models.CharField(max_length=200)
    q_post = models.IntegerField(default=0)
    q_vip = models.IntegerField(default=0)
    code_act_account = models.CharField(max_length=60)
    code_act_merchant = models.CharField(max_length=60)
    is_admin = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

class Product (models.Model):
    name = models.CharField(max_length=200)
    detail = models.TextField(max_length=2000)
    origin = models.CharField(max_length=200)
    type_product = models.BooleanField()
    is_visible = models.BooleanField(default=True)
    is_activity = models.BooleanField(default=True)
    archive = models.BooleanField(default=False)
    account_created = models.ForeignKey('Account', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Category (models.Model):
    name_category = models.CharField(max_length=200)
    quantity = models.IntegerField()

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
    date_start = models.DateField()
    date_end = models.DateField()

    def __str__(self):
        return self.product_id__name

class Product_Image(models.Model):
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    image_id = models.ForeignKey('Image', on_delete=models.CASCADE)


class Image (models.Model):
    image_link = models.ImageField(upload_to='merchant/product/')
    is_default = models.BooleanField(default=False)
    user_id = models.ForeignKey('Account', on_delete=models.CASCADE)


class Link_Type(models.Model):
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    parent_product = models.IntegerField()


class Tag(models.Model):
    tag_key = models.CharField(max_length=200)
    tag_value =models.CharField(max_length=200)


# class Post_Product (models.Model):
#     product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
#     quantity = models.IntegerField()
#     created = models.DateTimeField(auto_now=True)
#     is_vip = models.BooleanField()
#     is_activity = models.BooleanField()

#     def __str__(self):
#         return self.product_id__name

# class Rating (models.Model):
#     customer =  models.ForeignKey('Account', on_delete=models.CASCADE)
#     merchant =  models.ForeignKey('Account', on_delete=models.CASCADE)
#     num_of_star = models.IntegerField()
#     comment = models.CharField(max_length=2000)
#     is_activity = models.BooleanField()

#     def __str__(self):
#         return self.customer.name


# class Order (models.Model):
#     customer =  models.ForeignKey('Account', on_delete=models.CASCADE)
#     amount = models.IntegerField()
#     address = models.CharField(max_length=200)
#     phone = models.CharField(max_length=12)
#     state = models.CharField()
#     manner = models.CharField()
#     is_paid = models.BooleanField()
#     is_activity = models.BooleanField()
#     archive = models.BooleanField()

# class Order_Detail (models.Model):
#     order = models.ForeignKey('Order', on_delete=models.CASCADE)
#     product = models.ForeignKey('Product', on_delete=models.CASCADE)
#     merchant = models.ForeignKey('Account', on_delete=models.CASCADE)
#     quantity = models.IntegerField()
#     price = models.IntegerField()
#     CHOISE_STATE = (('1', 'Success'), ('0', 'Cancel'))
#     state = models.CharField()


# class Email_Template(models.Model):
#     name_template = models.CharField(max_length=100)
#     type_template = models.IntegerField()
#     content = models.TextField()
#     state = models.BooleanField(default=True)
