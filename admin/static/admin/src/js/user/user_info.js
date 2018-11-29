$(document).ready(function(){
    var check_url = $(location).attr('pathname').split('/');
    var id_user = check_url[check_url.length - 1]
    $.ajax({
        url: 'http://localhost:8000/admin/user/' + id_user,
        method:  'GET',
        contentType: 'application/json',
        success: function(response){
            if (response == -3){
                alert('Tai khoan khong ton tai');
                return;
            }
            if (response == -2){
                alert('Quyen truy cap bi tu choi');
                return;
            }
            if (response == -1){
                alert('Loi he thong!');
                return;
            }
            console.log(response)
            $('#inputName').val(response.name);
            $('#inputIDCard').val(response.id_card);
            $('#phone').val(response.phone);
            $('#inputAddress').val(response.address);
            $('#inputBirthday').val(response.birthday);
            if (response.lock == false)
                $('#select_status').append('<option>Đang hoạt động</option>');
            else
                $('#select_status').append('<option>Đã bị khóa</option>');
            
            if (response.sex == true)
                $('#Sex1').attr('checked', true)
            else if(response.sex == false)
                $('#Sex2').attr('checked', true)
            
            $('#username').val(response.username);
            $('#inputNameShop').val(response.name_shop);
            $('#email').val(response.email);
            if(response.role == 1)
                $('#type_user3').attr('checked', true);
            else if (response.role == 2)
                $('#type_user1').attr('checked', true);
            else if (response.role == 3)
                $('#type_user2').attr('checked', true);

            if (response.lock == false)
                $('button[id=unlock]').addClass('hidden');
            else 
                $('#lock').addClass('hidden');
            if (response.role == 2){
                $('#service').removeClass('hidden');
                $.ajax({
                    url: 'http://localhost:8000/admin/account_services?service=available',
                    method: 'GET',
                    contentType: 'application/json',
                    success: function(services){
                        for(var i = 0; i < services.length; i++){
                            html = '<tr>'
                            html += '<td>' + services[i].service_name + '</td>'
                            html += '<td>' + services[i].remain + ' tin </td>' 
                            html += '</tr>'
                            $('#result_sevice').append(html);
                        }
                    }
                })
            }
        }
    })

    $('#lock').click(function(){
        $.ajax({

        })
    }); 

    $('#unlock').click(function(){
        $.ajax({

        })
    });
})