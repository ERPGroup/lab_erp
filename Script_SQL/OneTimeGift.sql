/* Hau mai 10 hoa don dau tien */
/* Tạo lịch sử giao dịch */
Insert into website_Purchase_Service (purchase_name,amount,state,success_at,is_active,archive,merchant_id_id,service_id_id)
	select 'Khuyen mai 10 hoa don dau tien',0,1,now(),True,False,merchant_id,3
	from website_Order_Detail AS detail, website_order AS _order
	where 10 < 
	(
		select count(website_Order_Detail.id) 
		from website_Order_Detail,website_Account_Gift
		where merchant_id = detail.merchant_id and state = '1' and _order.id = order_id
		and website_Account_Gift.is_10 = False and website_Account_Gift.account_id = merchant_id
	)
	group by merchant_id
/* Thêm gói tin vô tài khoản */
Insert into website_Account_Service (remain,account_id,service_id)
	select 10,merchant_id,3
	from website_Order_Detail AS detail, website_order AS _order
	where 10 < 
	(
		select count(website_Order_Detail.id) 
		from website_Order_Detail,website_Account_Gift
		where merchant_id = detail.merchant_id and state = '1' and _order.id = order_id
		and website_Account_Gift.is_10 = False and website_Account_Gift.account_id = merchant_id
	)
	group by merchant_id
/* Xác nhận tài khoản đã nhận khuyến mãi */
Update website_Account_Gift set is_10 = True where account_id in (
	select distinct merchant_id
	from website_Order_Detail AS detail, website_order AS _order
	where 10 < 
	(
		select count(website_Order_Detail.id) 
		from website_Order_Detail,website_Account_Gift
		where merchant_id = detail.merchant_id and state = '1' and _order.id = order_id
		and website_Account_Gift.is_10 = False and website_Account_Gift.account_id = merchant_id
	)
)
/* Hau mai 50 hoa don dau tien */
Insert into website_Purchase_Service (purchase_name,amount,state,success_at,is_active,archive,merchant_id_id,service_id_id)
	select 'Khuyen mai 50 hoa don dau tien',0,1,now(),True,False,merchant_id,2
	from website_Order_Detail AS detail, website_order AS _order
	where 50 < 
	(
		select count(website_Order_Detail.id) 
		from website_Order_Detail,website_Account_Gift
		where merchant_id = detail.merchant_id and state = '1' and _order.id = order_id
		and website_Account_Gift.is_50 = False and website_Account_Gift.account_id = merchant_id
	)
	group by merchant_id
	
Insert into website_Account_Service (remain,account_id,service_id)
	select 10,merchant_id,2
	from website_Order_Detail AS detail, website_order AS _order
	where 50 < 
	(
		select count(website_Order_Detail.id) 
		from website_Order_Detail,website_Account_Gift
		where merchant_id = detail.merchant_id and state = '1' and _order.id = order_id
		and website_Account_Gift.is_50 = False and website_Account_Gift.account_id = merchant_id
	)
	group by merchant_id

Update website_Account_Gift set is_50 = True where account_id in (
	select distinct merchant_id
	from website_Order_Detail AS detail, website_order AS _order
	where 50 < 
	(
		select count(website_Order_Detail.id) 
		from website_Order_Detail,website_Account_Gift
		where merchant_id = detail.merchant_id and state = '1' and _order.id = order_id
		and website_Account_Gift.is_50 = False and website_Account_Gift.account_id = merchant_id
	)
)
/* Hau mai 100 hoa don dau tien */
Insert into website_Purchase_Service (purchase_name,amount,state,success_at,is_active,archive,merchant_id_id,service_id_id)
	select 'Khuyen mai 50 hoa don dau tien',0,1,now(),True,False,merchant_id,1
	from website_Order_Detail AS detail, website_order AS _order
	where 100 < 
	(
		select count(website_Order_Detail.id) 
		from website_Order_Detail,website_Account_Gift
		where merchant_id = detail.merchant_id and state = '1' and _order.id = order_id
		and website_Account_Gift.is_100 = False and website_Account_Gift.account_id = merchant_id
	)
	group by merchant_id
	
Insert into website_Account_Service (remain,account_id,service_id)
	select 10,merchant_id,1
	from website_Order_Detail AS detail, website_order AS _order
	where 100 < 
	(
		select count(website_Order_Detail.id) 
		from website_Order_Detail,website_Account_Gift
		where merchant_id = detail.merchant_id and state = '1' and _order.id = order_id
		and website_Account_Gift.is_100 = False and website_Account_Gift.account_id = merchant_id
	)
	group by merchant_id

Update website_Account_Gift set is_100 = True where account_id in (
	select distinct merchant_id
	from website_Order_Detail AS detail, website_order AS _order
	where 100 < 
	(
		select count(website_Order_Detail.id) 
		from website_Order_Detail,website_Account_Gift
		where merchant_id = detail.merchant_id and state = '1' and _order.id = order_id
		and website_Account_Gift.is_100 = False and website_Account_Gift.account_id = merchant_id
	)
)
