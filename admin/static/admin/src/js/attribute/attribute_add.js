$(document).ready(function(){
    $('#submit').click(function(){
        data = {
            'inputLabel': $('#inputLabel').val(),       
        }
        $.ajax({
            url: 'http://localhost:8000/admin/attribute',
            method: 'POST',
            contentType: 'application/x-www-form-urlencoded',
            data: data,
            success: function(response){
                if(response == 1){   
                    setTimeout("pageRedirect('/admin/manager_attribute')", 3000);
                    alert('Da them thanh cong!\nBan se duoc dieu huong den danh sach thuoc tinh sau 3 giay!');
                }
                else
                    alert('ERROR!');        
            }
        })
    });
});
