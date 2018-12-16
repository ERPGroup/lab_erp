$(document).ready(function () {
    $.ajax({
        url: 'https://laberp.pythonanywhere.com/data',
        method: 'GET',
        contentType: 'application/json',
        success: function (response) {
            console.log(response)
            for (var located = 0; located < response.length; located++) {
                if (response[located].type == 1) {
                    datas = response[located].data
                    for (var i = 0; i < datas.length; i++) {
                        html = '<div class="service_' + datas[i].id + '">'
                        html += '<div class="container">'
                        html += '<div class="row">'
                        html += '<h3 class="title_deal text-capitalize">' + datas[i].service_name + '</h3>'
                        html += '<div class="owl-product-sales owl-carousel owl-theme">'
                        posts = datas[i].posts

                        for (var item = 0; item < posts.length; item++) {
                            html += '<div class="item">'
                            html += '<div class="product_box is_palatinum">'
                            html += '<div class="title_box">'
                            html += '<a href="/shop/'+posts[item].creator_id_id+'"><p class="name_shop text-center"> SHOP '+posts[item].creator_id_id+'</p></a>'
                            html += '<p class="square_rating">' + posts[item].rating + '</p>'
                            html += '</div>'
                            html += '<div class="thumb_image_product">'
                            html += '<a><img src="' + posts[item].product.image + '"></a>'
                            html += '</div>'
                            html += '<div class="info_box">'
                            html += '<a href="/post/' + posts[item].id + '" class="detail_product">'
                            html += '<p>' + posts[item].product.name + '</p>'
                            html += '</a>'
                            if (posts[item].product.range_price[0] == posts[item].product.range_price[1]){
                                html += '<span class="price">'+ currency(((posts[item].product.range_price[0] * (100 - posts[item].product.discount_percent))/100), { precision: 0, separator: ',' }).format() +' VND </span>'
                            }
                            else{
                                html += '<span class="price">'+ currency((posts[item].product.range_price[1] * (100 - posts[item].product.discount_percent))/100, { precision: 0, separator: ',' }).format() + ' - ' +  currency((posts[item].product.range_price[0] * (100 - posts[item].product.discount_percent))/100, { precision: 0, separator: ',' }).format() +' VND </span>'
                            }
                            
                            // html += '<br class="hidden_desktop">'
                            // html += '<span class="disable_price">4.000.000 d</span>'
                            if (posts[item].product.discount_percent != 0) {
                                html += '<span class="sales_percent">-' + posts[item].product.discount_percent + '%</span>'
                            }
                            html += '</div>'
                            html += '<div class="quick_view">'
                            html += '<button class="btn_buy" onclick="location.href=\'https://laberp.pythonanywhere.com/post/' + posts[item].id + '\';">Xem thêm</button>'
                            html += '<button onclick="quick_view(' + posts[item].id + ');" class="btn_quickview"><i class="fa fa-shopping-cart"></i></button>'
                            html += '</div>'
                            html += '</div>'
                            html += '</div>'
                        }
                        html += '</div>'
                        html += '</div>'
                        html += '</div>'
                        html += '</div>'
                        $('#by_service').append(html)

                        $('.owl-product-sales').owlCarousel({
                            loop: true,
                            margin: 10,
                            responsiveClass: true,
                            owl2row: true,
                            responsive: {
                                0: {
                                    items: 1,
                                    nav: true
                                },
                                600: {
                                    items: 2,
                                    nav: false
                                },
                                1000: {
                                    items: 4,
                                    nav: true,
                                    loop: false
                                }
                            }
                        })
                    }

                }

                if (response[located].type == 2) {
                    datas = response[located].data
                    for (var i = 0; i < datas.length; i++) {
                        html = '<div class="service_' + datas[i].id + '">'
                        html += '<div class="container">'
                        html += '<div class="row">'
                        html += '<h3 class="title_deal text-capitalize">' + datas[i].name_category + ' | <a class="view_more" href="/collections/' + datas[i].id + '">Xem thêm</a></h3>'
                        html += '<div class="owl-product-sales owl-carousel owl-theme">'
                        posts = datas[i].posts

                        for (var item = 0; item < posts.length; item++) {
                            html += '<div class="item">'
                            html += '<div class="product_box is_gold">'
                            html += '<div class="title_box">'
                            html += '<a ><p class="name_shop text-center">Tin Vip</p></a>'
                            html += '<p class="square_rating">' + posts[item].rating + '</p>'
                            html += '</div>'
                            html += '<div class="thumb_image_product">'
                            html += '<a><img src="' + posts[item].product.image + '"></a>'
                            html += '</div>'
                            html += '<div class="info_box">'
                            html += '<a href="/post/' + posts[item].id + '" class="detail_product">'
                            html += '<p>' + posts[item].product.name + '</p>'
                            html += '</a>'
                            if (posts[item].product.range_price[0] == posts[item].product.range_price[1]){
                                html += '<span class="price">'+ currency(((posts[item].product.range_price[0] * (100 - posts[item].product.discount_percent))/100), { precision: 0, separator: ',' }).format() +' VND </span>'
                            }
                            else{
                                html += '<span class="price">'+ currency((posts[item].product.range_price[1] * (100 - posts[item].product.discount_percent))/100, { precision: 0, separator: ',' }).format() + ' - ' +  currency((posts[item].product.range_price[0] * (100 - posts[item].product.discount_percent))/100, { precision: 0, separator: ',' }).format() +' VND </span>'
                            }
                            // html += '<br class="hidden_desktop">'
                            // html += '<span class="disable_price">4.000.000 d</span>'
                            if (posts[item].product.discount_percent != 0) {
                                html += '<span class="sales_percent">-' + posts[item].product.discount_percent + '%</span>'
                            }
                            html += '</div>'
                            html += '<div class="quick_view">'
                            html += '<button class="btn_buy" onclick="location.href=\'https://laberp.pythonanywhere.com/post/' + posts[item].id + '\';">Xem thêm</button>'
                            html += '<button onclick="quick_view(' + posts[item].id + ');" class="btn_quickview"><i class="fa fa-shopping-cart"></i></button>'
                            html += '</div>'
                            html += '</div>'
                            html += '</div>'
                        }
                        html += '</div>'
                        html += '</div>'
                        html += '</div>'
                        html += '</div>'
                        $('#by_category').append(html)

                        $('.owl-product-sales').owlCarousel({
                            loop: true,
                            margin: 10,
                            responsiveClass: true,
                            responsive: {
                                0: {
                                    items: 1,
                                    nav: true
                                },
                                600: {
                                    items: 2,
                                    nav: false
                                },
                                1000: {
                                    items: 4,
                                    nav: true,
                                    loop: false
                                }
                            }
                        })
                    }
                }

            }
        }
    });



});

