
Category.objects.create(name_category='may tinh bang', quantity=2)

Attribute.objects.create(code='32', label='camera', type_attr='12')
Attribute.objects.create(code='32', label='man hinh', type_attr='12')
Attribute.objects.create(code='32', label='ram', type_attr='12')


Service.objects.create(service_name='goi bach kim', amount=400000, value=15, day_limit=10, day_visable_page_home=4, visable_vip=True, is_active=True, archive=False)
Service.objects.create(service_name='goi vang', amount=300000, value=10, day_limit=10, day_visable_page_home=2, visable_vip=True, is_active=True, archive=False)
Service.objects.create(service_name='goi bac', amount=150000, value=10, day_limit=10, day_visable_page_home=0, visable_vip=False, is_active=True, archive=False)
