update website_purchase_service_ads 
set state = 4 
where id in (
SELECT website_purchase_service_ads.id
FROM website_service_ads,website_purchase_service_ads
Where website_purchase_service_ads.service_ads_id_id = website_service_ads.id 
and website_purchase_service_ads.state = '3' 
and website_purchase_service_ads.date_start <= datetime()
)
