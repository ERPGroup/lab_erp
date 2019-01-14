Update website_account_service set remain = remain + 3
where service_id = 2 and account_id in (
	select DISTINCT detail.merchant_id 
	from website_Order_Detail AS detail, website_order AS _order
	where 10 < 
	(
		select count(website_Order_Detail.id) 
		from website_Order_Detail,website_Account_Gift
		where merchant_id = detail.merchant_id and state = '1' and _order.id = order_id
		and _order.created <= now()
		and _order.created >= now() - interval '1' day * 14
		and website_Account_Gift.is_daily_7 = False
		and merchant_id = website_Account_Gift.account_id
	)
)

Update website_Account_Gift set is_daily_15 = True
where account_id in (
	select DISTINCT detail.merchant_id 
	from website_Order_Detail AS detail, website_order AS _order
	where 10 < 
	(
		select count(id) 
		from website_Order_Detail
		where merchant_id = detail.merchant_id and state = '1' and _order.id = order_id
		and _order.created <= now()
		and _order.created >= now() - interval '1' day * 14 	
	)
)

