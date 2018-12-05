
Category.objects.create(name_category='may tinh bang', quantity=0)

Attribute.objects.create(code='32', label='camera', type_attr='12')
Attribute.objects.create(code='32', label='man hinh', type_attr='12')
Attribute.objects.create(code='32', label='ram', type_attr='12')


Service.objects.create(service_name='goi bach kim', amount=400000, value=15, quantity_product=15, day_limit=10, day_visable_page_home=4, visable_vip=True, is_active=True, archive=False, creator_id=1)
Service.objects.create(service_name='goi vang', amount=300000, value=10, quantity_product=10, day_limit=10, day_visable_page_home=2, visable_vip=True, is_active=True, archive=False, creator_id=1)
Service.objects.create(service_name='goi bac', amount=150000, value=10, quantity_product=10, day_limit=10, day_visable_page_home=0, visable_vip=False, is_active=True, archive=False, creator_id=1)


Service_Ads.objects.create(service_name='Quảng cáo hình ảnh đầu trang 7 ngày',position='Đầu trang',amount=1000000,day_limit=7,creator_id=1)
Service_Ads.objects.create(service_name='Quảng cáo hình ảnh đầu trang 15 ngày',position='Đầu trang',amount=1900000,day_limit=15,creator_id=1)
Service_Ads.objects.create(service_name='Quảng cáo hình ảnh đầu trang 30 ngày',position='Đầu trang',amount=2700000,day_limit=30,creator_id=1)
Service_Ads.objects.create(service_name='Quảng cáo hình ảnh giữa trang 7 ngày',position='Giữa trang',amount=900000,day_limit=7,creator_id=1)
Service_Ads.objects.create(service_name='Quảng cáo hình ảnh giữa trang 15 ngày',position='Giữa trang',amount=1600000,day_limit=15,creator_id=1)
Service_Ads.objects.create(service_name='Quảng cáo hình ảnh giữa trang 30 ngày',position='Giữa trang',amount=2400000,day_limit=30,creator_id=1)
Service_Ads.objects.create(service_name='Quảng cáo hình ảnh cuối trang 7 ngày',position='Cuối trang',amount=600000,day_limit=7,creator_id=1)
Service_Ads.objects.create(service_name='Quảng cáo hình ảnh cuối trang 15 ngày',position='Cuối trang',amount=1000000,day_limit=15,creator_id=1)
Service_Ads.objects.create(service_name='Quảng cáo hình ảnh cuối trang 30 ngày',position='Cuối trang',amount=1500000,day_limit=30,creator_id=1)
Service_Ads.objects.create(service_name='Quảng cáo slide x3 hình ảnh 7 ngày',position='Slide',amount=1500000,day_limit=7,creator_id=1)
Service_Ads.objects.create(service_name='Quảng cáo slide x3 hình ảnh 15 ngày',position='Slide',amount=2900000,day_limit=15,creator_id=1)
Service_Ads.objects.create(service_name='Quảng cáo slide x3 hình ảnh 30 ngày',position='Slide',amount=4500000,day_limit=30,creator_id=1)
Service_Ads.objects.create(service_name='Quảng cáo hình ảnh bên phải slide 1 - 7 ngày',position='Bên phải slide 1',amount=700000,day_limit=7,creator_id=1)
Service_Ads.objects.create(service_name='Quảng cáo hình ảnh bên phải slide 1 - 15 ngày',position='Bên phải slide 1',amount=1300000,day_limit=15,creator_id=1)
Service_Ads.objects.create(service_name='Quảng cáo hình ảnh bên phải slide 1 - 30 ngày',position='Bên phải slide 1',amount=1900000,day_limit=30,creator_id=1)
Service_Ads.objects.create(service_name='Quảng cáo hình ảnh bên phải slide 2 - 7 ngày',position='Bên phải slide 2',amount=700000,day_limit=7,creator_id=1)
Service_Ads.objects.create(service_name='Quảng cáo hình ảnh bên phải slide 2 - 15 ngày',position='Bên phải slide 2',amount=1300000,day_limit=15,creator_id=1)
Service_Ads.objects.create(service_name='Quảng cáo hình ảnh bên phải slide 2 - 30 ngày',position='Bên phải slide 2',amount=1900000,day_limit=30,creator_id=1)