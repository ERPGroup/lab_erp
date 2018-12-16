$('#select_type_user').change(function () {
    var result = document.getElementById('type_users_selected');
    if (this.value == 0)
        result.style.display = 'none';
    else
        result.style.display = 'block';
})

function validateNumber(str) {
    var reg = /^\d+$/;
    if (reg.test(str)) {
        return true;
    }
    return false;
}
function AddAlertError(str,message)
{
    var error = document.getElementById('errors_'+str)
    var result = document.getElementById('check_'+str)
    result.classList.add('has-error')
    error.innerHTML = message;
}
function RemoveAlertError(str)
{
    var error = document.getElementById('errors_'+str)
    var result = document.getElementById('check_'+str)
    result.classList.remove('has-error')
    error.innerHTML = '';
}
$(document).ready(function () {
    $('#input_tel').keyup(function (e) {
        var ph = /^((\\+[1-9]{1,4}[ \\-]*)|(\\([0-9]{2,3}\\)[ \\-]*)|([0-9]{2,4})[ \\-]*)*?[0-9]{3,4}?[ \\-]*[0-9]{3,4}?$/
        if (!ph.test(String($(this).val()))) {
            AddAlertError('tel','Số điện thoại không hợp lệ.')
        } else {
            RemoveAlertError('tel')
        }
    })
    $('#input_id').keyup(function (e) {
       
        if (!validateNumber(String($(this).val()))) {
            AddAlertError('CMND','CMND không hợp lệ')
        } else {
            RemoveAlertError('CMND')
        }
    })
    $('#sub_register').click(function (e) {
        e.preventDefault();
        var day = $("#datetimepicker1").find("input").val().split('/')
        var birthday = day[2] + '-' + day[1] + '-' + day[0]
        var sex = 0

        if ($('#inlineRadio2').attr('checked') == true)
            sex = 1;
        var type_account = $('#select_type_user').val()
        if (type_account == 0) {
            data = {
                'inputUsername': $('#inputUsername').val(),
                'inputEmail': $('#inputEmail').val(),
                'inputPassword': $('#inputPassword').val(),
                'inputFullname': $('#inputFullname').val(),
                'inputBirthday': birthday,
                'inputSex': sex,
                'inputOptionAcc': $('#select_type_user').val(),
            }
        } else {
            if ($('#input_tel').val().length != 10) {
                AddAlertError('tel','Số điện thoại không hợp lệ.')
                return;
            } else {
                RemoveAlertError('tel')
            }
            if ($('#input_id').val().length > 12 || $('#input_id').val().length < 10) {
                AddAlertError('CMND','CMND không hợp lệ')
                return;
            } else {
                RemoveAlertError('CMND')
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
            url: 'http://13.67.105.209:8000/f_register',
            method: 'POST',
            contentType: 'application/x-www-form-urlencoded',
            data: data,
            success: function (response) {
                if (response == 1) {
                    alert('Thư xác minh đã được gửi và mail của bạn!')
                    window.location.replace('/')
                } else {
                    if (response == "Username đã tồn tại!") {
                        AddAlertError('username','Tài khoản đã tồn tại')
                    }
                    if(response =="Email đã tồn tại!")
                    {
                        AddAlertError('email','Email đã tồn tại!')
                    }
                }
            }
        })
    })
})