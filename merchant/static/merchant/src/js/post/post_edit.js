$(document).ready(function(){
    var check_url = $(location).attr('pathname').split('/');
    var id_post = check_url[check_url.length - 1]


    $.ajax({
        url: 'http://54.213.242.175:8000/merchant/post/' + id_post,
        method: 'GET',
        contentType: 'application/json',
        success: function(response){

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
                        if(post.post_type == response[i]['service_id']){
                            $('#services').append('<option value="'+ response[i]['service_id'] +'" selected="selected">'+ response[i]['service_name'] + ' | ' + response[i]['remain'] +' tin' +'</option>');
                        }
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

            $('#inputQuantity').val(post.quantity);

            if (post.is_lock == true){
                $('#inputQuantity').attr('disabled', true)
            }

            if(post.is_activity == 0){
                $('#delete').addClass('hidden')
            }
            
            option_activity = '';
            if(post.is_activity == true){
                option_activity += '<option value="1" selected >Hiển thị</option>'
                option_activity += '<option value="0">Không hiển thị</option>'
            }else{
                option_activity += '<option value="1">Hiển thị</option>'
                option_activity += '<option value="0" selected >Không hiển thị</option>'
            }
            $('#inputIsActivity').append(option_activity)
            if (post.is_lock == true){
                $('#inputIsActivity').attr('disabled', true)
            }

            $('#edit').attr('disabled', true)

            // san bat truong hoop lock
        }
    })

    $('#products').change(function(){
        showProduct(this.value);
    });

    $('#edit').click(function(){

        if(parseInt($('#inputQuantity').val()) < 0){
            alert('Số lượng không hợp lệ!')
            return
        }

        data = {
            'inputQuantity': $('#inputQuantity').val(),
            'inputIsActivity': $('#inputIsActivity').val(),
        }

        $.ajax({
            url: 'http://54.213.242.175:8000/merchant/post/' + id_post,
            method: 'POST',
            contentType: 'application/x-www-form-urlencoded',
            data: data,
            success: function(response){
                if (response == 1){
                    alert('Thực hiện thành công!');
                    window.location.replace('/merchant/manager_post');
                }
                else{
                    alert(response)
                }
            }
        })
    });

    $('#delete').click(function(){
        $.ajax({
            url: 'http://54.213.242.175:8000/merchant/post/' + id_post,
            method: 'DELETE',
            contentType: 'application/x-www-form-urlencoded',
            success: function(response){
                if (response == 1){
                    alert('Thực hiện thành công!\nTin đăng đã tắt hiển thị!');
                    window.location.replace('/merchant/manager_post');
                }
                else{
                    alert(response)
                }
            }
        })
    });

    $('#inputQuantity').change(function(){
        $('#edit').attr('disabled', false)
    })

    $('#inputIsActivity').change(function(){
        $('#edit').attr('disabled', false)
    })
})

function showProduct(id_product){
    $.ajax({
        url: 'http://54.213.242.175:8000/merchant/product/'+ id_product + '?posted=true',
        method: 'GET',
        contentType: 'application/json',
        success: function(response){
            item = ''
            item += '<tr>'
            item += '<td><a href="/merchant/product/edit/'+ id_product +'">'+ response.code +'</a></td>'
            item += '<td>'+ response.code +'</td>'
            item += '<td><div class="tbl_thumb_product"><img src="/product/'+ response.images[0].image_link +'" alt="Product"></div></td>'
            
            if (response.price_max_min[0] == response.price_max_min[1])
                item += '<td>'+ currency((response.price_max_min[0] * (100 - response.discount_percent))/100, { precision: 0, separator: ',' }).format() +' VNĐ</td>'
            else
                item += '<td>'+ currency((response.price_max_min[1] * (100 - response.discount_percent))/100 + ' - ' + (response.price_max_min[0] * response.discount_percent)/100, { precision: 0, separator: ',' }).format() +' VNĐ</td>'
            
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
