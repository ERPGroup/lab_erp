$(document).ready(function(){
    $('#submit').click(function(){
        data = {
            'inputServiceName': $('#inputServiceName').val(),
            'inputValue': $('#inputValue').val(),
            'inputDayLimit': $('#inputDayLimit').val(),
            'inputDayVisablePageHome': $('#inputDayVisablePageHome').val(),
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
                    alert('Da them thanh cong!')
                }
            }
        })
    });
});