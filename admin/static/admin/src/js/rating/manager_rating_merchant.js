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
$(document).ready(function () {

    var check_url = $(location).attr('pathname').split('/');
    var id_account = check_url[check_url.length - 1]

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
        "lengthMenu": [[10, 25, 50, -1], [10, 25, 50, "All"]],
        "columnDefs": [
            { "type": 'formatted-num', targets: 0 },
            { "type": 'formatted-num', targets: 2 },
            { "type": 'date-eu', targets: 3 }
        ],
        "order": [[ 0, "desc" ]],
        "processing": true,
        "ajax": {
            "processing": true,
            "url": "https://laberp.pythonanywhere.com/admin/rating_mer/"+ id_account +"?table=true",
            "dataSrc": ""
        },
    });

    $('#back').attr('href', '/admin/user/see/' + id_account)

    $.ajax({
        url: 'https://laberp.pythonanywhere.com/admin/user/' + id_account,
        method:  'GET',
        contentType: 'application/json',
        success: function(response){
            var tool_bar = '';
            tool_bar += '<div class="col-xs-8 no_padding">';
            tool_bar += '<span>Người bán: <a href="/admin/user/see/'+ id_account +'">'+ response.name +'</a></span>';
            tool_bar += '</div>';
            $("div.toolbar").html(tool_bar);
        }
    })
});


function update_rating_mer(id_rating, action){
    data = {
        'id_rating': id_rating,
        'action' : action,
    }

    $.ajax({
        url: 'https://laberp.pythonanywhere.com/admin/update_rating_merchant',
        method: 'POST',
        contentType: 'application/x-www-form-urlencoded',
        data: data,
        success: function(response){
            if (response == 1){
                alert('Cập nhật thành công!');
                window.location.reload();
            }
            else{
                alert(response)
            }
        }
    })
}
