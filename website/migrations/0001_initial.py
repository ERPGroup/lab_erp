# Generated by Django 2.0.6 on 2018-11-22 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=100)),
                ('birthday', models.DateField(null=True)),
                ('phone', models.CharField(max_length=12)),
                ('id_card', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=200)),
                ('activity_account', models.BooleanField(default=False)),
                ('activity_merchant', models.BooleanField(default=False)),
                ('activity_advertiser', models.BooleanField(default=False)),
                ('name_shop', models.CharField(max_length=200)),
                ('q_post', models.IntegerField(default=0)),
                ('q_vip', models.IntegerField(default=0)),
                ('code_act_account', models.CharField(max_length=60)),
                ('code_act_merchant', models.CharField(max_length=60)),
                ('is_admin', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Account_Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remain', models.IntegerField(default=0)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=200)),
                ('label', models.CharField(max_length=200)),
                ('type_attr', models.CharField(max_length=200)),
                ('is_required', models.BooleanField(default=True)),
                ('is_unique', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percent', models.IntegerField()),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_link', models.ImageField(upload_to='merchant/product/')),
                ('is_default', models.BooleanField(default=False)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Link_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_product', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=12)),
                ('state', models.CharField(choices=[('1', 'Success'), ('0', 'Cancel'), ('2', 'Packing'), ('3', 'Transporting')], max_length=1)),
                ('manner', models.CharField(max_length=200)),
                ('is_paid', models.BooleanField()),
                ('is_activity', models.BooleanField()),
                ('archive', models.BooleanField()),
                ('canceler_id', models.IntegerField(null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Order_Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('state', models.CharField(choices=[('1', 'Success'), ('0', 'Cancel'), ('2', 'Packing'), ('3', 'Transporting')], max_length=1)),
                ('confirm_of_merchant', models.BooleanField()),
                ('canceler_id', models.IntegerField(null=True)),
                ('merchant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Account')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Post_Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('is_index', models.BooleanField()),
                ('created', models.DateTimeField(auto_now=True)),
                ('expire', models.DateTimeField()),
                ('is_activity', models.BooleanField(default=True)),
                ('visable_vip', models.BooleanField()),
                ('expire_visable_page_home', models.DateTimeField()),
                ('creator_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('detail', models.TextField(max_length=2000)),
                ('origin', models.CharField(max_length=200)),
                ('type_product', models.BooleanField()),
                ('price', models.IntegerField()),
                ('code', models.CharField(max_length=200)),
                ('is_visible', models.BooleanField(default=True)),
                ('is_activity', models.BooleanField(default=True)),
                ('archive', models.BooleanField(default=False)),
                ('account_created', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Product_Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now=True)),
                ('attribute_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Attribute')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Product_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Category')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Product_Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Image')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase_Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_name', models.CharField(max_length=200)),
                ('amount', models.IntegerField()),
                ('state', models.IntegerField()),
                ('success_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('archive', models.BooleanField(default=False)),
                ('merchant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase_Service_Ads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_name', models.CharField(max_length=200)),
                ('amount', models.IntegerField()),
                ('state', models.IntegerField()),
                ('date_start', models.DateTimeField(blank=True, null=True)),
                ('success_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('archive', models.BooleanField(default=False)),
                ('merchant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_of_star', models.IntegerField()),
                ('comment', models.CharField(max_length=2000)),
                ('is_activity', models.BooleanField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Customer', to='website.Account')),
                ('merchant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Merchant', to='website.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=200)),
                ('amount', models.IntegerField()),
                ('value', models.IntegerField()),
                ('quantity_product', models.IntegerField()),
                ('created', models.DateTimeField(auto_now=True)),
                ('day_limit', models.IntegerField()),
                ('day_visable_page_home', models.IntegerField()),
                ('visable_vip', models.BooleanField()),
                ('is_active', models.BooleanField(default=True)),
                ('archive', models.BooleanField(default=False)),
                ('creator_id', models.IntegerField()),
                ('canceler_id', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service_Ads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('amount', models.IntegerField()),
                ('created', models.DateTimeField(auto_now=True)),
                ('day_limit', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('archive', models.BooleanField(default=False)),
                ('creator_id', models.IntegerField()),
                ('canceler_id', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service_Ads_Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=200)),
                ('image_1', models.CharField(max_length=200)),
                ('image_1_url', models.CharField(max_length=200)),
                ('image_1_content', models.CharField(max_length=200)),
                ('image_2', models.CharField(max_length=200)),
                ('image_2_url', models.CharField(max_length=200)),
                ('image_2_content', models.CharField(max_length=200)),
                ('image_3', models.CharField(max_length=200)),
                ('image_3_url', models.CharField(max_length=200)),
                ('image_3_content', models.CharField(max_length=200)),
                ('expiried', models.DateTimeField()),
                ('is_active', models.BooleanField(default=False)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Account')),
                ('purchase_service_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Purchase_Service')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_key', models.CharField(max_length=200)),
                ('tag_value', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='purchase_service_ads',
            name='service_ads_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.Service_Ads'),
        ),
        migrations.AddField(
            model_name='purchase_service_ads',
            name='service_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.Service'),
        ),
        migrations.AddField(
            model_name='purchase_service',
            name='service_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Service'),
        ),
        migrations.AddField(
            model_name='post_product',
            name='post_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Service'),
        ),
        migrations.AddField(
            model_name='post_product',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Product'),
        ),
        migrations.AddField(
            model_name='order_detail',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Product'),
        ),
        migrations.AddField(
            model_name='link_type',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Product'),
        ),
        migrations.AddField(
            model_name='discount',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Product'),
        ),
        migrations.AddField(
            model_name='account_service',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Service'),
        ),
    ]
