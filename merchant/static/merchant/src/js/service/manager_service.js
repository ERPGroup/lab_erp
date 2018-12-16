$(document).ready(function(){
    $.ajax({
        url: 'http://13.67.105.209:8000/merchant/services',
        method: 'GET',
        contentType: 'application/json',
        success: function(response){
            console.log(response);
            for (var i = 0; i < response.length; i++){
                var item = response[i]['fields']
                box = ''
                box +='<div class="col-md-6 col-sm-6 background_white">'
                box +='<div class="pricingTable green  ">'
                box +='<div class="pricingTable-header">'
                box +='<h3 class="title">'+ item.service_name +'</h3>'
                box +='</div>'
                box +='<div class="price-value">'
                box +='<span class="amount">'+ item.amount +'</span>'
                box +='<span class="month">VNĐ/gói</span>'
                box +='</div>'
                box +='<ul class="pricing-content">'
                if(item.value != 0)
                    box +='<li>'+ item.value +' tin đăng</li>'
                else
                    box +='<li class="disable">'+ item.value +' tin đăng</li>'
                
                if(item.quantity_product != 0)
                    box +='<li>'+ item.quantity_product +' sản phẩm mỗi tin</li>'
                else
                    box +='<li class="disable">'+ item.quantity_product +' sản phẩm mỗi tin</li>'

                // setup day_limit
                if(item.day_limit != 0)
                    box +='<li>'+ item.day_limit +' ngày sử dụng mỗi tin</li>'
                else
                    box +='<li class="disable">'+ item.day_limit +' ngày sử dụng mỗi tin</li>'
                
                // setup visable_vip
                if(item.visable_vip == true)
                    box +='<li>Hiển thị trên khu vực VIP</li>'
                else
                    box +='<li class="disable">Không hiển thị trên khu vực VIP</li>'
                
                box +='</ul>'
                box +='<a href="/merchant/purchase_service/'+ response[i]['pk'] +'" class="pricingTable-signup"><span>Mua Ngay</span></a>'
                box +='</div>'
                box +='</div>'
                $("#item").append(box);
            }
        }
    })
});


