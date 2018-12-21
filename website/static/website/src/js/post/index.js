$(document).ready(function(){
    var check_url = $(location).attr('pathname').split('/');
    var id_post = check_url[check_url.length - 1]

    $.ajax({
        url: 'http://54.213.242.175:8000/post_data/' + id_post,
        method: 'GET',
        contentType: 'application/json',
        success: function(response){

            $.ajax({
                url: 'http://54.213.242.175:8000/get_data_hot_buy',
                method: 'GET',
                success: function(response){
                    var html = ''
                    posts = response.datas
                    for(var item=0; item < response.datas.length; item++){
                        html += '<div class="product_box">'
                        html += '<div class="title_box">'
                        html += '<a ><p class="name_shop text-center">Bán chạy</p></a>'
                        html += '<p class="square_rating">'+ posts[item].rating +'</p>'
                        html += '</div>'
                        html += '<div class="thumb_image_product">'
                        html += '<a><img src="'+ posts[item].product.image +'"></a>'
                        html += '</div>'
                        html += '<div class="info_box">'
                        html += '<a href="/post/'+ posts[item].id +'" class="detail_product">'
                        html += '<p>'+ posts[item].product.name +'</p>'
                        html += '</a>'
                        if (posts[item].product.range_price[0] == posts[item].product.range_price[1]){
                            html += '<span class="price">'+ currency(((posts[item].product.range_price[0] * (100 - posts[item].product.discount_percent))/100), { precision: 0, separator: ',' }).format() +' VND </span>'
                        }
                        else{
                            html += '<span class="price">'+ currency((posts[item].product.range_price[1] * (100 - posts[item].product.discount_percent))/100, { precision: 0, separator: ',' }).format() + ' - ' +  currency((posts[item].product.range_price[0] * (100 - posts[item].product.discount_percent))/100, { precision: 0, separator: ',' }).format() +' VND </span>'
                        }
                        
                        // html += '<br class="hidden_desktop">'
                        // html += '<span class="disable_price">4.000.000 d</span>'
                        html += '<span class="sales_percent">-'+ posts[item].product.discount_percent +'%</span>'
                        html += '</div>'
                        html += '<div class="quick_view">'
                        html += '<button class="btn_buy" onclick="location.href=\'http://54.213.242.175:8000/post/'+ posts[item].id +'\';">Xem thêm</button>'
                        html += '</div>'
                        html += '</div>'
                    }
                    $('#like_product').append(html)
                }
            })

            // $.ajax({
            //     url: 'http://54.213.242.175:8000/get_data_related/' + response.product.categories[0].id,
            //     method: 'GET',
            //     success: function(response){
            //         var html = ''
            //         posts = response.datas
            //         for(var item=0; item < response.datas.length; item++){
            //             html += '<div class="item">'
            //             html += '<div class="product_box">'
            //             html += '<div class="title_box">'
            //             html += '<a ><p class="name_shop text-center">Sản phẩm liên quan</p></a>'
            //             html += '<p class="square_rating">'+ posts[item].rating +'</p>'
            //             html += '</div>'
            //             html += '<div class="thumb_image_product">'
            //             html += '<a><img src="'+ posts[item].product.image +'"></a>'
            //             html += '</div>'
            //             html += '<div class="info_box">'
            //             html += '<a href="/post/'+ posts[item].id +'" class="detail_product">'
            //             html += '<p>'+ posts[item].product.name +'</p>'
            //             html += '</a>'
            //             if( posts[item].product.discount_percent != 0){
            //                 if (posts[item].product.range_price[0] == posts[item].product.range_price[1]){
            //                     html += '<span class="price">'+ currency(((posts[item].product.range_price[0] * (100 - posts[item].product.discount_percent))/100), { precision: 0, separator: ',' }).format() +' VND </span>'
            //                 }
            //                 else{
            //                     html += '<span class="price">'+ currency((posts[item].product.range_price[1] * (100 - posts[item].product.discount_percent))/100 + ' - ' + (posts[item].product.range_price[0] * posts[item].product.discount_percent)/100, { precision: 0, separator: ',' }).format() +' VND </span>'
            //                 }
            //             }
            //             else{
            //                 if (posts[item].product.range_price[0] == posts[item].product.range_price[1]){
            //                     html += '<span class="price">'+ currency(posts[item].product.range_price[0], { precision: 0, separator: ',' }).format() +' VND </span>'
            //                 }
            //                 else{
            //                     html += '<span class="price">'+ currency(posts[item].product.range_price[1]+ ' - ' + posts[item].product.range_price[0], { precision: 0, separator: ',' }).format() +' VND </span>'
            //                 }
            //             }
                        
            //             // html += '<br class="hidden_desktop">'
            //             // html += '<span class="disable_price">4.000.000 d</span>'
            //             html += '<span class="sales_percent">-'+ posts[item].product.discount_percent +'%</span>'
            //             html += '</div>'
            //             html += '<div class="quick_view">'
            //             html += '<button class="btn_buy" onclick="location.href=\'http://54.213.242.175:8000/post/'+ posts[item].id +'\';">Xem thêm</button>'
            //             html += '</div>'
            //             html += '</div>'
            //             html += '</div>'
            //         }
            //         $('#related').html('');
            //         $('#related').append(html);
            //         dl_owl('.owl-product-relate');
            //     }
            // })
            
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
            merchant_html += '<p>Tên cửa hàng: <a>'+ response.merchant.name_shop +'</a></p>'
            merchant_html += '<p>Đánh giá: '
            merchant_html += '<span class="rating"> '+ response.merchant.rating +' <i class="fa fa-star"></i></span>'
            merchant_html += '</p>'
            //merchant_html += '<p style="color:#f58634;">Cấp bậc: <b>Vàng <i class="fa fa-trophy"></i></b></p>'
            merchant_html += '<hr>'
            merchant_html += '<a href="/shop/'+ response.merchant.id +'">Ghé thăm gian hàng</a>'
            merchant_html += '<br>'
            merchant_html += '<a href="/shop/'+ response.merchant.id +'">Liên hệ người bán</a>'

            $('div[id=merchant]').append(merchant_html)


            html_choice_qty = '<span class="col-xs-4">Số lượng:</span>'
            html_choice_qty += '<button onclick="sub_product()" class="button_add">-</button>'
            html_choice_qty += '<input value="1" class="input_add" maxlength="3" size="5" name="quantity" id="quantity">'
            html_choice_qty += '<button onclick="add_product('+ (response.quantity - response.bought) +')" class="button_add">+</button>'
            $('#quantity_choice').append(html_choice_qty)

            $('b[id=qty_avaliable]').append('Còn hàng ('+ (response.quantity - response.bought) +' sản phẩm có sẵn)')
            $('#id_product').val(response.product.version[0].id_product)

        }
    })
});

