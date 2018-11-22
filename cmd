
Category.objects.create(name_category='may tinh bang', quantity=2)

Attribute.objects.create(code='32', label='camera', type_attr='12')
Attribute.objects.create(code='32', label='man hinh', type_attr='12')
Attribute.objects.create(code='32', label='ram', type_attr='12')


Service.objects.create(service_name='goi bach kim', amount=400000, value=15, day_limit=10, day_visable_page_home=4, visable_vip=True, is_active=True, archive=False);
Service.objects.create(service_name='goi vang', amount=300000, value=10, day_limit=10, day_visable_page_home=2, visable_vip=True, is_active=True, archive=False)
Service.objects.create(service_name='goi bac', amount=150000, value=10, day_limit=10, day_visable_page_home=0, visable_vip=False, is_active=True, archive=False)

Service_Ads.objects.create(service_name='Quảng cáo hình ảnh 867x800',type_service=2,position='Đầu trang',amount=1500000,created='11/11/2018',day_limit=7)

Account.objects.create(username='deftnt',email='jimmi2051deftnt',password='',name='NguyenLyThanh',phone='0978956043',activity_account=True,activity_merchant=True,is_admin=True)

Purchase_Service_Ads.objects.create(purchase_name='Quảng cáo thân trang',
merchant_id=Account.objects.get(pk=1),service_ads_id=Service_Ads.objects.get(pk=1),
amount=999999,state=1,date_start='2018-11-21'
)
class Purchase_Service_Ads(models.Model):
    purchase_name = models.CharField(max_length=200)
    merchant_id = models.ForeignKey('Account', on_delete=models.CASCADE)
    service_id = models.ForeignKey('Service', on_delete=models.CASCADE,blank=True,null=True)
    service_ads_id = models.ForeignKey('Service_Ads',on_delete=models.CASCADE,blank=True,null=True)
    amount = models.IntegerField()
    state = models.IntegerField()
    date_start = models.DateTimeField(blank=True,null=True)
    success_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    archive = models.BooleanField(default=False)

