$(document).ready(function(){
    var check_url = $(location).attr('pathname').split('/');
    var id_category = check_url[check_url.length - 1]

    // Load data in category
    $.ajax({
        url: 'http://13.67.105.209:8000/admin/category/' + id_category,
        method: 'GET',
        contentType: 'application/json',
        success: function(response){
            console.log(response);
            category = response[0]['fields']
            $('#inputName').val(category.name_category);
            //$('#number3').val(category.quantity);
            var option_active = ''
            if(category.is_active == true){
                option_active += '<option value="1" selected >Kích hoạt</option>'
                option_active += '<option value="0">Đang khoá</option>'
            }else{
                option_active += '<option value="1">Kích hoạt</option>'
                option_active += '<option value="0" selected >Đang khoá</option>'
            }
            $('#inputIsActive').append(option_active)
        }
    })

    // Edit Category

    $('#edit').click(function(){
        data = {
            'inputName': $('#inputName').val(),
            'inputIsActive': $('#inputIsActive').val(),    
        }

        $.ajax({
            url: 'http://13.67.105.209:8000/admin/category/' + id_category,
            method: 'POST',
            contentType: 'application/x-www-form-urlencoded',
            data: data,
            success: function(response){
                console.log(response);
                if(response == 1){
                    alert('Đã sửa thư mục thành công!');
                    pageRedirect('/admin/manager_category')
                }
                else
                    alert('Xảy ra lỗi!')
            }
        })
    });

    $('#delete').click(function(){
        $.ajax({
            url: 'http://13.67.105.209:8000/admin/category/' + id_category,
            method: 'DETELE',
            success: function(response){
                console.log(response);
                if(response == 1){
                    alert('Dạnh mục đã dừng sử dụng!');
                    pageRedirect('/admin/manager_category')
                }
                else
                    alert('ERROR')
            }
        })
    });
});
