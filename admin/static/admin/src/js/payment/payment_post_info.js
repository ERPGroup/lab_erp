$(document).ready(function(){
    var check_url = $(location).attr('pathname').split('/');
    var id_payment = check_url[check_url.length - 1]
    $.ajax({
        url: 'http://13.67.105.209:8000/admin/f_payment_post_detail/' + id_payment,
        method: 'GET',
        success: function(response){
            $('#inputName').val(response.merchant.name);
            $('#inputEmail').val(response.merchant.email);
            $('#inputContent').val(response.purchase_name);
            $('#inputCreated').val((response.success_at).split('T')[0] + ' ' + ((response.success_at).split('T')[1]).split('.')[0]);
            
            if( response.state == 1)
                $('#inputState').append('<option>Thành công</option>')
            else
                $('#inputState').append('<option>Thất bại</option>')

            $('#service_name').append('<a href="/admin/service/edit/'+ response.service_id_id +'">'+ response.service.service_name +'</a>')
            $('#amount').append(response.amount + ' $')
        }
    })
})