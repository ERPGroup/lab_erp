CKEDITOR.replace('editor1',
  {
    // Define the toolbar groups as it is a more accessible solution.
    toolbarGroups: [
      { 'name': 'basicstyles', 'groups': ['basicstyles'] },
      { 'name': 'links', 'groups': ['links'] },
      { 'name': 'paragraph', 'groups': ['list', 'blocks'] },
      { 'name': 'document', 'groups': ['mode'] },
      { 'name': 'insert', 'groups': ['insert'] },
      { 'name': 'styles', 'groups': ['styles'] }
    ],
    // Remove the redundant buttons from toolbar groups defined above.
    removeButtons: 'Underline,Strike,Subscript,Superscript,Anchor,Styles,Specialchar'
  }
)
var colors = new Array('#39b3d7', '#286090', '#5cb85c', '#ec971f', '#d9534f', '#39b3d7', '#d9534f', '#5cb85c', '#ec971f', '#286090')
function combination (a, b) {
  var count = 0
  var result = []
  for (var i = 0; i < a.length; i++) {
    for (var j = 1; j < b.length; j++) {
      result[count] = a[i] + " | " + b[j].textContent
      count++
      // if(count>10)
      // {
      //   alert('Hệ thống chỉ hỗ trợ tối đa 10 phiên bản');
      //   return false;
      // }
    }
  }
  return result
}

function get_verison(){
  var input  = $('.count_value');
  var result = []
  this_value_0 = $('.this_value_0')
  for (var i = 1; i < this_value_0.length; i++) {
    result.push(this_value_0[i].textContent)
  }
  if (input.length > 1){
    for (var i = 1; i < input.length; i++){
      var input_2 = $('.this_value_' + i);
      result = combination(result, input_2)
    }
  }
  return result
}


function load_vesion_product () {
  var input = document.getElementsByClassName('count_value')
  var this_value = document.getElementsByClassName('this_value_0')
  var result = []
  var i_count = 0
  for (var i = 1; i < this_value.length; i++) {
    result[i_count] = this_value[i].textContent
    i_count++
  }
  if (input.length > 1) {
    for (var i = 1; i < input.length; i++) {
      var input_2 = document.getElementsByClassName('this_value_' + i)
      result = combination(result, input_2)
    }
  }
  var x = document.getElementById('result_attribute')
  x.innerHTML = ''
  for (var i = 0; i < result.length; i++) {
    var html = ''
    html += '<tr>'
    html += '<td><input type="checkbox" checked id="check_vesion_'+ i +'" class="form-check-input"></td>'
    html += '<td><span style="color:#d9534f">' + result[i] + '</span></td>'
    html += '<td><input type="number" class="price_product" id="price_product_' + (i) + '" min="0" value=""></td>'
    html += '</tr>'
    x.innerHTML += html
  }
}


function addmore_att (content, name_tag) {
  m = $('#' + name_tag + ' > div')
  list_value = []
  for (i = 0 ; i < m.length; i++){
    list_value.push(m[i].textContent);
  }
  if(content == ''){
    return -1;
  }
  if (list_value.includes(content)){
    alert('Loi! tag bi trung');
    load_vesion_product();
    check_button_submit();
  }else{
    var uuid = guid();
    var attribute = '';
    attribute += '<div class="label label-info ' + name_tag + '" id="' + uuid + '">' + content + '<a href="#" onclick="$(\'#' + uuid + '\').remove(); load_vesion_product(); return false;"><i class="fa fa-remove"></i></a></div>';
    $('#' + name_tag).append(attribute);
    load_vesion_product();
    check_button_submit();
  }
}

function guid () {
  function s4 () {
    return Math.floor((1 + Math.random()) * 0x10000)
      .toString(16)
      .substring(1)
  }
  return s4() + s4() + '-' + s4() + '-' + s4() + '-' + s4() + '-' + s4() + s4() + s4()
}

function addmore_attribute () {
  var uuid = guid();
  var count_value = $('.count_value').length;
  var new_value = 'this_value_' + count_value;
  var new_name = 'name_attribute_' + count_value;
  var attribute = ''
  attribute += '<div class="form-group"><div class="col-lg-4"><input id="' + new_name + '" type="text" placeholder="Tên thuộc tính"></div><div class="col-lg-8"><input class="count_value ' + new_value + '" type="text" onkeypress="if (event.keyCode==13) {addmore_att(this.value,\'' + new_value + '\'); this.value=\'\'; return false; }" placeholder="Giá trị" width="100%" style="width:100%"></div>'
  attribute += '<div class="clearfix"></div></div>'
  attribute += '<div class="form-group">'
  attribute += '<div class="col-lg-8 col-xs-offset-4" id="' + new_value + '"></div><div class="clearfix"></div>'
  attribute += '</div>'
  $("#add_more").append(attribute);
}

