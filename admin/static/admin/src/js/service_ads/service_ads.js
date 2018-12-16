$(document).ready(function () {
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
        "lengthMenu": [
            [10, 25, 50, -1],
            [10, 25, 50, "All"]
        ],
        "processing": true,
        "ajax": {
            "processing": true,
            "url": "http://13.67.105.209:8000/admin/getAllAds",
            "dataSrc": ""
        },
        "columns": [{
                "data": "service_name"
            },
            {
                "data": "position"
            },
            {
                "data": "day_limit"
            },
            {
                "data": "amount"
            },
            {
                "data": "is_active"
            },
        ],

    });
    var tool_bar = '';
    tool_bar += '<div class="col-xs-8 no_padding">';
    tool_bar += '<span>Trạng thái: </span>';
    tool_bar += '<select style="width:50%;display:inline-block;" id="select_type" class="form-control">';
    tool_bar += '<option>Tất cả</option>';
    tool_bar += '<option>Kích hoạt</option>';
    tool_bar += '<option>Bị khóa</option>';
    tool_bar += '</select>';
    tool_bar += '</div>';
    $("div.toolbar").html(tool_bar);
    $('#select_type').change(function () {
        regExSearch = '^' + this.value + '$';
        if (this.value == "Tất cả") {
            table.api().columns(4).search('').draw();
        } else {
            table.api().columns(4).search(regExSearch, true, false).draw();
        }
    });
    var x = document.getElementById("dataTables-example_processing");
    x.style.display = "none";
});