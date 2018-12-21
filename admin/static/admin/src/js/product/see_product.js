// Edit Product

$(document).ready(function(){
    var check_url = $(location).attr('pathname').split('/');
    var id_product = check_url[check_url.length - 1]
    if($.inArray('edit', check_url)){
      $.ajax({
        url: 'http://54.213.242.175:8000/admin/product/' + id_product,
        method: 'GET',
        contentType: 'application/json',
        success: function(response){
          $('#inputCode').val(response.code);
          $('#inputName').val(response.name);
          CKEDITOR.instances['inputDetail'].setData(response.detail);
          $('#inputOrigin').val(response.origin);
          $('#inputDiscount').val(response.discount_percent);

          
          if(response.is_activity == 0)
            $('#ignore').addClass('hidden')

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

          for(var i = 0; i < response.images.length; i++){
            Showimage('/product/' + response.images[i].image_link, response.images[i].id);
          }
        },
      })
    }

    $('#ignore').click(function(){
      $.ajax({
        url: 'http://54.213.242.175:8000/admin/product/' + id_product,
        method: 'POST',
        contentType: 'application/x-www-form-urlencoded',
        success: function(response){
          if(response == 1){
            alert('Sản phẩm đã bị khóa!');
            window.location.replace('/admin/manager_product')
          }
          else
            alert(response);
        }
      })
    })

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
      xhr.open('GET', 'http://54.213.242.175:8000' + image_link);
      xhr.responseType = 'blob';
      xhr.send();
  }