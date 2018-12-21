$(document).ready(function(){
    $.ajax({
        url: 'http://54.213.242.175:8000/merchant/products?posted=false',
        method: 'GET',
        contentType: 'application/json',
        success: function(response){
            for (var i = 0; i < response.length; i++){
                $('#products').append('<option value="'+ response[i]['pk'] +'">'+ response[i]['fields']['code'] + ' - ' + response[i]['fields']['name'] +'</option>')
            }
            console.log($('#products:first').val())
            if ($('#products:first').val() === null )
                $('#item').empty();
            else
                showProduct($('#products:first').val());
        }
    }) 

    $.ajax({
        url: 'http://54.213.242.175:8000/merchant/account_services?service=available',
        method: 'GET',
        contentType: 'application/json',
        success: function(response){
            console.log(response)
            for(var i = 0; i < response.length; i++)
                $('#services').append('<option value="'+ response[i]['service_id'] +'">'+ response[i]['service_name'] + ' | ' + response[i]['remain'] +' tin' +'</option>');
            
            if ($('#services:first').val() !== null)
                showPost($('#services:first').val());
        }
    })

    $('#services').change(function(){
        showPost(this.value)
    });

    $('#products').change(function(){
        showProduct(this.value);
    });

    $('#submit').click(function(){
        if($('#products').val() == ''){
            alert('Vui lòng lựa chọn sản phẩm')
            return
        }

        if($('#services').val() == ''){
            alert('Vui lòng lựa chọn tin đăng')
            return
        }

        if(parseInt($('#inputQuantity').val()) < 0 || parseInt($('#inputQuantity').attr('max')) < parseInt($('#inputQuantity').val())){
            alert('Số lượng không hợp lệ!')
            return
        }


        data = {
            'inputProduct': $('#products').val(),
            'inputService': $('#services').val(),
            'inputQuantity': $('#inputQuantity').val(),
        }

        $.ajax({
            url: 'http://54.213.242.175:8000/merchant/post',
            method: 'POST',
            contentType: 'application/x-www-form-urlencoded',
            data: data,
            success: function(response){
                if (response == 1){
                    alert('Sản phẩm đã được đăng!');
                    window.location.replace('/merchant/manager_post');
                }
                else if (response == -4){
                    alert('Vui lòng kết nối tài khoản giao hàng tiết kiệm!');
                    window.location.replace('/setup/ghtk')
                }
                else{
                    alert(response);
                }
            }
        })
    });
})

function showProduct(id_product){
    $.ajax({
        url: 'http://54.213.242.175:8000/merchant/product/'+ id_product,
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

function showPost(id_service){
    $.ajax({
        url: 'http://54.213.242.175:8000/merchant/service/'+ id_service + '?posted=true',
        method: 'GET',
        contentType: 'application/json',
        success: function(service){
            
            $('#inputDayLimit').val(service['day_limit']);
            option_vip = '';
            if(service.visable_vip == true){
                option_vip += '<option value="1" selected >Có</option>'
                option_vip += '<option value="0">Không</option>'
            }else{
                option_vip += '<option value="1">Có</option>'
                option_vip += '<option value="0" selected >Không</option>'
            }
            $('#inputVisableVip').append(option_vip);
            $('#inputQuantity').val(service.quantity_product);
            $('#inputQuantity').attr('max', service.quantity_product);
        }
    })
}
