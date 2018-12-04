$(document).ready(function(){
    $.ajax({
        url: 'http://localhost:8000/data',
        method: 'GET',
        contentType: 'application/json',
        success: function(response){
            console.log(response)
            for(var located = 0; located < response.length; located++){
                if (response[located].type == 1){
                    datas = response[located].data
                    for(var i = 0; i < datas.length; i++){
                        html = '<div class="service_'+ datas[i].id +'">'
                        html += '<div class="container">'
                        html += '<div class="row">'
                        html += '<h3 class="title_deal">Sản phẩm khuyến mãi</h3>'
                        html += '<div class="owl-product-sales owl-carousel owl-theme">'
                        posts = datas[i].posts
                        
                        for (var item = 0; item < posts.length; item++){
                            html += '<div class="item">'
                            html += '<div class="product_box">'
                            html += '<div class="title_box">'
                            html += '<a href="#"><p class="name_product">Tablet Plaza</p></a>'
                            html += '<p class="poster_product">3 An Dương Vương, P3, Q5</p>'
                            html += '<p class="square_rating">8.0</p>'
                            html += '</div>'
                            html += '<div class="thumb_image_product">'
                            html += '<a href="/product"><img src="'+ posts[item].product.image +'"></a>'
                            html += '</div>'
                            html += '<div class="info_box">'
                            html += '<a href="/product" class="detail_product">'
                            html += '<p>'+ posts[item].product.name +'</p>'
                            html += '</a>'
                            html += '<span class="price">'+ posts[item].product.price +'</span>'
                            // html += '<br class="hidden_desktop">'
                            // html += '<span class="disable_price">4.000.000 d</span>'
                            // html += '<span class="sales_percent">15%</span>'
                            html += '</div>'
                            html += '<div class="quick_view">'
                            html += '<button class="btn_buy" onclick="location.href=\'http://localhost:8000/post/'+ posts[item].id +'\';">Xem thêm</button>'
                            html += '<button onclick="quick_view('+ posts[item].id +');" class="btn_quickview"><i class="fa fa-shopping-cart"></i></button>'
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
                            loop:true,
                            margin:10,
                            responsiveClass:true,
                            owl2row: true,
                            responsive:{
                                0:{
                                    items:1,
                                    nav:true
                                },
                                600:{
                                    items:3,
                                    nav:false
                                },
                                1000:{
                                    items:5,
                                    nav:true,
                                    loop:false
                                }
                            }
                        })
                    }
                    
                }

                if (response[located].type == 2){
                    datas = response[located].data
                    for(var i = 0; i < datas.length; i++){
                        html = '<div class="service_'+ datas[i].id +'">'
                        html += '<div class="container">'
                        html += '<div class="row">'
                        html += '<h3 class="title_deal">'+ datas[i].name_category +' | <a class="view_more" href="/collections/'+ datas[i].id +'">Xem thêm</a></h3>'
                        html += '<div class="owl-product-sales owl-carousel owl-theme">'
                        posts = datas[i].posts
                        
                        for (var item = 0; item < posts.length; item++){
                            html += '<div class="item">'
                            html += '<div class="product_box">'
                            html += '<div class="title_box">'
                            html += '<a href="#"><p class="name_product">Tablet Plaza</p></a>'
                            html += '<p class="poster_product">3 An Dương Vương, P3, Q5</p>'
                            html += '<p class="square_rating">8.0</p>'
                            html += '</div>'
                            html += '<div class="thumb_image_product">'
                            html += '<a href="/product"><img src="'+ posts[item].product.image +'"></a>'
                            html += '</div>'
                            html += '<div class="info_box">'
                            html += '<a href="/product" class="detail_product">'
                            html += '<p>'+ posts[item].product.name +'</p>'
                            html += '</a>'
                            html += '<span class="price">'+ posts[item].product.price +'</span>'
                            // html += '<br class="hidden_desktop">'
                            // html += '<span class="disable_price">4.000.000 d</span>'
                            // html += '<span class="sales_percent">15%</span>'
                            html += '</div>'
                            html += '<div class="quick_view">'
                            html += '<button class="btn_buy" onclick="location.href=\'http://localhost:8000/post/'+ posts[item].id +'\';">Xem thêm</button>'
                            html += '<button onclick="quick_view('+ posts[item].id +');" class="btn_quickview"><i class="fa fa-shopping-cart"></i></button>'
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
                            loop:true,
                            margin:10,
                            responsiveClass:true,
                            responsive:{
                                0:{
                                    items:1,
                                    nav:true
                                },
                                600:{
                                    items:3,
                                    nav:false
                                },
                                1000:{
                                    items:5,
                                    nav:true,
                                    loop:false
                                }
                            }
                        })
                    }
                }
                        
            }
        }
    });



});

