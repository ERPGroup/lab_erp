from django.db import models

# Create your models here.


class Account(models.Model):
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    birthday = models.DateField(null=True)
    sex = models.BooleanField(default=False)
    phone = models.CharField(max_length=12, null=True)
    id_card = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=200, null=True)
    name_shop = models.CharField(max_length=200, null=True)
    activity_account = models.BooleanField(default=False)
    activity_merchant = models.BooleanField(default=False)
    activity_advertiser = models.BooleanField(default=False)
    q_post = models.IntegerField(default=0)
    q_vip = models.IntegerField(default=0)
    code_act_account = models.CharField(max_length=60)
    code_act_merchant = models.CharField(max_length=60)
    token_ghtk = models.CharField(max_length=100, null=True)
    is_admin = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    is_lock =  models.BooleanField(default=False)

    def __str__(self):
        return self.email

class Account_Service(models.Model):
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    service = models.ForeignKey('Service', on_delete=models.CASCADE)
    remain = models.IntegerField(default=0)


class Product (models.Model):
    name = models.CharField(max_length=200)
    detail = models.TextField(max_length=2000, null=True)
    origin = models.CharField(max_length=200)
    type_product = models.BooleanField()
    price = models.IntegerField()
    discount_percent = models.IntegerField(default=0)
    code = models.CharField(max_length=200)
    is_activity = models.BooleanField(default=True)
    archive = models.BooleanField(default=False)
    account_created = models.ForeignKey('Account', on_delete=models.CASCADE)
    archive_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.name

class Category (models.Model):
    name_category = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name_category

class Product_Category(models.Model):
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE)
    archive = models.BooleanField(default=False)
    archive_at = models.DateTimeField(null=True)
    lock = models.BooleanField(default=False)


class Attribute (models.Model):
    label = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.label

class Product_Attribute (models.Model):
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    attribute_id = models.ForeignKey('Attribute', on_delete=models.CASCADE)
    value = models.CharField(max_length=200)
    archive = models.BooleanField(default=False)
    archive_at = models.DateTimeField(null=True)
    lock = models.BooleanField(default=False)



class Product_Image(models.Model):
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    image_id = models.ForeignKey('Image', on_delete=models.CASCADE)
    archive = models.BooleanField(default=False)
    archive_at = models.DateTimeField(null=True)


class Image (models.Model):
    image_link = models.ImageField(upload_to='merchant/product/')
    is_default = models.BooleanField(default=False)
    user_id = models.ForeignKey('Account', on_delete=models.CASCADE)


class Link_Type(models.Model):
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    parent_product = models.IntegerField()


class Tag(models.Model):
    tag_key = models.CharField(max_length=200)
    tag_value = models.CharField(max_length=200)
    tag_type = models.IntegerField()
    see = models.IntegerField(default=0)
    archive = models.BooleanField(default=False)
    archive_at = models.DateTimeField(null=True)


class Post_Product (models.Model):
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    post_type = models.ForeignKey('Service', on_delete=models.CASCADE)
    creator_id = models.ForeignKey('Account', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    expire = models.DateTimeField()
    visable_vip = models.BooleanField()
    created = models.DateTimeField(auto_now=True)
    is_activity = models.BooleanField(default=True)
    views = models.IntegerField(default=0)
    is_lock = models.BooleanField(default=False)
    bought = models.IntegerField(default=0)
    # archive = models.BooleanField(default=False)


class Rating (models.Model):
    customer =  models.ForeignKey('Account', on_delete=models.CASCADE, related_name='Customer')
    merchant =  models.ForeignKey('Account', on_delete=models.CASCADE, related_name='Merchant')
    num_of_star = models.IntegerField()
    comment = models.CharField(max_length=2000)
    confirm_bought = models.BooleanField()
    is_activity = models.BooleanField(default=True)

    def __str__(self):
        return self.customer.name

class Rating_Customer (models.Model):
    customer =  models.ForeignKey('Account', on_delete=models.CASCADE, related_name='cus')
    merchant =  models.ForeignKey('Account', on_delete=models.CASCADE, related_name='mer')
    num_of_star = models.IntegerField()
    confirm_bought = models.BooleanField()
    is_activity = models.BooleanField(default=True)

    def __str__(self):
        return self.customer.name

class Order (models.Model):
    customer =  models.ForeignKey('Account', on_delete=models.CASCADE)
    amount = models.IntegerField()
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=12)
    note = models.CharField(max_length=200, null=True)
    CHOICES_STATE = (('1', 'Thành công'), ('0', 'Hủy bỏ'), ('2', 'Đặt hàng'))
    state = models.CharField(max_length=1, choices=CHOICES_STATE)
    manner = models.BooleanField(default=True) # payment by COD or paypal
    is_paid = models.BooleanField()
    is_activity = models.BooleanField()
    created = models.DateTimeField(auto_now=True)
    archive = models.BooleanField()
    canceler_id = models.IntegerField(null=True)

