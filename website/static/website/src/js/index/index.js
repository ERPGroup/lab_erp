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
                        html = '<div class="sales">\n'
                        html += '<div class="container">\n'
                        html += '<div class="row">\n'
                        html += '<h3 class="title_deal">Sản phẩm khuyến mãi</h3>\n'
                        html += '<div class="owl-product-sales owl-carousel owl-theme">\n'
                        posts = datas[i].posts
                        console.log(datas)
                        for (var item = 0; item < posts.length; item++){
                            html += '<div class="item">\n'
                            html += '<div class="product_box">\n'
                            html += '<div class="title_box">\n'
                            html += '<a href="#">\n'
                            html += '<p class="name_product">Tablet Plaza</p>\n'
                            html += '</a>\n'
                            html += '<p class="poster_product">3 An Dương Vương, P3, Q5</p>\n'
                            html += '<p class="square_rating">8.0</p>\n'
                            html += '</div>\n'
                            html += '<div class="thumb_image_product">\n'
                            html += '<a href="/product"><img src=""></a>\n'
                            html += '</div>\n'
                            html += '<div class="info_box">\n'
                            html += '<a href="/product" class="detail_product">\n'
                            html += '<p> Sansung Galaxy Tab A8.0 (2017) - T385</p>\n'
                            html += '</a>\n'
                            html += '<span class="price">3.000.000 d</span>\n'
                            html += '<br class="hidden_desktop">\n'
                            html += '<span class="disable_price">4.000.000 d</span>\n'
                            html += '<span class="sales_percent">15%</span>\n'
                            html += '</div>\n'
                            html += '<div class="quick_view">\n'
                            html += '<button type="submit" class="btn_buy">Mua hàng</button>\n'
                            html += '<button onclick="quick_view();" class="btn_quickview"><i class="fa fa-search"></i></button>\n'
                            html += '</div>\n'
                            html += '</div>\n'
                            html += '</div>\n'
                        }
                        html += '</div>\n'
                        html += '</div>\n'
                        html += '</div>\n'
                        html += '</div>\n'
                        console.log(html)
                        $('#by_service').append(html)
                    }
                    
                }

                if (response[located].type == 2){

                }
                        
            }
        }
    });
});