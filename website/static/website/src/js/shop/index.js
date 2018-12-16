$(document).ready(function(){
    var check_url = $(location).attr('pathname').split('/');
    var id_shop = check_url[check_url.length - 1]
    $.ajax({
        url: 'https://laberp.pythonanywhere.com/get_product_shop/' + id_shop,
        method: 'GET',
        contentType: 'application/json',
        success: function(response){
            $('#name_shop').append('Tên cửa hàng: ' + response.name)
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
                // html += '<span class="sales_percent">-15%</span>'
                html += '</div>'
                html += '<div class="quick_view">'
                html += '<button class="btn_buy" onclick="location.href=\'https://laberp.pythonanywhere.com/post/'+ response.data[i].id +'\';">Xem thêm</button>'
                //html += '<button onclick="quick_view('+ response.data[i].id +');" class="btn_quickview"><i class="fa fa-shopping-cart"></i></button>'
                // html += '<button type="submit" class="btn_buy">Mua hàng</button>'
                // html += '<a onclick="quick_view();" href=""> <button onclick="return false;" class="btn_quickview"><i class="fa fa-search"></i></button></a>'
                html += '</div>'
                html += '</div>'
                html += '</div>'
                $('#products').append(html)

                $('#pagination').empty()

                paginator = ''
                if (response.has_previous == true)
                    paginator += '<li><a href="https://laberp.pythonanywhere.com/shop/'+ id_shop +'?page='+ (response.page - 1) +'">&laquo;</a></li>'

                paginator += '<li><a>'+ response.page +'</a></li>'
                if (response.has_next == true)
                    paginator += '<li><a href="https://laberp.pythonanywhere.com/shop/'+ id_shop +'?page='+ (response.page + 1) +'">&raquo;</a></li>'
                $('#pagination').append(paginator)

                $('#total_product').empty()
                $('#total_product').append('<p>Có <b>'+ response.length +'</b> sản phẩm liên quan</p>')

                $('#name_category').empty()
                $('#name_category').append(response.name)
            }
        }
    });

})



function rating_merchant(){
    var check_url = $(location).attr('pathname').split('/');
    var id_shop = check_url[check_url.length - 1]
    data = {
        'num_star': $('#num_star').val(),
        'comment': $('#comment_text').val(),
    }
    $.ajax({
        url: 'https://laberp.pythonanywhere.com/rating_merchant_shop/' + id_shop,
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