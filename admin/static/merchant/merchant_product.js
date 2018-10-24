CKEDITOR.replace('editor1',
{
    // Define the toolbar groups as it is a more accessible solution.
    toolbarGroups: [
        { "name": "basicstyles", "groups": ["basicstyles"] },
        { "name": "links", "groups": ["links"] },
        { "name": "paragraph", "groups": ["list", "blocks"] },
        { "name": "document", "groups": ["mode"] },
        { "name": "insert", "groups": ["insert"] },
        { "name": "styles", "groups": ["styles"] },
    ],
    // Remove the redundant buttons from toolbar groups defined above.
    removeButtons: 'Underline,Strike,Subscript,Superscript,Anchor,Styles,Specialchar',
}
);
var colors = new Array("#39b3d7", "#286090", "#5cb85c", "#ec971f", "#d9534f", "#39b3d7", "#d9534f", "#5cb85c", "#ec971f", "#286090");
function combination(a, b) {
var count = 0;
var result = new Array();
for (var i = 0; i < a.length; i++) {
    for (var j = 1; j < b.length; j++) {

        result[count] = '<span style="color:' + colors[i] + '">' + a[i] + '</span> | ' + b[j].textContent;
        count++;
    }
}
return result;
}
function load_2() {
var input = document.getElementsByClassName('count_value');
var this_value = document.getElementsByClassName('this_value_0');
var result = new Array();
var i_count = 0;
for (var i = 1; i < this_value.length; i++) {
    result[i_count] = this_value[i].textContent;
    i_count++;
}
if (input.length > 1) {
    for (var i = 1; i < input.length; i++) {
        var input_2 = document.getElementsByClassName("this_value_" + i);
        result = combination(result, input_2)
    }
}
var x = document.getElementById('result_attribute');
x.innerHTML = '';
for (var i = 0; i < result.length; i++) {
    var html = '';
    html += '<tr>';
    html += '<td><span style="color:red">' + result[i] + '</span></td>';
    html += '<td><input type="text" name="price_product_' + (i + 1) + '" maxlength="10" value=""></td>'
    html += '</tr>';
    x.innerHTML += html;
}
}
function addmore_att(a, b) {
var x = document.getElementById(b);
var uuid = guid();
var attribute = ''
attribute += '<div class="label label-info ' + b + '" id="' + uuid + '">' + a + '<a href="#" onclick="$(\'#' + uuid + '\').remove(); load_2(); return false;"><i class="fa fa-remove"></i></a></div>';
x.innerHTML += attribute;
load_2();
}
function guid() {
function s4() {
    return Math.floor((1 + Math.random()) * 0x10000)
        .toString(16)
        .substring(1);
}
return s4() + s4() + '-' + s4() + '-' + s4() + '-' + s4() + '-' + s4() + s4() + s4();
}
function addmore_attribute() {
var x = document.getElementById('add_more');
var uuid = guid();
var count_value = document.getElementsByClassName('count_value');
var new_value = 'this_value_' + count_value.length;
var new_name = 'name_attribute_' + count_value.length;
var attribute = '';
attribute += '<div class="form-group"><div class="col-lg-4"><input id="' + new_name + '" type="text" placeholder="Tên thuộc tính"></div><div class="col-lg-8"><input class="count_value ' + new_value + '" type="text" onkeypress="if (event.keyCode==13) {addmore_att(this.value,\'' + new_value + '\'); this.value=\'\'; return false; }" placeholder="Giá trị" width="100%" style="width:100%"></div>';
attribute += '<div class="clearfix"></div></div>';
attribute += '<div class="form-group">';
attribute += '<div class="col-lg-8 col-xs-offset-4" id="' + new_value + '"></div><div class="clearfix"></div>';
attribute += '</div>';
x.innerHTML += attribute;
}
function scrollto(id) {
    var etop = $('#' + id).offset().top;
    $(window).scrollTop(etop);
}
var el = document.getElementById("lightgallery");
lightGallery(el);
function readURL(input) {

    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            var result_1 = '';
            result_1 = '<li class="col-xs-6 col-sm-6 col-md-6 no_padding count_image" data-src="' + e.target.result + '"><a href=""><img class="img-responsive" src="' + e.target.result + '" alt="Thumb-1"></a></li>'
            el.insertAdjacentHTML('beforeend', result_1);
            window.lgData[el.getAttribute('lg-uid')].destroy(true);
            lightGallery(el);
            scrollto('lightgallery');
        };
        reader.readAsDataURL(input.files[0]);
    }
}