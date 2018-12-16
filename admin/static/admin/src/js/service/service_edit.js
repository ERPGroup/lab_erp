$(document).ready(function(){
    var check_url = $(location).attr('pathname').split('/');
    var id_service = check_url[check_url.length - 1]

    // Load data in service
    $.ajax({
        url: 'https://laberp.pythonanywhere.com/admin/service/' + id_service,
        method: 'GET',
        contentType: 'application/json',
        success: function(service){
            $('#inputServiceName').val(service.service_name);
            $('#inputValue').val(service.value);
            $('#inputQuantityProduct').val(service.quantity_product);
            $('#inputDayLimit').val(service.day_limit);
            // $('#inputDayVisablePageHome').val(service.day_visable_page_home);
            $('#inputAmount').val(service.amount);
            $('#inputCreator').val(service.account.email);
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
            url: 'https://laberp.pythonanywhere.com/admin/service/' + id_service,
            method: 'POST',
            contentType: 'application/x-www-form-urlencoded',
            data: data,
            success: function(response){
                console.log(response);
                if(response == 1){
                    alert('Đã sửa gói tin thành công!');
                    pageRedirect('/admin/manager_attribute')
                }
                else
                    alert('Xảy ra lỗi~')
            }
        })
    });

    $('#delete').click(function(){

        $.ajax({
            url: 'https://laberp.pythonanywhere.com/admin/service/' + id_service,
            method: 'DETELE',
            success: function(response){
                console.log(response);
                if(response == 1){
                    alert('Gói tin đã ngừng bán!');
                    pageRedirect('/admin/manager_services')
                }
                else
                    alert('Xảy ra lỗi~')
            }
        })
    });
});
