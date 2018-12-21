
function add_product(id_product){
    $.ajax({
        url: 'http://54.213.242.175:8000/add/' + id_product,
        method: 'GET',
        success: function(response){
            if(response == 1){
                alert("Thêm thành công");
                window.location.replace('/cart');
                // qty = $('input[id=quantity]').val();
                // $('input[id=quantity]').val(parseInt(qty) + 1);
                // $('#cart_mobi').empty()
                // $('#cart_mobi').append('('+ (parseInt(qty) + 1) +') sản phẩm')
                // $('#cart_desk').empty()
                // $('#cart_desk').append('('+ (parseInt(qty) + 1) +') sản phẩm')
                // $('#mobile_cart').empty()
                // $('#mobile_cart').append((parseInt(qty) + 1))
                // $('#desktop_cart').empty()
                // $('#desktop_cart').append((parseInt(qty) + 1))
            }
            else{
                alert(response);
            }
        }
    })
}

function sub_product(id_product){
    $.ajax({
        url: 'http://54.213.242.175:8000/sub/' + id_product,
        method: 'GET',
        success: function(response){
            if(response == 1){
                alert("Đã giảm thành công");
                window.location.replace('/cart');
                // qty = $('input[id=quantity]').val();
                // $('input[id=quantity]').val(parseInt(qty) - 1);
                // $('#cart_mobi').empty()
                // $('#cart_mobi').append('('+ (parseInt(qty) - 1) +') sản phẩm')
                // $('#cart_desk').empty()
                // $('#cart_desk').append('('+ (parseInt(qty) - 1) +') sản phẩm')
                // $('#mobile_cart').empty()
                // $('#mobile_cart').append((parseInt(qty) - 1))
                // $('#desktop_cart').empty()
                // $('#desktop_cart').append((parseInt(qty) - 1))
            }
            else{
                alert(response);
            }
        }
    })
}

function set_qty(id_product, qty){
    $.ajax({
        url: 'http://54.213.242.175:8000/set_qty/' + id_product + '/' + qty,
        method: 'GET',
        success: function(response){
            if(response == 1){
                alert('Đã thay đổi số lượng sản phẩm thành công!');
                window.location.replace('/cart');
            }
            else{
                alert(response);
            }
        }
    })
}

function remove(id_product){
    $.ajax({
        url: 'http://54.213.242.175:8000/remove/' + id_product,
        method: 'GET',
        success: function(response){
            alert(response);
            window.location.replace('/cart');
        }
    })
}