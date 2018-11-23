$(document).ready(function(){
    var check_url = $(location).attr('pathname').split('/');
    var id_post = check_url[check_url.length - 1]


    $.ajax({
        url: 'http://localhost:8000/merchant/post/' + id_post,
        method: 'GET',
        contentType: 'application/json',
        success: function(response){
            console.log((response[0]['fields'].expire.split('T')));

            post = response[0]['fields']

            //Load Product
            $.ajax({
                url: 'http://localhost:8000/merchant/products?posted=false&include=' + post.product_id ,
                method: 'GET',
                contentType: 'application/json',
                success: function(response){
                    for (var i = 0; i < response.length; i++){
                        if (post.product_id == response[i]['pk']){
                            $('#products').append('<option value="'+ response[i]['pk'] +'" selected="selected">'+ response[i]['fields']['code'] + ' - ' + response[i]['fields']['name'] +'</option>')
                            showProduct(response[i]['pk']);
                        }
                    }
                }
            }) 


            // load Service
            $.ajax({
                url: 'http://localhost:8000/merchant/account_services?service=available',
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
            if(post.is_activity == true){
                option_activity += '<option value="1" selected >Hiển thị</option>'
                option_activity += '<option value="0">Không hiển thị</option>'
            }else{
                option_activity += '<option value="1">Hiển thị</option>'
                option_activity += '<option value="0" selected >Không hiển thị</option>'
            }
            $('#inputIsActivity').append(option_activity)

            // san bat truong hoop lock
        }
    })

    $('#products').change(function(){
        showProduct(this.value);
    });

    $('#edit').click(function(){
        data = {
            'inputValue': $('#inputValue').val(),
            'inputIsActivity': $('#inputIsActivity').val(),
        }

        $.ajax({
            url: 'http://localhost:8000/merchant/post/' + id_post,
            method: 'POST',
            contentType: 'application/x-www-form-urlencoded',
            data: data,
            success: function(response){
                alert(response)
            }
        })
    });

    $('#delete').click(function(){
        $.ajax({
            url: 'http://localhost:8000/merchant/post/' + id_post,
            method: 'DELETE',
            contentType: 'application/x-www-form-urlencoded',
            success: function(response){
                alert(response)
            }
        })
    });
})

function showProduct(id_product){
    $.ajax({
        url: 'http://localhost:8000/merchant/product/'+ id_product,
        method: 'GET',
        contentType: 'application/json',
        success: function(response){
            console.log(response);
            item = ''
            item += '<tr>'
            item += '<td><a href="/merchant/product/edit/'+ this.value +'">'+ response.code +'</a></td>'
            item += '<td>'+ response.code +'</td>'
            item += '<td><div class="tbl_thumb_product"><img src="'+ response.list_image[0].image_link +'" alt="Product"></div></td>'
            item += '<td>'+ response.price_origin +' VNĐ</td>'
            item += '<td>Đây là sản phẩm demo cho mọi người xem thôi, chứ khong6 có gì đâu</td>'
            item += '</tr>'
            $('#item').empty();
            $('#item').append(item)
        }
    })
}
