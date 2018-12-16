/* Plugin Datatables */
    /* Create an array with the values of all the input boxes in a column */
    $.fn.dataTable.ext.order['dom-text'] = function (settings, col) {
        return this.api().column(col, { order: 'index' }).nodes().map(function (td, i) {
            return $('input', td).val();
        });
    }

    /* Create an array with the values of all the input boxes in a column, parsed as numbers */
    $.fn.dataTable.ext.order['dom-text-numeric'] = function (settings, col) {
        return this.api().column(col, { order: 'index' }).nodes().map(function (td, i) {
            return $('input', td).val() * 1;
        });
    }
    /* End */
    $(document).ready(function () {
        var table = $('#tbl_manager_users').dataTable({
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
            "createdRow": function (row, data, index) {
                if (data[2] == "Quản lý") {
                    $('td', row).addClass('highlight');
                }
            },
            "columns": [
                null,
                null,
                null,
                { "orderDataType": "dom-text-numeric" },
                null,
            ],
            "ajax": {
                "processing": true,
                "url": "https://laberp.pythonanywhere.com/admin/users?table=true",
                "dataSrc": ""
            },
        });
        var tool_bar = '';
        tool_bar += '<div class="column_hidden">Bật/Tắt cột hiển thị: '
        tool_bar += '<a class="toggle-vis" data-column="0">Email</a> - <a class="toggle-vis" data-column="1">Họ và tên</a> - ';
        tool_bar += '<a class="toggle-vis" data-column="2">Loại tài khoản</a> - <a class="toggle-vis" data-column="3">Đánh giá</a> - ';
        tool_bar += '<a class="toggle-vis" data-column="4">Trạng thái</a>';
        tool_bar += '</div>'
        $("div.toolbar").html(tool_bar);
        $('a.toggle-vis').on('click', function (e) {
            e.preventDefault();
            // Get the column API object
            var column = table.api().column($(this).attr('data-column'));
            // Toggle the visibility
            column.visible(!column.visible());
        });
        $('#tbl_manager_users tbody').on('click', 'tr', function () {
            $(this).toggleClass('selected');
        });
        $('#select_status').change(function () {
            regExSearch = '^' + this.value + '$';
            if (this.value == "Tất cả") {
                table.api().columns(4).search('').draw();
            }
            else {
                table.api().columns(4).search(regExSearch, true, false).draw();
            }
        });
        $('#select_position').change(function () {
            if (this.value == "Tất cả") {
                table.api().columns(2).search('').draw();
            }
            else {
                table.api().columns(2).search(this.value).draw();
            }
        });
    });