function quick_view(id_post) {
    var popup = document.getElementById('popup_quickview')
    popup.style.display = 'block'
    $('body').append('<div id="over">')
    $('#over').fadeIn(300)

    $.ajax({
        url: 'https://laberp.pythonanywhere.com/post_data/' + id_post,
        method: 'GET',
        contentType: 'application/json',
        success: function (response) {
            console.log(response)
            $('#name_product').empty()
            $('#name_product').append(response.product.name)


            datas = [];
            for (var item = 0; item < response.product.images.length; item++) {
                datas.push({
                    img: '/product/' + response.product.images[item].image_link,
                    thumb: '/product/' + response.product.images[item].image_link
                })
            }
            // Load data -- API 
            var $fotoramaDiv = $('#list_images').fotorama();
            var fotorama = $fotoramaDiv.data('fotorama');
            fotorama.load(datas)

            version_html = ''
            $('#version').empty()
            for (var item = 0; item < response.product.version.length; item++) {
                if (item == 0)
                    version_html += '<option selected="selected" value="' + item + '" >' + response.product.version[item].name_product + '</option>'
                else
                    version_html += '<option value="' + item + '" >' + response.product.version[item].name_product + '</option>'
            }
            $('#version').append(version_html)
            $('#version').attr('data-post', response.id)

            $('#attributes').empty()
            attributes_html = ''
            for (var i = 0; i < response.product.version[0].attributes.length; i++) {
                if (i == 5) break;
                attributes_html += response.product.version[0].attributes[i].label + ' : ' + response.product.version[0].attributes[i].value + '<br />'
            }
            attributes_html += '<li><a href="/post/' + id_post + '">Xem thêm</a><li>'
            $('#attributes').append(attributes_html);
            $('#price').empty()
            $('#price').append(currency(((response.product.version[0].price * (100 - response.product.discount_percent)) / 100), {
                precision: 0,
                separator: ','
            }).format() + ' VND')

            $('#form_quickview').empty()
            html_choice_qty = '<input type="hidden" id="version_product" value="' + response.product.version[0].id_product + '">'
            html_choice_qty += '<button onclick="sub_product()" class="button_add">-</button>'
            html_choice_qty += '<input value="1" class="input_add" maxlength="3" size="1" name="quantity" id="input_quantity">'
            html_choice_qty += '<button onclick="add_product(' + (response.quantity - response.bought) + ')" class="button_add">+</button>'
            html_choice_qty += '<button onclick="buy_product()" class="btn_buy">Mua hàng</button>'
            $('#form_quickview').append(html_choice_qty)


            $('#quantity').empty()
            $('#quantity').append('<a>' + (response.quantity - response.bought) + ' sản phẩm</a>')
            $('#merchant').empty()
            $('#merchant').append('<a href="">' + response.merchant.name_shop + '</a>')
        }
    })
}

