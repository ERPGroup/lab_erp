$(document).ready(function(){
    var check_url = $(location).attr('pathname').split('/');
    var id_payment = check_url[check_url.length - 1]
    $.ajax({
        url: 'https://laberp.pythonanywhere.com/merchant/f_payment_ads_detail/' + id_payment,
        method: 'GET',
        success: function(response){
            $('#inputName').val(response.merchant.name);
            $('#inputEmail').val(response.merchant.email);
            $('#inputContent').val(response.purchase_name);
            $('#inputCreated').val((response.success_at).split('T')[0] + ' ' + ((response.success_at).split('T')[1]).split('.')[0]);
            
            if( response.state != 0)
                $('#inputState').append('<option>Thành công</option>')
            else
                $('#inputState').append('<option>Thất bại</option>')

            $('#service_name').append('<a href="/admin/manager_ads_detail/'+ response.service_ads_id_id +'">'+ response.service.service_name +'</a>')
            $('#amount').append(response.amount + ' VNĐ')
        }
    })
})