function load_ads(key_search, output_url, output_img) {
    $.ajax({
        url: 'http://localhost:8000/getAds',
        data: {
            key: key_search,
        },
        type: 'POST',
        success: function (data) {
            if (data == -1) {

            } else {
                $(output_url).attr('href', data['url']);
                $(output_img).attr('src', "http://localhost:8000/ads/" + data['img']);
            }
        }
    })
}
$(document).ready(function () {
    load_ads("Đầu trang", "#ads_url_top", "#ads_top")
    load_ads("Cuối trang", "#ads_url_bottom", "#ads_bottom")
    load_ads("Giữa trang", "#ads_url_middle", "#ads_middle")
    load_ads("Bên phải slide 1", "#url_right_1", "#ads_right_1")
    load_ads("Bên phải slide 2", "#url_right_2", "#ads_right_2")
    //Slide
    $.ajax({
        url: 'http://localhost:8000/getAds',
        data: {
            key: "Slide",
        },
        type: 'POST',
        async: false,
        success: function (data) {
            if (data == -1) {} else {
                $('#ads_slide_1').attr('src', "http://localhost:8000/ads/" + data['img_1']);
                $('#ads_slide_2').attr('src', "http://localhost:8000/ads/" + data['img_2']);
                $('#ads_slide_3').attr('src', "http://localhost:8000/ads/" + data['img_3']);
                $('#content_1').html('');
                $('#content_1').html(data['content_1']);
                $('#content_2').html('');
                $('#content_2').html(data['content_2']);
                $('#content_3').html('');
                $('#content_3').html(data['content_3']);
                $('#ads_url_1').attr('href', data['url_1']);
                $('#ads_url_2').attr('href', data['url_2']);
                $('#ads_url_3').attr('href', data['url_3']);
            }
        }
    })
});