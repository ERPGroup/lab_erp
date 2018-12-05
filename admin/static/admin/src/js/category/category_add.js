
$(document).ready(function(){
    $('#submit').click(function(){
        data = {
            'inputName': $('#inputName').val(),      
        }
        $.ajax({
            url: 'http://localhost:8000/admin/category',
            method: 'POST',
            contentType: 'application/x-www-form-urlencoded',
            data: data,
            success: function(response){
                if(response == 1){   
                    setTimeout("pageRedirect('/admin/manager_category')", 3000);
                    alert('Da them thanh cong!\nBan se duoc dieu huong den danh muc san pham sau 3 giay!');
                }
                else
                    alert('ERROR!');        
            }
        })
    });
});
