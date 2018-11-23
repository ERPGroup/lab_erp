
$(document).ready(function(){
    $('#submit').click(function(){
        data = {
            'inputServiceName': $('#inputServiceName').val(),
            'inputValue': $('#inputValue').val(),
            'inputQuantityProduct': $('#inputQuantityProduct').val(),
            'inputDayLimit': $('#inputDayLimit').val(),
            'inputAmount': $('#inputAmount').val(),
            'inputIsActive': $('#inputIsActive').val(),
            'inputVisableVip': $('#inputVisableVip').val(),
        }
        $.ajax({
            url: 'http://localhost:8000/admin/service',
            method: 'POST',
            contentType: 'application/x-www-form-urlencoded',
            data: data,
            success: function(response){
                if(response == 1){   
                    setTimeout("pageRedirect('/admin/manager_services')", 3000);
                    alert('Da them thanh cong!\nBan se duoc dieu huong den danh sach dich vu sau 3 giay!');
                }
                else
                    alert('ERROR!');
                
            }
        })
    });
});
