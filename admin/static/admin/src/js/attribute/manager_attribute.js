$(document).ready(function (){
    var table = $('#tbl_manager_attributes').dataTable({
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
        { "type": "numeric-comma", targets: 5 }
        ],
        "processing": true,
        "ajax": {
            "processing": true,
            "url": "http://localhost:8000/admin/attributes",
            "dataSrc": ""
        },
    });
});
