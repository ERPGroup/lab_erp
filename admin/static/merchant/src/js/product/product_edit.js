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
        for(var i = 0; i < response.list_image.length; i++){
          Showimage(response.list_image[i].image_link, response.list_image[i].id);
        }
      },
    })
  }
});

function Showimage(image_link, image_id){
  var xhr = new XMLHttpRequest();
    xhr.onload = function() {
        var reader = new FileReader();
        console.log("reader" + this)
        reader.onloadend = function() {
            console.log(this)
            var result_1 = ''
            result_1 = '<div class="col-lg-6 no_padding ' + this + ' count_image item" id="'+ this +'" data-src="' + reader.result + '">'
            result_1 += '<img src="' + reader.result + '" />'
            result_1 += '<div class="action_image">'
            result_1 += '<a href="#"><i class="fa fa-check"></i></a>'
            result_1 += '<a href="#" onclick="$(\'#' + this + '\').remove(); reload(); return false;" ><i class="fa fa-remove"></i></a>'
            result_1 += '</div>'
            result_1 += '</div>'
            console.log(result_1)
            $el.append(result_1);
            $el.data('lightGallery').destroy(true);
            $el.lightGallery();
        }.bind(this)
        console.log(xhr.response);
        reader.readAsDataURL(xhr.response);
    }.bind(image_id);
    xhr.open('GET', 'http://localhost:8000' + image_link);
    xhr.responseType = 'blob';
    xhr.send();
}