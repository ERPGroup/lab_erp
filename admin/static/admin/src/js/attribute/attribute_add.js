$(document).ready(function(){
    $('#submit').click(function(){
        data = {
            'inputLabel': $('#inputLabel').val(),       
        }
        $.ajax({
            url: 'http://54.213.242.175:8000/admin/attribute',
            method: 'POST',
            contentType: 'application/x-www-form-urlencoded',
            data: data,
            success: function(response){
                if(response == 1){   
                    alert('Đã thêm thuộc tính thành công!');
                    pageRedirect('/admin/manager_attribute');
                }
                else
                    alert('Xảy ra lỗi!');        
            }
        })
    });
});
