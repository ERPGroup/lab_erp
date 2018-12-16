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
        "columnDefs": [
            { "type": 'formatted-num', targets: 0 },
            { "type": 'formatted-num', targets: 2 },
            { "type": 'date-eu', targets: 3 }
        ],
        "processing": true,
        "ajax": {
            "processing": true,
            "url": "http://13.67.105.209:8000/admin/getAllPost",
            "dataSrc": ""
        },
        "columns": [{
                "data": "ads_name"
            },
            {
                "data": "user"
            },
            {
                "data": "date_start"
            },
            {
                "data": "position"
            },
            {
                "data": "status"
            },
        ],
    });
    var tool_bar = '';
    tool_bar += '<div class="col-xs-8 no_padding">';
    tool_bar += '<span>Trạng thái: </span>';
    tool_bar += '<select style="width:50%;display:inline-block;" id="select_type" class="form-control">';
    tool_bar += '<option>Tất cả</option>';
    tool_bar += '<option>Đang xử lý</option>';
    tool_bar += '<option>Không duyệt</option>';
    tool_bar += '<option>Duyệt</option>';
    tool_bar += '</select>';
    tool_bar += '</div>';
    $("div.toolbar").html(tool_bar);
    $('#select_type').change(function () {
        regExSearch = '^' + this.value + '$';
        if (this.value == "Tất cả") {
            table.api().columns(4).search('').draw();
        }
        else {
            table.api().columns(4).search(regExSearch, true, false).draw();
        }
    });
});