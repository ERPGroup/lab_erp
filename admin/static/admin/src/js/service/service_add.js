
$(document).ready(function(){
    $('#submit').click(function(){
        if ($('#inputServiceName').val() == ''){
            alert('Tên dịch vụ không hợp lệ')
            return
        }
        
        if ($('#inputValue').val() == ''){
            alert('Số lượng tin không hợp lệ')
            return
        }

        if ($('#inputQuantityProduct').val() == ''){
            alert('Số lượng sản phẩm không hợp lệ')
            return
        }

        if ($('#inputDayLimit').val() == ''){
            alert('Giới hạn không hợp lệ')
            return
        }

        if ($('#inputAmount').val() == ''){
            alert('Số tiền không hợp lệ')
            return
        }


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
            url: 'http://13.67.105.209:8000/admin/service',
            method: 'POST',
            contentType: 'application/x-www-form-urlencoded',
            data: data,
            success: function(response){
                if(response == 1){   
                    alert('Đã thêm gói tin mới!');
                    pageRedirect('/admin/manager_services')
                }
                else
                    alert(response);
                
            }
        })
    });
});
