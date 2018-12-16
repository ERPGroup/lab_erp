$(document).ready(function () {
  var x = $('#pid').val()
  $.ajax({
    url: 'https://laberp.pythonanywhere.com/admin/getDetailRegister',
    data: {
      inputID: x
    },
    type: 'POST',
    success: function (data) {
      if ($('#position').val() == 'Slide') {
        html = ''
        html += '<tr><td style="width:80px;text-align:center;">1</td>'
        html += '<td>' + data['url_1'] + '</td>'
        html += '<td><div class="tbl_thumb_product"><img src="/ads/' + data['img_1'] +
          '" alt="' + data['img_1'] + '"></div></td>'
        html += '<td>' + data['content_1'] + '</td></tr>'
        html += '<tr><td style="width:80px;text-align:center;">2</td>'
        html += '<td>' + data['url_2'] + '</td>'
        html += '<td><div class="tbl_thumb_product"><img src="/ads/' + data['img_2'] +
          '" alt="' + data['img_2'] + '"></div></td>'
        html += '<td>' + data['content_2'] + '</td></tr>'
        html += '<tr><td style="width:80px;text-align:center;">3</td>'
        html += '<td>' + data['url_3'] + '</td>'
        html += '<td><div class="tbl_thumb_product"><img src="/ads/' + data['img_3'] +
          '" alt="' + data['img_1'] + '"></div></td>'
        html += '<td>' + data['content_3'] + '</td></tr>'
        $('#tbl').html(html)
      } else {
        html = ''
        html += '<tr><td style="width:80px;text-align:center;">1</td>'
        html += '<td>' + data['url_1'] + '</td>'
        html += '<td><div class="tbl_thumb_product"><img src="/ads/' + data['img_1'] +
          '" alt="' + data['img_1'] + '"></div></td>'
        html += '<td>' + data['content_1'] + '</td></tr>'
        $('#tbl').html(html)
      }
      document.getElementById('post_id').value = data['id']
    }

  })
})
$('#submit').click(function (e) {
  e.preventDefault()
  var post_id = $('#post_id').val()
  var service_id = $('#pid').val()
  $.ajax({
    url: 'https://laberp.pythonanywhere.com/admin/submitPost',
    data: {
      inputSID: service_id,
      inputPID: post_id
    },
    type: 'POST',
    success: function (data) {
      $('#this_result').html('<label class="alert alert-success">Xác nhận thành công</label>')
    }
  })
})
$('#cancel').click(function (e) {
  e.preventDefault()
  var post_id = $('#post_id').val()
  var service_id = $('#pid').val()
  $.ajax({
    url: 'https://laberp.pythonanywhere.com/admin/cancelPost',
    data: {
      inputSID: service_id,
      inputPID: post_id
    },
    type: 'POST',
    success: function (data) {
      $('#this_result').html('<label class="alert alert-danger">Hủy thành công</label>')
    }
  })
})
