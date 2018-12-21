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
    var table = $('#dataTables_posted').dataTable({
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
            sSearch: "Tìm kiếm: ",
            sUrl: "",
        },
        "dom": '<"toolbar">frtip',
        "order": [[ 0, "desc" ]],
        "columnDefs": [
            { "type": 'formatted-num', targets: 0 },
            { "type": 'formatted-num', targets: 2 },
            { "type": 'date-eu', targets: 3 }
        ],
        "processing": true,
        "ajax": {
            "processing": true,
            "url": "http://54.213.242.175:8000/admin/posts",
            "dataSrc": ""
        },
    });

    var tool_bar = '';
    tool_bar += '<div class="col-xs-6 no_padding">';
    tool_bar += '<span>Loại tin: </span>';
    tool_bar += '<select style="width:50%;display:inline-block;" id="select_type" class="form-control">';
    tool_bar += '</select>';
    tool_bar += '</div>';

    tool_bar += '<div class="col-xs-6 no_padding">';
    tool_bar += '<span>Trạng thái: </span>';
    tool_bar += '<select style="width:50%;display:inline-block;" id="state" class="form-control">';
    tool_bar += '<option>Đang hiển thị</option>';
    tool_bar += '<option>Tất cả</option>';
    tool_bar += '<option>Ngừng hiển thị</option>';
    tool_bar += '<option>Hết hạn</option>';
    tool_bar += '<option>Bị khóa</option>';
    tool_bar += '</select>';
    tool_bar += '</div>';

    var keyword = 'Đang hiển thị'
    table.api().columns(5).search(keyword, true, false).draw();

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

    $('#state').change(function () {
        regExSearch = '^' + this.value + '$';
        if (this.value == "Tất cả") {
            table.api().columns(5).search('').draw();
        }
        else {
            table.api().columns(5).search(regExSearch, true, false).draw();
        }
    });

    $.ajax({
        url: 'http://54.213.242.175:8000/admin/services',
        method: 'GET',
        contentType: 'application/json',
        success: function(response){
            console.log(response)
            tool_bar = '<option>Tất cả</option>';
            for(var i = 0; i < response.length; i++)
                tool_bar += '<option>'+ response[i]['fields'].service_name +'</option>';
            $('#select_type').append(tool_bar)
        }
    })
});
