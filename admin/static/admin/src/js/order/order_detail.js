$(document).ready(function () {

    var check_url = $(location).attr('pathname').split('/');
    var id_order = check_url[check_url.length - 1]
    $.ajax({
        url: 'http://localhost:8000/admin/order/' + id_order,
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
            "url": "http://localhost:8000/admin/orders_detail/" + id_order,
            "dataSrc": ""
        },

    });
});
