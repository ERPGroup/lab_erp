update website_purchase_service_ads 
set state = 5 
where id in (
SELECT website_purchase_service_ads.id
FROM website_service_ads,website_purchase_service_ads
Where website_purchase_service_ads.service_ads_id_id = website_service_ads.id and website_purchase_service_ads.state = '4' and (website_purchase_service_ads.date_start +  interval '1' day * website_service_ads.day_limit) <= now()
)
