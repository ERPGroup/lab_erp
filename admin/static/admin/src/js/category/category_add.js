
$(document).ready(function(){
    $('#submit').click(function(){
        data = {
            'inputName': $('#inputName').val(),      
        }
        $.ajax({
            url: 'https://laberp.pythonanywhere.com/admin/category',
            method: 'POST',
            contentType: 'application/x-www-form-urlencoded',
            data: data,
            success: function(response){
                if(response == 1){   
                    alert('Đã thêm danh mục thành công!');
                    pageRedirect('/admin/manager_category')
                }
                else
                    alert('Xảy ra lỗi!');        
            }
        })
    });
});
