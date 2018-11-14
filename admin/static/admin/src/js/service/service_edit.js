$(document).ready(function(){
    var check_url = $(location).attr('pathname').split('/');
    var id_service = check_url[check_url.length - 1]

    // Load data in service
    $.ajax({
        url: 'http://localhost:8000/admin/service/' + id_service,
        method: 'GET',
        contentType: 'application/json',
        success: function(response){
            console.log(response);
            service = response[0]['fields']
            $('#inputServiceName').val(service.service_name);
            $('#inputValue').val(service.value);
            $('#inputQuantityProduct').val(service.quantity_product);
            $('#inputDayLimit').val(service.day_limit);
            $('#inputDayVisablePageHome').val(service.day_visable_page_home);
            $('#inputAmount').val(service.amount);
            var option_active = ''
            if(service.is_active == true){
                option_active += '<option value="1" selected >Sử dụng</option>'
                option_active += '<option value="0">Không sử dụng</option>'
            }else{
                option_active += '<option value="1">Sử dụng</option>'
                option_active += '<option value="0" selected >Không sử dụng</option>'
            }
            $('#inputIsActive').append(option_active)
            var option_vip = '';
            if(service.visable_vip == true){
                option_vip += '<option value="1" selected >Có</option>'
                option_vip += '<option value="0">Không</option>'
            }else{
                option_vip += '<option value="1">Có</option>'
                option_vip += '<option value="0" selected >Không</option>'
            }
            $('#inputVisableVip').append(option_vip);
        }
    })

    // Edit Service

    $('#edit').click(function(){
        data = {
            'inputVisableVip': $('#inputVisableVip').val(),
            'inputIsActive': $('#inputIsActive').val(),
        }

        $.ajax({
            url: 'http://localhost:8000/admin/service/' + id_service,
            method: 'POST',
            contentType: 'application/x-www-form-urlencoded',
            data: data,
            success: function(response){
                console.log(response);
                if(response == 1){
                    setTimeout("pageRedirect('/admin/manager_services')", 3000);
                    alert('Da sua thanh cong!\nBan se duoc dieu huong den danh sach dich vu sau 3 giay!');
                }
                else
                    alert('ERROR')
            }
        })
    });

    $('#delete').click(function(){

        $.ajax({
            url: 'http://localhost:8000/admin/service/' + id_service,
            method: 'DETELE',
            success: function(response){
                console.log(response);
                if(response == 1){
                    setTimeout("pageRedirect('/admin/manager_services')", 3000);
                    alert('Dich vu da ngung ban!\nBan se duoc dieu huong den danh sach dich vu sau 3 giay!');
                }
                else
                    alert('ERROR')
            }
        })
    });
});
