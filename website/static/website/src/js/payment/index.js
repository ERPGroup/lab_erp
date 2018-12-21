$(document).ready(function(){
    $('#update_profile').click(function(){
        $.ajax({
            url: 'http://54.213.242.175:8000/get_profile_payment',
            method: 'GET',
            success: function(response){
                $('#_billing_address_last_name').val(response.name)
                $('#_billing_address_phone').val(response.phone)
                $('#_billing_address_address1').val(response.address)
            }
        })
    });

    $('#sub_destop').click(function(){

        if ($('#_billing_address_last_name').val() == ''){
            alert('Họ tên không được để trống!');
            return
        }

        if ($('#_billing_address_phone').val() == ''){
            alert('Số điện thoại không được để trống!');
            return
        }


        if ($('#_billing_address_address1').val() == ''){
            alert('Địa chị không được để trống');
            return
        }

        if (check_phone('_billing_address_phone') == false){
            alert('Số điện thoại không hợp lệ!')
            return
        }

        data  = {
            'inputName': $('#_billing_address_last_name').val(),
            'inputPhone': $('#_billing_address_phone').val(),
            'inputAddress': $('#_billing_address_address1').val(),
            'inputNote': $('#inputNote').val(),
        }
        console.log(data)
        document.getElementById("loader").style.display = "block";
        document.getElementById("html_payment").style.display = "none";
        $.ajax({
            url: 'http://54.213.242.175:8000/payment',
            method: 'POST',
            contentType: 'application/x-www-form-urlencoded',
            data: data,
            success: function(response){
                if(response == 1){
                    alert('Đặt hàng thành công!');
                    window.location.replace('/customer/history_order');
                }
                else
                {
                    alert(response);
                    document.getElementById("loader").style.display = "none";
                    document.getElementById("html_payment").style.display = "block";
                }
            }
        })
    });

    $('#sub_mobile').click(function(){

        if ($('#_billing_address_last_name').val() == ''){
            alert('Họ tên không được để trống!');
            return
        }

        if ($('#_billing_address_phone').val() == ''){
            alert('Số điện thoại không được để trống!');
            return
        }


        if ($('#_billing_address_address1').val() == ''){
            alert('Địa chị không được để trống');
            return
        }

        if (check_phone('_billing_address_phone') == false){
            alert('Số điện thoại không hợp lệ!')
            return
        }

        data  = {
            'inputName': $('#_billing_address_last_name').val(),
            'inputPhone': $('#_billing_address_phone').val(),
            'inputAddress': $('#_billing_address_address1').val(),
            'inputNote': $('#inputNote').val(),
        }
        document.getElementById("loader").style.display = "block";
        document.getElementById("html_payment").style.display = "none";
        $.ajax({
            url: 'http://54.213.242.175:8000/payment',
            method: 'POST',
            contentType: 'application/x-www-form-urlencoded',
            data: data,
            success: function(response){
                if(response == 1){
                    alert('Đặt hàng thành công!');
                    window.location.replace('/customer/history_order');
                }
                else
                {
                    alert(response);
                    document.getElementById("loader").style.display = "none";
                    document.getElementById("html_payment").style.display = "block";
                }
            }
        })
    });
});

function check_phone(txtPhone){
    var a = document.getElementById(txtPhone).value;
    var filter = /^[0-9-+]+$/;
    if (a.length != 10)
        return false;
    if (filter.test(a)) {
        return true;
    }
    else {
        return false;
    }
}