function quick_view (id_post) {
    var popup = document.getElementById('popup_quickview')
    popup.style.display = 'block'
    $('body').append('<div id="over">')
    $('#over').fadeIn(300)

    $.ajax({
        url: 'http://localhost:8000/post_data/' + id_post,
        method: 'GET',
        contentType: 'application/json',
        success: function(response){
            console.log(response)
            $('#name_product').empty()
            $('#name_product').append(response.product.name)


            datas = [];
            for(var item = 0; item < response.product.images.length; item++){
                datas.push({img: '/product/'+ response.product.images[item].image_link, thumb: '/product/'+ response.product.images[item].image_link})
            }
            // Load data -- API 
            var $fotoramaDiv = $('#list_images').fotorama();
            var fotorama = $fotoramaDiv.data('fotorama');
            fotorama.load(datas)

            version_html = ''
            $('#version').empty()
            for(var item = 0; item < response.product.version.length; item++){
                if (item == 0)
                    version_html += '<option selected="selected" value="'+ item +'" >'+ response.product.version[item].name_product +'</option>'
                else
                    version_html += '<option value="'+ item +'" >'+ response.product.version[item].name_product +'</option>'
            }
            $('#version').append(version_html)
            $('#version').attr('data-post', response.id)

            $('#attributes').empty()
            attributes_html = ''
            for(var i = 0; i < response.product.version[0].attributes.length; i++){
                if (i == 2) return;
                attributes_html += response.product.version[0].attributes[i].label + ' : ' + response.product.version[0].attributes[i].value
            }
            attributes_html += '<li><a href="/post/'+ id_post +'">Xem thêm</a><li>'
            $('#attributes').append(attributes_html);
            $('#price').empty()
            $('#price').append(response.product.version[0].price + ' VND')

            $('#form_quickview').empty()
            html_choice_qty = '<input type="hidden" id="version_product" value="'+ response.product.version[0].id_product +'">'
            html_choice_qty += '<button onclick="sub_product()" class="button_add">-</button>'
            html_choice_qty += '<input value="1" class="input_add" maxlength="3" size="1" name="quantity" id="quantity">'
            html_choice_qty += '<button onclick="add_product('+ (response.quantity - response.bought) +')" class="button_add">+</button>'
            html_choice_qty += '<button onclick="buy_product()" class="btn_buy">Mua hàng</button>'
            $('#form_quickview').append(html_choice_qty)


            $('#quantity').empty()
            $('#quantity').append('<a>'+ (response.quantity - response.bought) +' sản phẩm</a>')
            $('#merchant').empty()
            $('#merchant').append('<a href="">'+ response.merchant.name_shop +'</a>')
        }
    })

    
}

function get_attr(item){
    var id_post = $('#version').attr('data-post')
    $.ajax({
        url: 'http://localhost:8000/post_data/' + id_post,
        method: 'GET',
        contentType: 'application/json',
        success: function(response){
            $('#attributes').empty()
            attributes_html = ''
            for(var i = 0; i < response.product.version[item].attributes.length; i++){
                if (i == 2) return;
                attributes_html += response.product.version[item].attributes[i].label + ' : ' + response.product.version[item].attributes[i].value
            }
            attributes_html += '<li><a href="/post/'+ id_post +'">Xem thêm</a><li>'
            $('#attributes').append(attributes_html);
            $('#price').empty()
            $('#price').append(response.product.version[item].price + ' VND')
            
            $('#version_product').val(response.product.version[item].id_product)
        }
    });
}

function sub_product(){
    var qty = parseInt($('#quantity').val());
    if (qty <= 1) return
    $('#quantity').val(qty -1);
}
  
function add_product(qty_aval){
    var qty = parseInt($('#quantity').val()); 
    if (qty >= qty_aval) return
    $('#quantity').val(qty + 1);
}



function buy_product(){
    var quantity = $('quantity').val()
    var product = $('#version_product').val()

}