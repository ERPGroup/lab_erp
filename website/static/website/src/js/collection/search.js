$(document).ready(function(){
    var check_url = $(location).attr('pathname').split('/');
    var id_category = check_url[check_url.length - 1]
    if (GetURLParameter('page') == undefined)
        page = ''
    else
        page = 'page='+ GetURLParameter('page')

    console.log(page)
    $('.advanced_search').change(function(){
        price_from = $('#price_from').val(),
        price_to = $('#price_to').val()    
        data={
            'price_from':price_from,
            'price_to':price_to,
        }

        if(price_from.length==0 || price_from===null){
            data['price_from']=0
        }
        if(price_to.length==0 || price_to===null){
            data['price_to']=99000000
        }
        

        $('#products').empty();
        $.ajax({
            url: 'http://localhost:8000/advanced_search/'+ id_category + '?' + page,
            method: 'GET',
            contentType: 'application/json',
            data:data,
            success: function(response){
                console.log(response);
                for( var i = 0 ; i < response.data.length; i++){
                    html = '<div class="col-xs-6 col-sm-6 col-md-4 col-lg-4 no_padding">'
                    html += '<div class="product_box">'
                    html += '<div class="title_box">'
                    html += '<a href="#">'
                    html += '<p class="name_product">Tablet Plaza</p>'
                    html += '</a>'
                    html += '<p class="poster_product">3 An Dương Vương, P3, Q5</p>'
                    html += '<p class="square_rating">8.0</p>'
                    html += '</div>'
                    html += '<div class="thumb_image_product">'
                    html += '<a href="/product"><img src="'+ response.data[i].product.image +'"></a>'
                    html += '</div>'
                    html += '<div class="info_box">'
                    html += '<a href="/product/'+ response.data[i].product.id +'" class="detail_product">'
                    html += '<p>'+ response.data[i].product.name +'</p>'
                    html += '</a>'
                    html += '<span class="price">'+ response.data[i].product.price +' VND</span>'
                    // html += '<br class="hidden_desktop">'
                    // html += '<span class="disable_price">4.000.000 d</span>'
                    // html += '<span class="sales_percent">-15%</span>'
                    html += '</div>'
                    html += '<div class="quick_view">'
                    html += '<button type="submit" class="btn_buy">Mua hàng</button>'
                    html += '<a onclick="quick_view();" href=""> <button onclick="return false;" class="btn_quickview"><i class="fa fa-search"></i></button></a>'
                    html += '</div>'
                    html += '</div>'
                    html += '</div>'
                    $('#products').append(html)
    
                    $('#pagination').empty()
                    paginator = ''
                    if (response.has_previous == true)
                        /*paginator += '<li><a href="/advanced_search/'+ id_category +'?page='+ (response.page - 1) +'">&laquo;</a></li>'*/
                        paginator += '<li><a href="/advanced_search/'+ id_category +'?price_from='+data.price_from +'&price_to='+data.price_to +'&page='+ (response.page - 1) +'">&laquo;</a></li>'

                    paginator += '<li><a>'+ response.page +'</a></li>'
                    if (response.has_next == true)
                        paginator += '<li><a href="/advanced_search/'+ id_category +'?price_from='+data.price_from +'&price_to='+data.price_to +'&page='+ (response.page + 1) +'">&raquo;</a></li>'
                    $('#pagination').append(paginator)
    
                    $('#total_product').empty()
                    $('#total_product').append('<p>Có <b>'+ response.length +'</b> sản phẩm liên quan</p>')
    
                    $('#name_category').empty()
                    $('#name_category').append(response.name)
                }
            }
        });
    })

})