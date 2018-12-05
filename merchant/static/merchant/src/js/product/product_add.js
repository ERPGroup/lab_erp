// Add product
$(document).ready(function(){
  $('#submit').click(function(){
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

    for(item =0; item < list_version.length; item++){
      if (list_version[item]['price'] == ''){
        alert('Giá phiên bản không hợp lệ');
        return
      }
      
    }

    if (list_category.length < 1 || list_category.length > 2){
      alert('Số lượng phiên bản không nhỏ hơn 1 hoặc lớn hơn 2');
      return
    }

    if (values_image.length < 1){
      alert('Số lượng phiên bản không nhỏ hơn 1 ');
      return
    }

    if (values_image.list_tag > 3){
      alert('Số lượng phiên bản không lớn hơn 3 ');
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

    console.log(data)
    $.ajax({
      url: 'http://localhost:8000/merchant/product',
      method: 'POST',
      contentType: 'application/x-www-form-urlencoded',
      data: data,
      success: function(response){
        console.log(response);
        if(response == 1)
          alert('da them san pham');
        else
          alert(response)
      },
    });
  });
});