// list attributes
$(document).ready(function(){
  $.ajax({
    url: 'http://localhost:8000/merchant/attributes',
    method: 'GET',
    contentType: 'application/json',
    success: function(response){
      for (var i = 0; i < response.length; i++){
        var count_value = $('.count_value').length;
        var new_value = 'this_value_' + count_value;
        var new_name = 'name_attribute_' + count_value;
        var attribute = ''
        attribute += '<div class="form-group"><div class="col-lg-4"><input id="' + new_name + '" data-id="'+ response[i].pk +'" type="text" readonly value="'+ response[i].fields.label +'"></div><div class="col-lg-8"><input class="count_value ' + new_value + '" type="text" onkeypress="if (event.keyCode==13) {addmore_att(this.value,\'' + new_value + '\'); this.value=\'\';  return false; }" placeholder="Giá trị" width="100%" style="width:100%"></div>'
        attribute += '<div class="clearfix"></div></div>'
        attribute += '<div class="form-group">'
        attribute += '<div class="col-lg-8 col-xs-offset-4" id="' + new_value + '"></div><div class="clearfix"></div>'
        attribute += '</div>'
        $("#add_more").append(attribute);
      }
    },
  })
})

function scrollto (id) {
  var etop = $('#' + id).offset().top
  $(window).scrollTop(etop)
}

// Upload image
$(document).ready(function(){
  $('#upload-photo').change(function(){
    data = new FormData();
    files = $('#upload-photo').get(0).files;

    if (files.length > 0){
      data.append('photo', files[0]);
    }

    $.ajax({
      url: 'http://localhost:8000/merchant/upload_image',
      method: 'POST',
      contentType: false,
      processData: false,
      data: data,
      success: function(response){
        // alert(response);
        if (response == -3)
          alert('Vui long dang nhap de them san pham');
        if (response > 0){
          var reader = new FileReader()
          reader.onload = function (e) {
              var result_1 = ''
              result_1 = '<div class="col-lg-6 no_padding ' + response + ' count_image item" id="'+ response +'" data-src="' + e.target.result + '">'
              result_1 += '<img src="' + e.target.result + '" />'
              result_1 += '<div class="action_image">'
              result_1 += '<a href="#"><i class="fa fa-check"></i></a>'
              result_1 += '<a href="#" onclick="$(\'#' + response + '\').remove(); reload(); delete_image('+ response +'); return false;" ><i class="fa fa-remove"></i></a>'
              result_1 += '</div>'
              result_1 += '</div>'
              $el.append(result_1);
              $el.data('lightGallery').destroy(true);
              $el.lightGallery();
          }
          reader.readAsDataURL(files[0]);
        }
        if (response == 0){
          alert('Do khong phai file anh');
        }
        if (response == -2){
          alert('Dung luong anh khong duoc vuot qua 2MB');
        }
        if (response == -1){
          alert('Xay ra loi');
        }
      },
      error: function(jqXHR){
        alert(jqXHR.responseText);
      }
    });
  });
});


function delete_image(id_image){
  $.ajax({
    url: 'http://localhost:8000/merchant/delete_image/' + id_image,
    method: 'DELETE',
    success: function(response){
      $('#upload_photo').val(''); 
      alert(response);
    }
  })
}

// List Categorys
$(document).ready(function(){
  $.ajax({
    url: 'http://localhost:8000/merchant/categorys',
    method: 'GET',
    contentType: 'application/json',
    success: function(response){

      for (var item = 0; item < response.length; item++){
        html = '<li><a href="#" data-id-category='+ response[item].pk +' onclick="clickcategory($(this).text(), $(this).attr(\'data-id-category\'));">'+ response[item].fields.name_category +'</a></li>'
        $("#list-category").append(html)
      }
      // console.log(response);
    },  
  })
});

function load_category_autocomplete(keyword){
  $("#list-category").empty()
  $.ajax({
    url: 'http://localhost:8000/merchant/categorys?keyword=' + keyword,
    method: 'GET',
    contentType: 'application/json',
    success: function(response){
      for (var item = 0; item < response.length; item++){
        html = '<li><a href="#" data-id-category='+ response[item].pk +' onclick="clickcategory($(this).text(), $(this).attr(\'data-id-category\'));">'+ response[item].fields.name_category +'</a></li>'
        $("#list-category").append(html)
      }
    },  
  })
}


// Choose Category
function clickcategory(name, id) {
  var category_search = $('.category_search')
  var check = false;
  for( var i = 0; i < category_search.length; i++){
    if(category_search[i].id == id){
      check = true;
    }
  }
  if (check == false){
    var html = '';
    html += '<div class="col-lg-12 category_search" id="' + id + '" onclick="$(this).remove();">' + name + '</div>'
    $('#value_category').append(html);
  }
}

function check_button_submit(){
    count_product_vesion = $("#result_attribute > tr").length;
    if (count_product_vesion == 0){
      $('#submit').attr('disabled', 'disabled');
    }
    else {
      $('#submit').removeAttr('disabled');
    }
  }
  
  $(document).ready(function(){
    count_product_vesion = $("#result_attribute > tr").length;
    if (count_product_vesion == 0){
      $('#submit').attr('disabled', 'disabled');
    }
    else {
      $('#submit').removeAttr('disabled');
    }
  });

  // function check_price(){
  //   var check_url = $(location).attr('pathname').split('/');
  //   var id_product = check_url[check_url.length - 1]
  //   $.ajax({
  //     url: 'http://localhost:8000/merchant/product/' + id_product,
  //     method: 'GET',
  //     contentType: 'application/json',
  //     success: function(response){
  //       for(var i = 0; i < response.list_price.length; i++)
  //           $('#price_product_'+ i).val(response.list_price[i])
  //     }
  //   })
  // }

$(document).ready(function(){

  $('#inputDiscount').change(function(){
    discount = $('#inputDiscount').val()
    console.log(discount)
    if (discount > 100 || discount < 0){
      $('#inputDiscount').val(0)
    }
  })
})