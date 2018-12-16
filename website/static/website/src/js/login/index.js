$(document).ready(function(){
    $('#sub_forget_pass').click(function(){
        data = {
            'inputEmail': $('#forgot_email').val(),
        }
        $.ajax({
            url: 'https://laberp.pythonanywhere.com/forgot_password',
            method: 'POST',
            contentType: 'application/x-www-form-urlencoded',
            data: data,
            success: function(response){
                if(response == 1){
                    alert('Thư lấy lại mật khẩu đã được gửi và mail của bạn!')
                    window.location.replace('/')
                }
                else(
                    alert(response)
                )
            }
        })
    })
})