/*------------------------------------------------------
    Author : www.webthemez.com
    License: Commons Attribution 3.0
    http://creativecommons.org/licenses/by/3.0/
---------------------------------------------------------  */

;(function ($) {
  'use strict'
  var mainApp = {
    initFunction: function () {
      /*MENU 
      ------------------------------------*/
      $('#main-menu').metisMenu()

      $(window).bind('load resize', function () {
        if ($(this).width() < 768) {
          $('div.sidebar-collapse').addClass('collapse')
        } else {
          $('div.sidebar-collapse').removeClass('collapse')
        }
      })
    },
    initialization: function () {
      mainApp.initFunction()
    }

  }
  // Initializing ///

  $(document).ready(function () {
    mainApp.initFunction()
  })
}(jQuery))

function checkPassword () {
  var password = document.getElementById('inputPassword')
  var repassword = document.getElementById('inputRePassword')
  var checkPassword = document.getElementById('checkPassword')
  if (password.value != repassword.value) {
    checkPassword.classList.add('has-error')
  }else {
    checkPassword.classList.remove('has-error')
  }
}
function checkEmail () {
  var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
  var email = document.getElementById('email')
  var result = document.getElementById('re_email')
  if (re.test(String(email.value).toLowerCase())) {
    result.classList.remove('has-error')
  }else {
    result.classList.add('has-error')
  }
}
function checkPhone () {
  var ph = /^((\\+[1-9]{1,4}[ \\-]*)|(\\([0-9]{2,3}\\)[ \\-]*)|([0-9]{2,4})[ \\-]*)*?[0-9]{3,4}?[ \\-]*[0-9]{3,4}?$/
  var phone = document.getElementById('phone')
  var result = document.getElementById('re_phone')
  if (ph.test(String(phone.value))) {
    result.classList.remove('has-error')
  }else {
    result.classList.add('has-error')
  }
}
function checkNumber (a) {
  var pattern = /^\d+$/
  var number = document.getElementById(a)
  var result = document.getElementById('re_' + a)
  if (pattern.test(String(number.value))) {
    result.classList.remove('has-error')
  }else {
    result.classList.add('has-error')
  }
}
function guid () {
  function s4 () {
    return Math.floor((1 + Math.random()) * 0x10000)
      .toString(16)
      .substring(1)
  }
  return s4() + s4() + '-' + s4() + '-' + s4() + '-' + s4() + '-' + s4() + s4() + s4()
}
function addmore_tags (a) {
  var x = document.getElementById('tags_add')
  var attribute = ''
  var uuid = guid();
  attribute += ' <li id="' + uuid + '"><span class="value_tags">' + a + '<a href="#"><i onclick="$(\'#'+uuid+'\').remove(); return false;" class="fa fa-remove"></i></a></span></li>'
  x.innerHTML += attribute
}

