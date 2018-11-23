$(document).ready(function(){
    $('#sub_destop').click(function(){
        data  = {
            'inputEmail': $('#_email').val(),
            'inputName': $('#_billing_address_last_name').val(),
            'inputPhone': $('#_billing_address_phone').val(),
            'inputAddress': $('#_billing_address_address1').val(),
            'inputNote': $('#inputNote').val(),
        }
        console.log(data)

        $.ajax({
            url: 'http://localhost:8000/payment',
            method: 'POST',
            contentType: 'application/x-www-form-urlencoded',
            data: data,
            success: function(response){
                alert(response);
            }
        })
    });

    $('#sub_mobile').click(function(){
        data  = {
            'inputEmail': $('#_email').val(),
            'inputName': $('#_billing_address_last_name').val(),
            'inputPhone': $('#_billing_address_phone').val(),
            'inputAddress': $('#_billing_address_address1').val(),
            'inputNote': $('#inputNote').val(),
        }
        $.ajax({
            url: 'http://localhost:8000/payment',
            method: 'POST',
            contentType: 'application/x-www-form-urlencoded',
            data: data,
            success: function(response){
                alert(response);
            }
        })
    });
});
