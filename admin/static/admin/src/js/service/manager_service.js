$(document).ready(function (){
    var table = $('#tbl_manager_servies').dataTable({
        language: {
            paginate: {
                previous: "<i class='fa fa-arrow-left'></i>",
                next: "<i class='fa fa-arrow-right'></i>"
            },
            bFilter: true,
            sProcessing: "Đang xử lý...",
            sLengthMenu: "Xem _MENU_ mục",
            sZeroRecords: "Không tìm thấy dòng nào phù hợp",
            sInfo: "Đang xem _START_ đến _END_ trong tổng số _TOTAL_ mục",
            sInfoEmpty: "Đang xem 0 đến 0 trong tổng số 0 mục",
            sInfoFiltered: "(được lọc từ _MAX_ mục)",
            sInfoPostFix: "",
            sSearch: "Tìm kiếm:",
            sUrl: "",
        },
        "dom": '<"toolbar">frtip',
        "lengthMenu": [[10, 25, 50, -1], [10, 25, 50, "All"]],
        "columnDefs": [
        { "type": "numeric-comma", targets: 4 }
        ],
        "processing": true,
        "ajax": {
            "processing": true,
            "url": "http://54.213.242.175:8000/admin/services?table=true",
            "dataSrc": ""
        },
    });

    // $.ajax({
    //     url: 'http://54.213.242.175:8000/admin/services',
    //     method: 'GET',
    //     contentType: 'application/json',
    //     success: function(response){
    //         console.log(response);
    //         for(var i = 0; i < response.length; i++){
    //             item_id = response[i]['pk']
    //             item = response[i]['fields']
    //             var table = $('#tbl_manager_servies').dataTable()
    //             table.row.add([
    //                 item.service_name,
    //                 item.value,
    //                 item.day_limit,
    //                 item.amount,
    //                 item.is_active,
    //             ]).draw();
    //             var row = ''
    //             row += '<tr>'
    //             row += '<td><a href="/admin/service/edit/'+ item_id +'">'+ item.service_name +'</a></td>'
    //             row += '<td>'+ item.value +' tin</td>'
    //             row += '<td>'+ item.day_limit +' ngày</td>'
    //             row += '<td>'+ item.amount +' VNĐ</td>'
    //             if(item.is_active == true)
    //                 row += '<th style="color:green">Đang bán</th>'
    //             else
    //                 row += '<th style="color:red">Ngừng bán</th>'
    //             row += '</tr>'
    //             $('#content_table').append(row);
    //         }
    //     }
    // });
});
