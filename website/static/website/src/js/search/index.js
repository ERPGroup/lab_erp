$(document).ready(function(){

    if(GetURLParameter('filter') == 'true'){
        $('#price_from').val(GetURLParameter('min'))
        $('#price_to').val(GetURLParameter('max'))
    }

    url = 'https://laberp.pythonanywhere.com/f_search?r=' + GetURLParameter('r') + '&';
    if (GetURLParameter('page') == undefined){
        if(GetURLParameter('newest') != undefined){
            url += 'newest=' + GetURLParameter('newest')
        }
        if(GetURLParameter('buiest') != undefined){
            url += 'buiest=' + GetURLParameter('buiest')
        }
        if(GetURLParameter('pricest') != undefined){
            url += 'pricest=' + GetURLParameter('pricest')
        }
        if(GetURLParameter('filter') == 'true'){
            url += 'filter=' + GetURLParameter('filter') + '&min=' + GetURLParameter('min') + '&max=' + GetURLParameter('max')
        }
    }
    else{
        url += 'page='+ GetURLParameter('page') + '&'
        if(GetURLParameter('newest') != undefined){
            url += 'newest=' + GetURLParameter('newest')
        }
        if(GetURLParameter('buiest') != undefined){
            url += 'buiest=' + GetURLParameter('buiest')
        }
        if(GetURLParameter('pricest') != undefined){
            url += 'pricest=' + GetURLParameter('pricest')
        }
        if(GetURLParameter('filter') == 'true'){
            url += 'filter=' + GetURLParameter('filter') + '&min=' + GetURLParameter('min') + '&max=' + GetURLParameter('max')
        }
    }

    console.log(url)
    $.ajax({
        url: url,
        method: 'GET',
        contentType: 'application/json',
        success: function(response){
            //console.log(response);
            for( var i = 0 ; i < response.data.length; i++){
                html = '<div class="col-xs-6 col-sm-6 col-md-4 col-lg-4 no_padding">'
                html += '<div class="product_box">'
                html += '<div class="title_box">'
                if(response.data[i].vip == true)
                    html += '<a ><p class="name_shop text-center">Tin Vip</p></a>'
                else
                    html += '<a ><p class="name_shop text-center">Tin Thường</p></a>'
                html += '<p class="square_rating">'+ response.data[i].rating +'</p>'
                html += '</div>'
                html += '<div class="thumb_image_product">'
                html += '<a href="/product"><img src="'+ response.data[i].product.image +'"></a>'
                html += '</div>'
                html += '<div class="info_box">'
                html += '<a href="/product/'+ response.data[i].product.id +'" class="detail_product">'
                html += '<p>'+ response.data[i].product.name +'</p>'
                html += '</a>'
                if (response.data[i].product.range_price[0] == response.data[i].product.range_price[1]){
                    html += '<span class="price">'+ currency(((response.data[i].product.range_price[0] * (100 - response.data[i].product.discount_percent))/100), { precision: 0, separator: ',' }).format() +' VND </span>'
                }
                else{
                    html += '<span class="price">'+ currency((response.data[i].product.range_price[1] * (100 - response.data[i].product.discount_percent))/100, { precision: 0, separator: ',' }).format() + ' - ' +  currency((response.data[i].product.range_price[0] * (100 - response.data[i].product.discount_percent))/100, { precision: 0, separator: ',' }).format() +' VND </span>'
                }
                
                // html += '<span class="price">'+ response.data[i].product.price +' VND</span>'
                // html += '<br class="hidden_desktop">'
                // html += '<span class="disable_price">4.000.000 d</span>'
                html += '<span class="sales_percent">-'+ response.data[i].product.discount_percent +'%</span>'
                html += '</div>'
                html += '<div class="quick_view">'
                html += '<button class="btn_buy" onclick="location.href=\'https://laberp.pythonanywhere.com/post/'+ response.data[i].id +'\';">Xem thêm</button>'
                html += '<button onclick="quick_view('+ response.data[i].id +');" class="btn_quickview"><i class="fa fa-shopping-cart"></i></button>'
                // html += '<button type="submit" class="btn_buy">Mua hàng</button>'
                // html += '<a onclick="quick_view();" href=""> <button onclick="return false;" class="btn_quickview"><i class="fa fa-search"></i></button></a>'
                html += '</div>'
                html += '</div>'
                html += '</div>'
                $('#products').append(html)

                $('#pagination').empty()

                url_paginator = 'https://laberp.pythonanywhere.com/search?' + GetURLParameter('r') + '&';;
                if(GetURLParameter('newest') != undefined){
                    url_paginator += 'newest=' + GetURLParameter('newest') + '&'
                }
                if(GetURLParameter('buiest') != undefined){
                    url_paginator += 'buiest=' + GetURLParameter('buiest') + '&'
                }
                if(GetURLParameter('pricest') != undefined){
                    url_paginator += 'pricest=' + GetURLParameter('pricest') + '&'
                }
                if(GetURLParameter('filter') == 'true'){
                    url_paginator += 'filter=' + GetURLParameter('filter') + '&min=' + GetURLParameter('min') + '&max=' + GetURLParameter('max') + '&'
                }
                paginator = ''
                if (response.has_previous == true)
                    paginator += '<li><a href="'+ url_paginator +'page='+ (response.page - 1) +'">&laquo;</a></li>'

                paginator += '<li><a>'+ response.page +'</a></li>'
                if (response.has_next == true)
                    paginator += '<li><a href="'+ url_paginator +'page='+ (response.page + 1) +'">&raquo;</a></li>'
                $('#pagination').append(paginator)

                $('#total_product').empty()
                $('#total_product').append('<p>Có <b>'+ response.length +'</b> sản phẩm liên quan</p>')

                $('#name_category').empty()
                $('#name_category').append(response.name)
            }
        }
    });

    $("#newest").on('click', Newest_down)
    $("#buiest").on('click', Buiest_down)
    $("#pricest").on('click', Pricest_down)

    if(GetURLParameter('newest') == 'true'){
        $('#newest').empty()
        $('#newest').append('<a>Mới nhất <i class="fa fa-arrow-up"></i></a>')
        $("#newest").off('click').on('click', Newest_up)
    }
    else{
        $('#newest').empty()
        $('#newest').append('<a>Mới nhất <i class="fa fa-arrow-down"></i></a>')
        $("#newest").off('click').on('click', Newest_down)
    }

    if(GetURLParameter('buiest') == 'true'){
        $('#buiest').empty()
        $('#buiest').append('<a >Bán chạy nhất<i class="fa fa-arrow-up"></i></a>')
        $("#buiest").off('click').on('click', Buiest_up)
    }
    else{
        $('#buiest').empty()
        $('#buiest').append('<a >Bán chạy nhất<i class="fa fa-arrow-down"></i></a>')
        $("#buiest").off('click').on('click', Buiest_down)
    }

    if(GetURLParameter('pricest') == 'true'){
        $('#pricest').empty()
        $('#pricest').append('<a >Giá bán<i class="fa fa-arrow-up"></i></a>')
        $("#pricest").off('click').on('click', Pricest_up)
    }
    else{
        $('#pricest').empty()
        $('#pricest').append('<a >Giá bán<i class="fa fa-arrow-down"></i></a>')
        $("#pricest").off('click').on('click', Pricest_down)
    }

})

