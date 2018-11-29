$(document).ready(function(){
    $.ajax({
        url: 'http://localhost:8000/merchant/products?posted=false',
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
        url: 'http://localhost:8000/merchant/account_services?service=available',
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
        data = {
            'inputProduct': $('#products').val(),
            'inputService': $('#services').val(),
            'inputValue': $('#inputValue').val(),
        }

        $.ajax({
            url: 'http://localhost:8000/merchant/post',
            method: 'POST',
            contentType: 'application/x-www-form-urlencoded',
            data: data,
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

function showPost(id_service){
    $.ajax({
        url: 'http://localhost:8000/merchant/service/'+ id_service,
        method: 'GET',
        contentType: 'application/json',
        success: function(response){
            console.log(response);
            service = response[0]['fields']
            
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
            $('#inputValue').val(service.value);
            $('#inputValue').attr('max', service.value);
        }
    })
}