function get_attr(item) {
    var id_post = $('#version').attr('data-post')
    $.ajax({
        url: 'https://laberp.pythonanywhere.com/post_data/' + id_post,
        method: 'GET',
        contentType: 'application/json',
        success: function (response) {
            $('#attributes').empty()
            attributes_html = ''
            for (var i = 0; i < response.product.version[item].attributes.length; i++) {
                if (i == 5) break;
                attributes_html += response.product.version[item].attributes[i].label + ' : ' + response.product.version[item].attributes[i].value + '<br />'
            }
            attributes_html += '<li><a href="/post/' + id_post + '">Xem thêm</a><li>'
            $('#attributes').append(attributes_html);
            $('#price').empty()
            $('#price').append(currency(((response.product.version[item].price * (100 - response.product.discount_percent))/100), { precision: 0, separator: ',' }).format() + ' VND')
            
            $('#version_product').val(response.product.version[item].id_product)
        }
    });
}

function sub_product() {
    var qty = parseInt($('#input_quantity').val());
    if (qty <= 1) return
    $('#input_quantity').val(qty - 1);
}

function add_product(qty_aval) {
    var qty = parseInt($('#input_quantity').val());
    if (qty >= qty_aval) return
    $('#input_quantity').val(qty + 1);
}



function buy_product() {
    var quantity = $('#input_quantity').val()
    var product = $('#version_product').val()
    $.ajax({
        url: 'https://laberp.pythonanywhere.com/add_qty/' + product + '/' + quantity,
        method: 'GET',
        success: function (response) {
            if (response == -2) {
                alert('Vui lòng lựa chọn phiên bản!');
            } else if (response == -1) {
                alert('Sản phẩm không đủ số lượng!')
            } else if (response == -3) {
                alert('Bạn không được phép mua sản phẩm này')
            } else if (response == -4) {
                alert('Vui lòng đăng nhập để mua sản phẩm')
            } else {
                alert(response);
                if (confirm("Bạn muốn tiếp tục mua hàng?")) {
                    var popup = document.getElementById('popup_quickview')
                    popup.style.display = 'none'
                    $('#over').remove()
                    $.ajax({
                        url: 'https://laberp.pythonanywhere.com/count',
                        method: 'GET',
                        success: function (response) {
                            $('#cart_mobi').empty()
                            $('#cart_mobi').append('(' + response + ') sản phẩm')
                            $('#cart_desk').empty()
                            $('#cart_desk').append('(' + response + ') sản phẩm')
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