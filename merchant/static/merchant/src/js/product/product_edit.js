// Edit Product

$(document).ready(function(){
  var check_url = $(location).attr('pathname').split('/');
  var id_product = check_url[check_url.length - 1]
  if($.inArray('edit', check_url)){
    $.ajax({
      url: 'http://13.67.105.209:8000/merchant/product/' + id_product,
      method: 'GET',
      contentType: 'application/json',
      success: function(response){
        console.log(response);
        $('#inputCode').val(response.code);
        $('#inputName').val(response.name);
        CKEDITOR.instances['inputDetail'].setData(response.detail);
        $('#inputOrigin').val(response.origin);
        $('#inputDiscount').val(response.discount_percent);

        for(var i = 0; i < response.categories.length; i++){
          clickcategory(response.categories[i].name_category, response.categories[i].id )
        }

        for(var  i= 0; i < response.list_attr.length; i++){
          for(var j = 0; j < response.list_attr[i].length; j++){
            console.log('this_value_'+i);
            addmore_att(response.list_attr[i][j], 'this_value_'+i);
          }
        }
        for(var i = 0; i < response.list_price.length; i++){
            $('#price_product_'+ i).val(response.list_price[i])
        }

        for(var i = 0; i < response.tags.length; i++){
          addmore_tags(response.tags[i].tag_key)
        }
        sort_list_img = response.images
        list_data = []
        for(var i = 0; i < sort_list_img.length; i++){
          Showimage('/product/' + sort_list_img[i].image_link, sort_list_img[i].id)
        }
      },
    })
  }
  
  

  $('#edit').click(function(){
    version_value = get_verison()
    list_version = new Array()
    for (item= 0; item < version_value.length; item++){
      if ($('#check_vesion_' + item).is(':checked')){
        version = {
          'value': version_value[item],
          'price': $('#price_product_' + item).val(),
        }
        list_version.push(version);
      }
    }

    list_category  = new Array();
    values_category = $('#value_category > div');
    for (item = 0; item < values_category.length; item++){
      list_category.push(values_category[item].id)
    }

    list_image = new Array();
    values_image = $('#lightgallery > div')
    for (item = 0; item < values_image.length; item++){
      list_image.push(values_image[item].id)
    }

    list_tag = new Array();
    value_tag = $('.value_tags')
    for (item = 0; item < value_tag.length; item++){
      list_tag.push(value_tag[item].textContent)
    }

    // Check


    if (list_version.length < 1 || list_version.length > 10){
      alert('Số lượng phiên bản không nhỏ hơn 1 hoặc lớn hơn 10');
      return
    }

    for(item = 0; item < list_version.length; item++){
      if (list_version[item]['price'] == ''){
        alert('Giá phiên bản không hợp lệ');
        return
      }
      
    }

    if (list_category.length < 1 || list_category.length > 2){
      alert('Số lượng thư mục không nhỏ hơn 1 hoặc lớn hơn 2');
      return
    }

    if (values_image.length < 1){
      alert('Số lượng hình ảnh không nhỏ hơn 1 ');
      return
    }

    if (list_tag.length > 3){
      alert('Số lượng tag không lớn hơn 3 ');
      return
    }

    if ($("#inputCode").val() == ''){
      alert('Mã SKU không được để trống');
      return
    }

    if ($("#inputName").val() == ''){
      alert('Tên sản phẩm không được để trống');
      return
    }

    if ($("#inputDiscount").val() == ''){
      alert('Giảm giá không được để trống');
      return
    }

    if ($("#inputOrigin").val() == ''){
      alert('Nguồn gốc không được để trống');
      return
    }
    
    var data = {
      'inputCode': $("#inputCode").val(),
      'inputName': $('#inputName').val(),
      'inputDetail': CKEDITOR.instances['inputDetail'].getData(),
      'inputDiscount': $('#inputDiscount').val(),
      'inputOrigin': $('#inputOrigin').val(),
      'inputCategory': Object.assign({}, list_category),
      'inputTag': Object.assign({}, list_tag),
      'inputCountCategory': list_category.length,
      'inputCountTag': list_tag.length,
      'inputImage': Object.assign({}, list_image),
      'inputCountImage': list_image.length,
      'inputVersion': Object.assign({}, list_version),
      'inputCountProduct': list_version.length,
    }


    $.ajax({
      url: 'http://13.67.105.209:8000/merchant/product/' + id_product,
      method: 'POST',
      contentType: 'application/x-www-form-urlencoded',
      data: data,
      success: function(response){
        //console.log(response);
        if(response == 1){
          alert('Đã sửa sản phẩm');
          window.location.replace('/merchant/manager_product')
        }else{
          alert(response)
        }
      },
    });
  });

  $('#delete').click(function(){
    $.ajax({
      url: 'http://13.67.105.209:8000/merchant/product/' + id_product,
      method: 'DELETE',
      success: function(response){
        if(response == 1){
          alert('Sản phẩm đã xóa!');
          window.location.replace('/merchant/manager_product')
        }else
          alert(response);
      }
    });
  });

});



function get_blob(image_link, id_image, callback){
  var xhr = new XMLHttpRequest();
    xhr.onload = function() {
      var reader = new FileReader();
      reader.onloadend = function(){
        return callback(id_image, reader.result);
      }
      reader.readAsDataURL(xhr.response);
    }
    xhr.open('GET', 'http://13.67.105.209:8000' + image_link);
    xhr.responseType = 'blob';
    xhr.send();
}



function Showimage(image_link, image_id){
  var xhr = new XMLHttpRequest();
    xhr.onload = function() {
      console.log(this)
        var reader = new FileReader();
        reader.onloadend = function() {
          console.log(this)
          var result_1 = ''
          result_1 = '<div class="col-lg-6 no_padding ' + image_id + ' count_image item" id="'+ image_id +'" data-src="' + reader.result + '">'
          result_1 += '<img src="' + reader.result + '" />'
          result_1 += '<div class="action_image">'
          result_1 += '<a href="#"><i class="fa fa-check"></i></a>'
          result_1 += '<a href="#" onclick="$(\'#' + image_id + '\').remove(); $(\'#' + image_id + '\').remove(); alert(\'Đã xóa hình\'); return true;" ><i class="fa fa-remove"></i></a>'
          result_1 += '</div>'
          result_1 += '</div>'
          $el.append(result_1);
          $el.data('lightGallery').destroy(true);
          $el.lightGallery();
        }
        console.log(xhr.response);
        reader.readAsDataURL(xhr.response);
    }
    xhr.open('GET', 'http://13.67.105.209:8000' + image_link);
    xhr.responseType = 'blob';
    xhr.send();
}