function rating_merchant(){
    var check_url = $(location).attr('pathname').split('/');
    var id_post = check_url[check_url.length - 1]
    data = {
        'num_star': $('#num_star').val(),
        'comment': $('#comment_text').val(),
    }
    $.ajax({
        url: 'http://54.213.242.175:8000/rating_merchant/' + id_post,
        method: 'POST',
        contentType: 'application/x-www-form-urlencoded',
        data: data,
        success: function(response){
            if(response == 1){
                alert('Đánh giá thành công!')
                location.reload()
            }
            else{
                alert(response)
            }
        }
    })
}

function get_version(item){
    var check_url = $(location).attr('pathname').split('/');
    var id_post = check_url[check_url.length - 1]
    $.ajax({
        url: 'http://54.213.242.175:8000/post_data/' + id_post,
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
            var price =currency(((response.product.version[item].price * (100 - response.product.discount_percent))/100), { precision: 0, separator: ',' }).format()
            $('h3[id=price_product]').append(price + ' VND')

            $('#id_product').val(response.product.version[item].id_product)
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



function buy_product(){
    var quantity = $('input[id=quantity]').val()
    var product = $('#id_product').val()
    $.ajax({
        url: 'http://54.213.242.175:8000/add_qty/' + product + '/' + quantity,
        method: 'GET',
        success: function(response){
            if(response == -2){
                alert('Vui lòng lựa chọn phiên bản!');
            }
            else if(response == -1){
                alert('Sản phẩm không đủ số lượng!')
            }
            else if(response == -3){
                alert('Bạn không được phép mua sản phẩm này')
            }
            else if(response == -4){
                alert('Vui lòng đăng nhập để mua sản phẩm')
            }
            else{
                alert(response);
                if (confirm("Bạn muốn tiếp tục mua hàng?")) {
                    var popup = document.getElementById('popup_quickview')
                    popup.style.display = 'none'
                    $('#over').remove()
                    $.ajax({
                        url: 'http://54.213.242.175:8000/count',
                        method: 'GET',
                        success: function(response){
                            $('#cart_mobi').empty()
                            $('#cart_mobi').append('('+ response +') sản phẩm')
                            $('#cart_desk').empty()
                            $('#cart_desk').append('('+ response +') sản phẩm')
                            $('#mobile_cart').empty()
                            $('#mobile_cart').append(response)
                            $('#desktop_cart').empty()
                            $('#desktop_cart').append(response)
                        }
                    })
                } else {
                    window.location.replace('/cart')
                }
            }
        }
    })
}

