$(document).ready(function(){
    var check_url = $(location).attr('pathname').split('/');
    var id_post = check_url[check_url.length - 1]


    $.ajax({
        url: 'http://54.213.242.175:8000/merchant/post/' + id_post,
        method: 'GET',
        contentType: 'application/json',
        success: function(response){
            console.log((response[0]['fields'].expire.split('T')));

            post = response[0]['fields']

            //Load Product
            $.ajax({
                url: 'http://54.213.242.175:8000/merchant/product/' + post.product_id ,
                method: 'GET',
                contentType: 'application/json',
                success: function(response){
                    $('#products').append('<option value="'+ response.id +'" selected="selected">'+ response['code'] + ' - ' + response['name'] +'</option>')
                    showProduct(response.id);
                }
            }) 


            // load Service
            $.ajax({
                url: 'http://54.213.242.175:8000/merchant/account_services?service=available',
                method: 'GET',
                contentType: 'application/json',
                success: function(response){

                    for(var i = 0; i < response.length; i++)
                        if(post.post_type == response[i]['service_id'])
                            $('#services').append('<option value="'+ response[i]['service_id'] +'" selected="selected">'+ response[i]['service_name'] + ' | ' + response[i]['remain'] +' tin' +'</option>');
                }
            })

            created = post.created.split('T')
            $('#inputCreated').val(created[0] + " " + created[1].split('.')[0])
            $('#inputViews').val(post.views)

            expire = post.expire.split('T')
            $('#inputExpire').val(expire[0] + " " + expire[1].split('.')[0])

            option_vip = '';
            if(post.visable_vip == true){
                option_vip += '<option value="1" selected >Có</option>'
                option_vip += '<option value="0">Không</option>'
            }else{
                option_vip += '<option value="1">Có</option>'
                option_vip += '<option value="0" selected >Không</option>'
            }
            $('#inputVisableVip').append(option_vip);

            $('#inputValue').val(post.quantity);
            $('#inputValue').attr('max', post.quantity);
            
            option_activity = '';
            if (post.is_lock == false){
                if(post.is_activity == true){
                    option_activity += '<option value="1" selected >Hiển thị</option>'
                    option_activity += '<option value="0">Không hiển thị</option>'
                }else{
                    option_activity += '<option value="1">Hiển thị</option>'
                    option_activity += '<option value="0" selected >Không hiển thị</option>'
                }
            }
            else
            {
                option_activity += '<option value="1">Bị khóa</option>'
            }
            
            $('#inputIsActivity').append(option_activity)

            // san bat truong hoop lock
        }
    })
})


function showProduct(id_product){
    $.ajax({
        url: 'http://54.213.242.175:8000/admin/product/'+ id_product,
        method: 'GET',
        contentType: 'application/json',
        success: function(response){
            item = ''
            item += '<tr>'
            item += '<td><a href="/admin/product/see/'+ id_product +'">'+ response.code +'</a></td>'
            item += '<td>'+ response.code +'</td>'
            item += '<td><div class="tbl_thumb_product"><img src="/product/'+ response.images[0].image_link +'" alt="Product"></div></td>'
            if (response.discount_percent != 0){
                if (response.price_max_min[0] == response.price_max_min[1])
                    item += '<td>'+ (response.price_max_min[0] * (100 - response.discount_percent))/100 +' VNĐ</td>'
                else
                    item += '<td>'+ (response.price_max_min[1] * (100 - response.discount_percent))/100 + ' - ' + (response.price_max_min[0] * response.discount_percent)/100 +' VNĐ</td>'
            }
            else{
                if (response.price_max_min[0] == response.price_max_min[1])
                    item += '<td>'+ response.price_max_min[0] +' VNĐ</td>'
                else
                    item += '<td>'+ response.price_max_min[1] + ' - ' + response.price_max_min[0] +' VNĐ</td>'
            }
            if (response.detail != '')
                item += '<td>' + (response.detail).substr(0, 50).split('>')[1] + '</td>'
            else
                item += '<td> </td>'
            item += '</tr>'
            $('#item').empty();
            $('#item').append(item)
        }
    })
}
