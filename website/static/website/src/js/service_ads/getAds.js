$(document).ready(function () {
    $.ajax({
        url: 'https://laberp.pythonanywhere.com/getAds',
        type: 'POST',
        success: function (data) {
            if (data == -1) {

            } else {
                for (var i = 0; i < data.length; i++) {
                    if (data[i]['position'] == "Slide") {
                        $('#ads_slide_1').attr('src', "/ads/" + data[i]['img_1']);
                        $('#ads_slide_2').attr('src', "/ads/" + data[i]['img_2']);
                        $('#ads_slide_3').attr('src', "/ads/" + data[i]['img_3']);
                        $('#content_1').html('');
                        $('#content_1').html(data[i]['content_1']);
                        $('#content_2').html('');
                        $('#content_2').html(data[i]['content_2']);
                        $('#content_3').html('');
                        $('#content_3').html(data[i]['content_3']);
                        $('#ads_url_1').attr('href', data[i]['url_1']);
                        $('#ads_url_2').attr('href', data[i]['url_2']);
                        $('#ads_url_3').attr('href', data[i]['url_3']);
                    } else {
                        var output_url, output_img;
                        switch (data[i]['position']) {
                            case "Đầu trang":
                                output_url = "#ads_url_top";
                                output_img = "#ads_top";
                                break;
                            case "Cuối trang":
                                output_url = "#ads_url_bottom";
                                output_img = "#ads_bottom";
                                break;
                            case "Giữa trang":
                                output_url = "#ads_url_middle";
                                output_img = "#ads_middle";
                                break;
                            case "Bên phải slide 1":
                                output_url = "#url_right_1";
                                output_img = "#ads_right_1";
                                break;
                            case "Bên phải slide 2":
                                output_url = "#url_right_2";
                                output_img = "#ads_right_2";
                                break;

                            default:
                                output_img = "";
                                output_img = "";
                        }
                        $(output_url).attr('href', data[i]['url_1']);
                        $(output_img).attr('src', "/ads/" + data[i]['img_1']);
                    }
                }
            }
        }
    })
})