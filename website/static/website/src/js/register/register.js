$('#select_type_user').change(function () {
    var result = document.getElementById('type_users_selected');
    if (this.value == 0)
        result.style.display = 'none';
    else
        result.style.display = 'block';
})