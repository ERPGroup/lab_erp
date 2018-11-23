
function add_product(id_product){
    $.ajax({
        url: 'http://localhost:8000/add/' + id_product,
        method: 'GET',
        success: function(response){
            alert(response)
        }
    })
}
