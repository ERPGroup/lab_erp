// Edit Product

$(document).ready(function(){
  var check_url = $(location).attr('pathname').split('/');
  var id_product = check_url[check_url.length - 1]
  if($.inArray('edit', check_url)){
    $.ajax({
      url: 'http://localhost:8000/merchant/product/' + id_product,
      method: 'GET',
      contentType: 'application/json',
      success: function(response){
        console.log(response);
        $('#inputCode').val(response.code);
        $('#inputName').val(response.name);
        CKEDITOR.instances['inputDetail'].setData(response.detail);
        $('#inputOrigin').val(response.origin);
        $('#inputPrice').val(response.price_origin);
        for(var i = 0; i < response.list_category.length; i++){
          clickcategory(response.list_category[i].name_category, response.list_category[i].id )
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

        sort_list_img = (response.list_image).sort()
        list_data = []
        for(var i = 0; i < sort_list_img.length; i++){
          // // console.log(sort_list_img[i].image_link)
          Showimage(sort_list_img[i].image_link, sort_list_img[i].id);
          // // console.log('end');
          toDataURL(sort_list_img[i].image_link)
          .then((dataUrl) => {
            console.log(dataUrl);
          })
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

    var data = {
      'inputCode': $("#inputCode").val(),
      'inputName': $('#inputName').val(),
      'inputDetail': CKEDITOR.instances['inputDetail'].getData(),
      'inputPrice': $('#inputPrice').val(),
      'inputOrigin': $('#inputOrigin').val(),
      'inputCategory': Object.assign({}, list_category),
      'inputCountCategory': list_category.length,
      'inputImage': Object.assign({}, list_image),
      'inputCountImage': list_image.length,
      'inputVersion': Object.assign({}, list_version),
      'inputCountProduct': list_version.length,
    }
    console.log(data)
    $.ajax({
      url: 'http://localhost:8000/merchant/product/' + id_product,
      method: 'POST',
      contentType: 'application/x-www-form-urlencoded',
      data: data,
      success: function(response){
        console.log(response);
        if(response == 1){
          alert('da sua san pham');
        }
      },
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
    xhr.open('GET', 'http://localhost:8000' + image_link);
    xhr.responseType = 'blob';
    xhr.send();
}

const toDataURL = url => fetch(url)
  .then(response => response.blob())
  .then(blob => new Promise((resolve, reject) => {
    const reader = new FileReader()
    reader.onloadend = () => resolve(reader.result )
    reader.onerror = reject
    reader.readAsDataURL(blob)
  }))


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
          result_1 += '<a href="#" onclick="$(\'#' + image_id + '\').remove(); reload(); delete_image('+ image_id +'); return false;" ><i class="fa fa-remove"></i></a>'
          result_1 += '</div>'
          result_1 += '</div>'
          $el.append(result_1);
          $el.data('lightGallery').destroy(true);
          $el.lightGallery();
        }
        console.log(xhr.response);
        reader.readAsDataURL(xhr.response);
    }
    xhr.open('GET', 'http://localhost:8000' + image_link);
    xhr.responseType = 'blob';
    xhr.send();
}