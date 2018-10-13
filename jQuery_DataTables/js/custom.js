
$.fn.dataTable.ext.search.push(
function (settings, data, dataIndex) {
    var startDate = Date.parse($('#start-date').val(), 10);
    var endDate = Date.parse($('#end-date').val(), 10);
    var columnDate = Date.parse(data[4]) || 0; // use data for the age column

    if ((isNaN(startDate) && isNaN(endDate)) ||
         (isNaN(startDate) && columnDate <= endDate) ||
         (startDate <= columnDate && isNaN(endDate)) ||
         (startDate <= columnDate && columnDate <= endDate)) {
        return true;
    }
    return false;
}
);

$.fn.dataTableExt.oApi.fnMultiFilter = function (oSettings, oData) {
    for (var key in oData) {
        if (oData.hasOwnProperty(key)) {
            for (var i = 0, iLen = oSettings.aoColumns.length ; i < iLen ; i++) {
                if (oSettings.aoColumns[i].sName == key) {
                    /* Add single column filter */
                    oSettings.aoPreSearchCols[i].sSearch = oData[key];
                    break;
                }
            }
        }
    }
    this.oApi._fnReDraw(oSettings);
};



$(document).ready(function () {

    // Initialize DatePicker
    $('.input-group.date').datepicker({
        format: "mm/dd/yy",
        orientation: "top left",
        autoclose: true,
        todayHighlight: false,
        toggleActive: false
    });


    var table = $('#example').DataTable(
        {

            "columnDefs": [

                {
                    "targets": [3],
                    "visible": true,
                    "searchable": true,
                    "type": "num"
                },
                {
                    "targets": [2],
                    "visible": true,
                    "searchable": true,
                    "type": "string"
                },
                {
                    "targets": [1],
                    "visible": true,
                    "searchable": true,
                    "type": "string"
                },
                {
                    "targets": [0],
                    "visible": true,
                    "searchable": true,
                    "type": "string"
                },
                {
                    "aoColumns": [
              { "sName": "name" },
              { "sName": "position" },
              { "sName": "office" },
              { "sName": "age" },
              { "sName": "startdate" },
                { "sName": "salary" }
                    ]
                }
            ]
        });

    //Clear all checkbox
    $('.btn-fltr-clearAll').click(function () {
        myFilterBox = $(this).parent().parent().parent();
        $(myFilterBox).find('input[type=checkbox]').each(function () {
            // some staff
            this.checked = false;
        });
    });

    //Select all checkbox
    $('.btn-fltr-selectAll').click(function () {
        myFilterBox = $(this).parent().parent().parent();
        $(myFilterBox).find('input[type=checkbox]').each(function () {
            // some staff
            this.checked = true;
        });
    });

    // Event listener to the two range filtering inputs to redraw on input
    $('#start-date, #end-date').change(function () {
        table.draw();
    });

    //Event Listener for custom radio buttons to filter datatable
    $('.customRadioButton').change(function () {
        table.columns(2).search(this.value).draw();
    });

    //Event Listener for custom textbox to filter datatable
    $('#customSearchTextBox').on('keyup keypress change', function () {
        table.search(this.value).draw();
    });



    //custom checkbox for column based filter
    $('.custom-checkbox').change(function () {
        changeTable(true);
    });

    //Event Listener for button click for Selecting all columns and Deselecting
    $('.btn-fltr-clearAll, .btn-fltr-selectAll').click(function () {
        changeTable(true)
    })


    //This function does most of part of filtering in our demo. As the datatable once instantiated to be searchable or not, it is not possible to change its properties like sortable, searchable, etc without reinstantiating the datatable. 
    //This function gets the values from checkbox, textbox and filter buttons and sets the properties of the datatable.
    //Based on the selected checkbox, this function will set those particular columns to be searchable while make rest as false
    function changeTable(checkBoxStatus) {

        i = 0;
        var arr = [];
        $('input:checkbox[name="searchby-column"]:checked').each(function () {
            arr[i++] = parseInt(this.value);
        });
        var searchBox = $('#customSearchTextBox').val();

        if (checkBoxStatus) {

            if (arr[0] == null) {
                arr = [0, 1, 2, 3, 4, 5];
            }
            table.destroy();

            table = $('#example').DataTable(
                {
                    "pagingType": "simple",
                    "iDisplayLength": 5,
                    "iDisplayStart": 1,
                    columnDefs: [
                       { targets: arr, searchable: true },
                       { targets: '_all', searchable: false }
                    ]
                }
            );
        }

        //use custom search box
        table.search(searchBox).draw();
    }


    //Hightlight our search text in the datatable
    table.on('draw', function () {
        var body = $(table.table().body());

        //We can change the highlight color in dataTables.searchHighlight.css
        body.unhighlight();
        body.highlight(table.search());
    });
});