function Newest_down() {
    if(GetURLParameter('filter')){
        alert('Xin lỗi!\nChúng tôi chưa hỗ trợ chức năng này cho lọc giá!')
        return
    }
    url = 'https://laberp.pythonanywhere.com/search?r=' + GetURLParameter('r') + '&';
    if (GetURLParameter('page') == undefined){
        url += 'newest=true&'
    }
    else{
        url += 'newest=true&' + 'page='+ GetURLParameter('page')
    }
    document.location = url;
}

function Newest_up() {
    if(GetURLParameter('filter')){
        alert('Xin lỗi!\nChúng tôi chưa hỗ trợ chức năng này cho lọc giá!')
        return
    }
    url = 'https://laberp.pythonanywhere.com/search?r=' + GetURLParameter('r') + '&';
    if (GetURLParameter('page') == undefined){
        url += 'newest=false&'
    }
    else{
        url += 'newest=false&' + 'page='+ GetURLParameter('page')
    }
    document.location = url;
}


function Buiest_down() {
    if(GetURLParameter('filter')){
        alert('Xin lỗi!\nChúng tôi chưa hỗ trợ chức năng này cho lọc giá!')
        return
    }
    url = 'https://laberp.pythonanywhere.com/search?r=' + GetURLParameter('r') + '&';
    if (GetURLParameter('page') == undefined){
        url += 'buiest=true&'
    }
    else{
        url += 'buiest=true&' + 'page='+ GetURLParameter('page')
    }
    document.location = url;
}

function Buiest_up() {
    if(GetURLParameter('filter')){
        alert('Xin lỗi!\nChúng tôi chưa hỗ trợ chức năng này cho lọc giá!')
        return
    }
    url = 'https://laberp.pythonanywhere.com/search?r=' + GetURLParameter('r') + '&';
    if (GetURLParameter('page') == undefined){
        url += 'buiest=false&'
    }
    else{
        url += 'buiest=false&' + 'page='+ GetURLParameter('page')
    }
    document.location = url;
}


function Pricest_down() {
    if(GetURLParameter('filter')){
        alert('Xin lỗi!\nChúng tôi chưa hỗ trợ chức năng này cho lọc giá!')
        return
    }
    url = 'https://laberp.pythonanywhere.com/search?r=' + GetURLParameter('r') + '&';
    if (GetURLParameter('page') == undefined){
        url += 'pricest=true&'
    }
    else{
        url += 'pricest=true&' + 'page='+ GetURLParameter('page')
    }
    document.location = url;
}

