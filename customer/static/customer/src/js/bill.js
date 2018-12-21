$(document).ready(function(){
    var check_url = $(location).attr('pathname').split('/');
    var id_order = check_url[check_url.length - 1]

    $('#success_order').click(function(){
        $.ajax({
            url: 'http://54.213.242.175:8000/customer/success_order/' + id_order,
            method: 'GET',
            success: function(response){
                if (response == 1){
                    alert('Đơn hàng đã cập nhật trạng thái!');
                    location.reload();
                }
                else{
                    alert(response);
                }
            }
        })
    });

    $('#cancel_order').click(function(){
        $.ajax({
            url: 'http://54.213.242.175:8000/customer/cancel_order/' + id_order,
            method: 'GET',
            success: function(response){
                if (response == 1){
                    alert('Đơn hàng đã cập nhật trạng thái!');
                    location.reload();
                }
                else{
                    alert(response);
                }
            }
        })
    });
});

function cancel_order_item(id_order_item){
    $.ajax({
        url: 'http://54.213.242.175:8000/customer/cancel_order_item/' + id_order_item,
        method: 'GET',
        success: function(response){
            if (response == 1){
                alert('Đơn hàng đã cập nhật trạng thái!');
                location.reload();
            }
            else{
                alert(response);
            }
        }
    })
}