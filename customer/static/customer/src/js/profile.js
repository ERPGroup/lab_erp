$(document).ready(function(){
    // Load data 
    $.ajax({
        url: 'https://laberp.pythonanywhere.com/customer/user',
        method: 'GET',
        contentType: 'application/json',
        success: function(response){
            console.log(response);
            user = response[0]['fields']
            $('#inputUsername').val(user.username);
            $('#inputFullname').val(user.name);
            $('#inputAddress').val(user.address);
            $('#inputTel').val(user.phone);
            $('#datetimepicker1').datetimepicker({
                    locale: 'vi',
                    format: 'DD/MM/YYYY',
                    maxDate: new Date('2010-12-30'),
                    date: new Date(user.birthday),
            });
            if(user.sex==false){
                $( "#inlineRadio3" ).prop( "checked", true );
                $( "#inlineRadio2" ).prop( "checked", false );
            }
            else{
                $( "#inlineRadio2" ).prop( "checked", true );
                $( "#inlineRadio3" ).prop( "checked", false );
            }
        }
    })

    //Change password
    $('#password').click(function(){
        password1= $('#inputPassword').val()
        password2= $('#inputRePassword').val()
        if (password1 == "" || password2 == ""){
            alert('Vui long nhap day du mat khau!');
            return
        }
        if(password2 != password1){
            alert('Mat khau khong giong nhau!');
            return
        }
        data = {
            'inputPassword': $('#inputPassword').val()   
        }
        $.ajax({
            url: 'https://laberp.pythonanywhere.com/customer/password',
            method: 'POST',
            contentType: 'application/x-www-form-urlencoded',
            data: data,
            success: function(response){
                console.log(response);
                if(response == 1){
                    setTimeout("location.href = 'https://laberp.pythonanywhere.com/customer/profile';",0);
                    alert('Da doi mat khau thanh cong!');
                }
                else
                    alert('ERROR')
            }
        })
    });
    //Change persional information
    $('#info').click(function(){
        name= $('#inputFullname').val()
        address= $('#inputAddress').val()
        phone= $('#inputTel').val()
        day=$("#datetimepicker1").find("input").val().split('/')
        birthday=day[2]+'-'+day[1]+'-'+day[0]

        if ($("#inlineRadio2").is(':checked')){
            sex=1
        }
        else{
            sex=0
        }         

        if (name == "" || address == "" || phone == "" || birthday == ""){
            alert('Vui long nhap day du thong tin ca nhan!');
            return
        }

        data = {
            'name': name,
            'address': address,
            'phone': phone,
            'birthday': birthday,
            'sex': sex,
        }
        console.log(data)
        $.ajax({
            url: 'https://laberp.pythonanywhere.com/customer/info',
            method: 'POST',
            contentType: 'application/x-www-form-urlencoded',
            data: data,
            success: function(response){
                console.log(response);
                if(response == 1){
                    setTimeout("location.href = 'https://laberp.pythonanywhere.com/customer/profile';",0);
                    alert('Cap nhat thong tin ca nhan thanh cong!');
                }
                else
                    alert('ERROR')
            }
        })
    });
})