function Pricest_up() {
    if(GetURLParameter('filter')){
        alert('Xin lỗi!\nChúng tôi chưa hỗ trợ chức năng này cho lọc giá!')
        return
    }
    url = 'https://laberp.pythonanywhere.com/search?r=' + GetURLParameter('r') + '&';
    if (GetURLParameter('page') == undefined){
        url += 'pricest=false&'
    }
    else{
        url += 'pricest=false&' + 'page='+ GetURLParameter('page')
    }
    document.location = url;
}


function Filter_price() {
    url = 'https://laberp.pythonanywhere.com/search?r=' + GetURLParameter('r') + '&';
    var price_from = $('#price_from').val()
    if (price_from == ''){
        alert('Vui lòng nhập giá!')
        return
    }
    var price_to = $('#price_to').val()
    if (price_to == ''){
        alert('Vui lòng nhập giá!')
        return
    }
    if (parseInt(price_from) >= parseInt(price_to)){
        alert('Mức giá không hợp lệ!')
        return
    }
    if (GetURLParameter('page') == undefined){
        url += 'filter=true&min='+ price_from +'&max='+ price_to
    }
    else{
        url += 'filter=true&min='+ price_from +'&max='+ price_to + '&page='+ GetURLParameter('page')
    }
    document.location = url;
}

function Cancel_Filter(){
    url = 'https://laberp.pythonanywhere.com/search?r=' + GetURLParameter('r') + '&';
    document.location = url;
}


function GetURLParameter(sParam){
    var sPageURL = window.location.search.substring(1)
    var sURLVariables = sPageURL.split('&')
    for (var i = 0; i < sURLVariables.length; i++){
        var sParameterName = sURLVariables[i].split('=')
        if (sParameterName[0] == sParam){
            return sParameterName[1]
        }
    }
}

function quick_view (id_post) {
    var popup = document.getElementById('popup_quickview')
    popup.style.display = 'block'
    $('body').append('<div id="over">')
    $('#over').fadeIn(300)

    $.ajax({
        url: 'https://laberp.pythonanywhere.com/post_data/' + id_post,
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
                if (i == 5) break;
                attributes_html += response.product.version[0].attributes[i].label + ' : ' + response.product.version[0].attributes[i].value + '<br />'
            }
            attributes_html += '<li><a href="/post/'+ id_post +'">Xem thêm</a><li>'
            $('#attributes').append(attributes_html);
            $('#price').empty()
            $('#price').append(currency(((response.product.version[0].price * (100 - response.product.discount_percent))/100), { precision: 0, separator: ',' }).format() + ' VND')

            $('#form_quickview').empty()
            html_choice_qty = '<input type="hidden" id="version_product" value="'+ response.product.version[0].id_product +'">'
            html_choice_qty += '<button onclick="sub_product()" class="button_add">-</button>'
            html_choice_qty += '<input value="1" class="input_add" maxlength="3" size="1" name="quantity" id="input_quantity">'
            html_choice_qty += '<button onclick="add_product('+ (response.quantity - response.bought) +')" class="button_add">+</button>'
            html_choice_qty += '<button onclick="buy_product()" class="btn_buy">Mua hàng</button>'
            $('#form_quickview').append(html_choice_qty)


            $('#quantity').empty()
            $('#quantity').append('<a>'+ (response.quantity - response.bought) +' sản phẩm</a>')
            $('#merchant').empty()
            $('#merchant').append('<a href="/shop/'+ response.merchant.id +'">'+ response.merchant.name_shop +'</a>')
        }
    })
}



function sub_product(){
    var qty = parseInt($('#input_quantity').val());
    if (qty <= 1) return
    $('#input_quantity').val(qty -1);
}
  
function add_product(qty_aval){
    var qty = parseInt($('#input_quantity').val()); 
    if (qty >= qty_aval) return
    $('#input_quantity').val(qty + 1);
}


function get_attr(item){
    var id_post = $('#version').attr('data-post')
    $.ajax({
        url: 'https://laberp.pythonanywhere.com/post_data/' + id_post,
        method: 'GET',
        contentType: 'application/json',
        success: function(response){
            $('#attributes').empty()
            attributes_html = ''
            for(var i = 0; i < response.product.version[item].attributes.length; i++){
                if (i == 5) break;
                attributes_html += response.product.version[item].attributes[i].label + ' : ' + response.product.version[item].attributes[i].value + '<br />'
            }
            attributes_html += '<li><a href="/post/'+ id_post +'">Xem thêm</a><li>'
            $('#attributes').append(attributes_html);
            $('#price').empty()
            $('#price').append(currency(((response.product.version[item].price * (100 - response.product.discount_percent))/100), { precision: 0, separator: ',' }).format() + ' VND')
            
            $('#version_product').val(response.product.version[item].id_product)
        }
    });
}


function buy_product(){
    var quantity = $('#input_quantity').val()
    var product = $('#version_product').val()
    $.ajax({
        url: 'https://laberp.pythonanywhere.com/add_qty/' + product + '/' + quantity,
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
                        url: 'https://laberp.pythonanywhere.com/count',
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