class Order_Detail (models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    merchant = models.ForeignKey('Account', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    CHOICES_STATE = (('1', 'Thành công'), ('0', 'Hủy bỏ'), ('2', 'Đặt hàng'), ('3', 'Đang gói hàng'), ('4', 'Đang vận chuyển'))
    state = models.CharField(max_length=1, choices=CHOICES_STATE)
    confirm_of_merchant = models.BooleanField()
    canceler_id = models.IntegerField(null=True)
    is_seen =models.BooleanField(default=False)


# class Email_Template(models.Model):
#     name_template = models.CharField(max_length=100)
#     type_template = models.IntegerField()
#     content = models.TextField()
#     state = models.BooleanField(default=True)


class Service(models.Model):
    service_name = models.CharField(max_length=200)
    amount = models.IntegerField()
    value = models.IntegerField()
    quantity_product = models.IntegerField()
    created = models.DateTimeField(auto_now=True)
    day_limit = models.IntegerField()
    visable_vip = models.BooleanField()
    is_active = models.BooleanField(default=True)
    archive = models.BooleanField(default=False)
    creator_id = models.IntegerField()
    canceler_id = models.IntegerField(null=True)

    def __str__(self):
        return self.service_name

class Purchase_Service(models.Model):
    purchase_name = models.CharField(max_length=200)
    merchant_id = models.ForeignKey('Account', on_delete=models.CASCADE)
    service_id = models.ForeignKey('Service', on_delete=models.CASCADE)
    amount = models.FloatField(null=True, blank=True, default=None)
    state = models.IntegerField()
    success_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    archive = models.BooleanField(default=False)


class Service_Ads(models.Model):
    service_name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    amount = models.IntegerField()
    created = models.DateTimeField(auto_now=True)
    day_limit = models.IntegerField()
    is_active = models.BooleanField(default=True)
    archive = models.BooleanField(default=False)
    creator_id = models.IntegerField()
    canceler_id = models.IntegerField(null=True)


class Service_Ads_Post(models.Model):
    service_name = models.CharField(max_length=200)
    purchase_service_id = models.ForeignKey('Purchase_Service_Ads', on_delete=models.CASCADE)
    customer_id = models.ForeignKey('Account',on_delete=models.CASCADE)
    image_1 = models.CharField(max_length=200)
    image_1_url = models.CharField(max_length=200)
    image_1_content = models.CharField(max_length=200)
    image_2 = models.CharField(max_length=200,blank=True,null=True)
    image_2_url = models.CharField(max_length=200,blank=True,null=True)
    image_2_content = models.CharField(max_length=200,blank=True,null=True)
    image_3 = models.CharField(max_length=200,blank=True,null=True)
    image_3_url = models.CharField(max_length=200,blank=True,null=True)
    image_3_content = models.CharField(max_length=200,blank=True,null=True)
    CHOICES_STATE = (('1','IsPosting'),('2','IsConfirm'),('-1','Cancel'))
    state = models.CharField(max_length=1, choices=CHOICES_STATE)


class Purchase_Service_Ads(models.Model):
    purchase_name = models.CharField(max_length=200)
    merchant_id = models.ForeignKey('Account', on_delete=models.CASCADE)
    service_ads_id = models.ForeignKey('Service_Ads',on_delete=models.CASCADE)
    amount = models.IntegerField()
    CHOICES_STATE = (('1', 'Success'), ('0', 'Cancel'), ('2','IsPosted'), ('3','IsConfirmed'),('4', 'IsActiving'),('5','Expired'))
    state = models.CharField(max_length=1, choices=CHOICES_STATE)
    date_start = models.DateTimeField(blank=True,null=True)
    success_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    archive = models.BooleanField(default=False)