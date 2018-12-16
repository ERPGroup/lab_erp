$(document).ready(function () {

    var check_url = $(location).attr('pathname').split('/');
    var id_order = check_url[check_url.length - 1]
    $.ajax({
        url: 'http://13.67.105.209:8000/merchant/order/' + id_order,
        method: 'GET',
        success: function(response){
            $('#inputIdCus').val(response.customer_id);
            $('#inputName').val(response.name_customer);
            $('#inputRating').val(response.rating_point + ' */ ' + response.rating_count + ' lần')
            $('#inputAmount').val(response.amount + ' VND')
            $('#inputNote').val(response.note)
            $('#inputCreated').val((response.created.split('T')[0]) + ' ' + (response.created.split('T')[1]).split('.')[0])
            $('#inputNameCus').val(response.name)
            $('#inputAddress').val(response.address)
            $('#inputPhone').val(response.phone)
            
            if (response.state == 0){
                $('#inputState').append('<option>Hủy đơn hàng</option>')
            }
            if (response.state == 1){
                $('#inputState').append('<option>Hoàn tất đơn hàng</option>')
            }
            if (response.state == 2){
                $('#inputState').append('<option>Đặt hàng</option>')
            }

            if (response.disable_rating == true){
                $('#part_rating').removeClass('hidden');
                $('#inputRatingCus').attr('disabled', true)
                $('#inputRatingCus').val(response.value_rating)
            }
            else{
                if(response.rate_cus  == true){
                    $('#part_rating').removeClass('hidden');
                    var num_star = $('#inputRatingCus').val()
                    $('#submit_action').append('<button onclick="rating_customer('+ id_order +')" class="btn btn-default">Đánh giá</button>')
                }
            }
            

            if (response.state_now == 2){
                $('#submit_action').append('<button onclick="change_state('+ id_order +', 3)" class="btn btn-warning">Bắt đầu gói hàng</button>')
            }
            if (response.state_now == 3){
                $('#submit_action').append('<button onclick="change_state('+ id_order +', 4)" class="btn btn-info">Bắt đầu vận chuyển</button>')
            }
            if (response.state_now == 4){
                $('#submit_action').append('<button onclick="change_state('+ id_order +', 1)" class="btn btn-success">Thành công</button>')
                $('#submit_action').append('<button onclick="change_state('+ id_order +', 0)" style="margin-left: 5px;" class="btn btn-danger">Hủy bỏ</button>')
            }
        }
    })





    jQuery.extend(jQuery.fn.dataTableExt.oSort, {
        "formatted-num-pre": function (a) {
            a = (a === "-" || a === "") ? 0 : a.replace(/[^\d\-\.]/g, "");
            return parseFloat(a);
        },

        "formatted-num-asc": function (a, b) {
            return a - b;
        },

        "formatted-num-desc": function (a, b) {
            return b - a;
        }
    });

    var table = $('#dataTables-example').dataTable({
        language: {
            paginate: {
                previous: "<i class='fa fa-arrow-left'></i>",
                next: "<i class='fa fa-arrow-right'></i>"
            },
            sProcessing: "Đang xử lý...",
            sLengthMenu: "Xem _MENU_ mục",
            sZeroRecords: "Không tìm thấy dòng nào phù hợp",
            sInfo: "Đang xem _START_ đến _END_ trong tổng số _TOTAL_ mục",
            sInfoEmpty: "Đang xem 0 đến 0 trong tổng số 0 mục",
            sInfoFiltered: "(được lọc từ _MAX_ mục)",
            sInfoPostFix: "",
            sSearch: "Tìm:",
            sUrl: "",
        },
        "dom": '<"toolbar">frtip',
        "lengthMenu": [[5, 25, 50, -1], [5, 25, 50, "All"]],
        "columnDefs": [
            { "type": 'formatted-num', targets: 0 },
            { "type": 'formatted-num', targets: 3 },
            { "type": 'formatted-num', targets: 4 },
        ],
        "processing": true,
        "ajax": {
            "processing": true,
            "url": "http://13.67.105.209:8000/merchant/orders_detail/" + id_order,
            "dataSrc": ""
        },

    });
});


function rating_customer(id_order){
    $("#wrapper").css("display","none");
    $("#loader").css("display","block");
    data = {
        'order_id': id_order,
        'customer_id' : $('#inputIdCus').val(),
        'num_star' : $('#inputRatingCus').val(),
    }

    $.ajax({
        url: 'http://13.67.105.209:8000/merchant/rating_customer',
        method: 'POST',
        contentType: 'application/x-www-form-urlencoded',
        data: data,
        success: function(response){
            if (response == 1){
                alert('Đánh giá thành công!');
                $("#wrapper").css("display","block");
                $("#loader").css("display","none");
                window.location.replace('/merchant/order')
            }
            else{
                alert(response)
                $("#wrapper").css("display","block");
                $("#loader").css("display","none");
            }
        }
    })
}


function change_state(order_id, state){
    $("#wrapper").css("display","none");
    $("#loader").css("display","block");
    $.ajax({
        url: 'http://13.67.105.209:8000/merchant/change_state/' + order_id + '/' + state,
        method: 'GET',
        success: function(response){
            if (response == 1){
                alert('Trạng thái đã thay đổi')
                $("#wrapper").css("display","block");
                $("#loader").css("display","none");
                window.location.replace('/merchant/order')
            }
            else{
                alert(response)
                $("#wrapper").css("display","block");
                $("#loader").css("display","none");
            }
        }
    })
}