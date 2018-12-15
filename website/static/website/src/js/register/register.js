$('#select_type_user').change(function () {
    var result = document.getElementById('type_users_selected');
    if (this.value == 0)
        result.style.display = 'none';
    else
        result.style.display = 'block';
})

$(document).ready(function(){
    $('#sub_register').click(function(){
        var day = $("#datetimepicker1").find("input").val().split('/')
        var birthday = day[2]+'-'+day[1]+'-'+day[0]
        var sex = 0

        if($('#inlineRadio2').attr('checked') == true)
            sex = 1;
        var type_account = $('#select_type_user').val()
        if (type_account == 0){
            data = {
                'inputUsername': $('#inputUsername').val(),
                'inputEmail': $('#inputEmail').val(),
                'inputPassword': $('#inputPassword').val(),
                'inputFullname': $('#inputFullname').val(),
                'inputBirthday': birthday,
                'inputSex': sex,
                'inputOptionAcc': $('#select_type_user').val(),
            }
        }
        else{
            if ($('#input_tel').val().length != 10){
                alert('Số điện thoại không hợp lệ')
                return;
            }
            if ($('#input_id').val().length > 12 || $('#input_id').val().length < 10){
                alert('Chứng minh nhân dân không hợp lệ')
                return;
            }
            data = {
                'inputUsername': $('#inputUsername').val(),
                'inputEmail': $('#inputEmail').val(),
                'inputPassword': $('#inputPassword').val(),
                'inputFullname': $('#inputFullname').val(),
                'inputBirthday': birthday,
                'inputSex': sex,
                'inputOptionAcc': $('#select_type_user').val(),
                'inputID': $('#input_id').val(),
                'inputTel': $('#input_tel').val(),
                'inputAddress': $('#input_address').val(),
                'inputStore': $('#input_store').val(),
            }
        }
        
        $.ajax({
            url: 'http://localhost:8000/f_register',
            method: 'POST',
            contentType: 'application/x-www-form-urlencoded',
            data: data,
            success: function(response){
                if(response == 1){
                    alert('Thư xác minh đã được gửi và mail của bạn!')
                    window.location.replace('/')
                }
                else(
                    alert(response)
                )
            }
        })
    })
})