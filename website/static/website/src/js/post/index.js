$(document).ready(function(){
    var check_url = $(location).attr('pathname').split('/');
    var id_post = check_url[check_url.length - 1]

    $.ajax({
        url: 'http://localhost:8000/post_data/' + id_post,
        method: 'GET',
        contentType: 'application/json',
        success: function(response){
            console.log(response)
            $('h2[id=name_product]').append(response.product.name)
            $('#product_title').append(response.product.name)
            $('#detail_product').append(response.product.detail)

            $('#bxslider').empty()
            $('#bx-pager').empty()
            html_zoom = ''
            html_image = ' '
            for(var item = 0; item < response.product.images.length; item++){
                html_zoom += '<li>'
                html_zoom += '<div class="thumb_image_quickview">'
                html_zoom += '<img class="cloudzoom" id="zoom1" data-cloudzoom="zoomSizeMode:\'image\',zoomPosition:\'3\', zoomOffsetX:0" src="/product/'+ response.product.images[item].image_link +'" alt="#" />'
                html_zoom += '</div>'
                html_zoom += '</li>'
                if (item == 0)
                
                    html_image += '<a href="" data-slide-index="0"><img class="img-responsive" src="/product/'+ response.product.images[item].image_link +'"/></a>'
                else
                    html_image += '<a href="" data-slide-index="1"><img class="img-responsive" src="/product/'+ response.product.images[item].image_link +'"/></a>'
            }

            $('#bxslider').append(html_zoom)
            $('#bx-pager').append(html_image)

            $('.bxslider').bxSlider({
                pagerCustom: '#bx-pager',
                infiniteLoop: false,
                touchEnabled: true,
                nextText: '<i class="icon-right-open-mini" aria-hidden="true"></i>',
                prevText: '<i class="icon-left-open-mini" aria-hidden="true"></i>',
                onSlideAfter: function (currentSlideNumber, totalSlideQty, currentSlideHtmlObject) {
                    $('.active-slide').removeClass('active-slide');
                    $('.bxslider>li').eq(currentSlideHtmlObject + 1).addClass('active-slide');
                    $('#bx-pager .owl-stage').trigger('to.owl.carousel', currentSlideHtmlObject);
                },
                onSliderLoad: function () {
                    $('.bxslider > li').eq(1).addClass('active-slide')
                },
            });

            dl_owl('div[id=bx-pager]');

            CloudZoom.quickStart();
            $.extend($.fn.CloudZoom.defaults, {
                zoomPosition: 'inside',
                autoInside: true,
                disableOnScreenWidth: 991
            });

            html_option = ''
            for(var i = 0; i < response.product.version.length; i++){
                html_option += '<option value="'+ i +'">'+ response.product.version[i].name_product +'</option>'
            }
            $('select[id=version]').append(html_option);
            // setup first version
            get_version(0);

            merchant_html = ''
            merchant_html += '<h2>Thông tin người bán: </h2>'
            merchant_html += '<p>Tên cửa hàng: <a href="">'+ response.merchant.name_shop +'</a></p>'
            merchant_html += '<p>Đánh giá: '
            merchant_html += '<span class="rating"> '+ response.merchant.rating +' <i class="fa fa-star"></i></span>'
            merchant_html += '</p>'
            //merchant_html += '<p style="color:#f58634;">Cấp bậc: <b>Vàng <i class="fa fa-trophy"></i></b></p>'
            merchant_html += '<hr>'
            merchant_html += '<a href="#">Ghé thăm gian hàng</a>'
            merchant_html += '<br>'
            merchant_html += '<a href="#">Liên hệ người bán</a>'

            $('div[id=merchant]').append(merchant_html)


            html_choice_qty = '<span class="col-xs-4">Số lượng:</span>'
            html_choice_qty += '<button onclick="sub_product()" class="button_add">-</button>'
            html_choice_qty += '<input value="1" class="input_add" maxlength="3" size="5" name="quantity" id="quantity">'
            html_choice_qty += '<button onclick="add_product('+ (response.quantity - response.bought) +')" class="button_add">+</button>'
            $('#quantity_choice').append(html_choice_qty)

            $('b[id=qty_avaliable]').append('Còn hàng ('+ (response.quantity - response.bought) +' sản phẩm có sẵn)')
        }
    })
});


function get_version(item){
    var check_url = $(location).attr('pathname').split('/');
    var id_post = check_url[check_url.length - 1]
    $.ajax({
        url: 'http://localhost:8000/post_data/' + id_post,
        method: 'GET',
        contentType: 'application/json',
        success: function(response){
            $('tbody[id=tbl_product]').empty()
            tbl_product_html = ''
            for(var i = 0; i < response.product.version[item].attributes.length; i++){
                tbl_product_html += '<tr>'
                tbl_product_html += '<td>'+ response.product.version[item].attributes[i].label +'</td>'
                tbl_product_html += '<td>'+ response.product.version[item].attributes[i].value +'</td>'
                tbl_product_html += '</tr>'
            }
            $('tbody[id=tbl_product]').append(tbl_product_html);

            $('h3[id=price_product]').empty()
            $('h3[id=price_product]').append(response.product.version[item].price + ' VND')

            // $('#version_product').val(response.product.version[item].id_product)
        }
    });
}


function sub_product(){
    var qty = parseInt($('input[id=quantity]').val());
    if (qty <= 1) return
    $('input[id=quantity]').val(qty -1);
}
  
function add_product(qty_aval){
    var qty = parseInt($('input[id=quantity]').val()); 
    if (qty >= qty_aval) return
    $('input[id=quantity]').val(qty + 1);
}
