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
/* Plugin Datatables */
  /* Create an array with the values of all the input boxes in a column */
  $.fn.dataTable.ext.order['dom-text'] = function (settings, col) {
    return this.api().column(col, { order: 'index' }).nodes().map(function (td, i) {
        return $('input', td).val();
    });
}

/* Create an array with the values of all the input boxes in a column, parsed as numbers */
$.fn.dataTable.ext.order['dom-text-numeric'] = function (settings, col) {
    return this.api().column(col, { order: 'index' }).nodes().map(function (td, i) {
        return $('input', td).val() * 1;
    });
}

/* Create an array with the values of all the select options in a column */
$.fn.dataTable.ext.order['dom-select'] = function (settings, col) {
    return this.api().column(col, { order: 'index' }).nodes().map(function (td, i) {
        return $('select', td).val();
    });
}

/* Create an array with the values of all the checkboxes in a column */
$.fn.dataTable.ext.order['dom-checkbox'] = function (settings, col) {
    return this.api().column(col, { order: 'index' }).nodes().map(function (td, i) {
        return $('input', td).prop('checked') ? '1' : '0';
    });
}
/* End */
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
function checkEmail() {
    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    var email = document.getElementById('email');
    var result = document.getElementById('re_email');
    if(re.test(String(email.value).toLowerCase()))
    {
        result.classList.remove('has-error');
    }
    else{
        result.classList.add('has-error');
    }
}
function checkPhone(){
    var ph = /^((\\+[1-9]{1,4}[ \\-]*)|(\\([0-9]{2,3}\\)[ \\-]*)|([0-9]{2,4})[ \\-]*)*?[0-9]{3,4}?[ \\-]*[0-9]{3,4}?$/;
    var phone = document.getElementById('phone');
    var result = document.getElementById('re_phone');
    if(ph.test(String(phone.value)))
    {
        result.classList.remove('has-error');
    }
    else{
        result.classList.add('has-error');
    }
}