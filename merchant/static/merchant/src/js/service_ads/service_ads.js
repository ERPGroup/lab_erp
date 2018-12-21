// Upload image
function readURL(input, output) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $(output).attr('src', e.target.result);
        }
        reader.readAsDataURL(input.files[0]);
    }
}
$("#upload-photo-1").change(function () {
    readURL(this, '#ads_1');
});
$("#upload-photo-2").change(function () {
    readURL(this, '#ads_2');
});
$("#upload-photo-3").change(function () {
    readURL(this, '#ads_3');
});
$(document).ready(function () {
    $('#upload-photo').change(function () {
        data = new FormData();
        files = $('#upload-photo').get(0).files;
        if (files.length > 0) {
            data.append('photo', files[0]);
        }
        $.ajax({
            url: 'http://54.213.242.175:8000/merchant/upload_image_ads/',
            method: 'POST',
            contentType: false,
            processData: false,
            data: data,
            success: function (response) {
                // alert(response);
                if (response > 0) {
                    var reader = new FileReader()
                    reader.onload = function (e) {
                        var result_1 = ''
                        result_1 = '<div class="col-lg-6 no_padding ' + response +
                            ' count_image item" id="' + response + '" data-src="' +
                            e.target.result + '">'
                        result_1 += '<img src="' + e.target.result + '" />'
                        result_1 += '<div class="action_image">'
                        result_1 += '<a href="#"><i class="fa fa-check"></i></a>'
                        result_1 += '<a href="#" onclick="$(\'#' + response +
                            '\').remove(); reload(); return false;" ><i class="fa fa-remove"></i></a>'
                        result_1 += '</div>'
                        result_1 += '</div>'
                        $el.append(result_1);
                        $el.data('lightGallery').destroy(true);
                        $el.lightGallery();
                    }
                    reader.readAsDataURL(files[0]);
                }
                if (response == 0) {
                    alert('Do khong phai file anh');
                }
                if (response == -2) {
                    alert('Dung luong anh khong duoc vuot qua 2MB');
                }
                if (response == -1) {
                    alert('Xay ra loi');
                }
            },
            error: function (jqXHR) {
                alert(jqXHR.responseText);
            }
        });
    });
});
$(document).ready(function () {
    if ($('#' + $('#select_type').val()).val() == "Slide") {
        document.getElementById('post_img_2').style.display = "block";
        document.getElementById('post_img_3').style.display = "block";
        document.getElementById('post_img_1').classList.remove("col-lg-12");
        document.getElementById('post_img_1').classList.add("col-lg-4");
    } else {
        document.getElementById('post_img_2').style.display = "none";
        document.getElementById('post_img_3').style.display = "none";
        document.getElementById('post_img_1').classList.add("col-lg-12");
        document.getElementById('post_img_1').classList.remove("col-lg-4");
    }
})
$('#select_type').change(function () {
    if ($('#' + this.value).val() == "Slide") {
        document.getElementById('post_img_2').style.display = "block";
        document.getElementById('post_img_3').style.display = "block";
        document.getElementById('post_img_1').classList.remove("col-lg-12");
        document.getElementById('post_img_1').classList.add("col-lg-4");
    } else {
        document.getElementById('post_img_2').style.display = "none";
        document.getElementById('post_img_3').style.display = "none";
        document.getElementById('post_img_1').classList.add("col-lg-12");
        document.getElementById('post_img_1').classList.remove("col-lg-4");
    }
})