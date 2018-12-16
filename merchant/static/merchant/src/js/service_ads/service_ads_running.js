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

        "columnDefs": [
            { "type": 'date-eu', targets: 3 },
            { "type": 'date-eu', targets: 2 }
        ],
        "processing": true,
        "ajax": {
            "processing": true,
            "url": "https://laberp.pythonanywhere.com/merchant/getAllAdsRunning",
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
                "data": "date_end"
            },
            {
                "data": "status"
            },
        ],
    });
});