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

//Quảng cáo 

(function ($) {
  'user strict'
  $.fn.Dqdt_CountDown = function (options) {
    return this.each(function () {
      // get instance of the dqdt.
      new $.Dqdt_CountDown(this, options)
    })
  }
  function success(a) {
    var inputID = "";
    if (a.length > 3) {
      if (a.slice(0, 4) == "none") {
        load();
      }
      if (a.slice(0, 5) == "start") {
        inputID = a.substr(6, 10);
        $.ajax({
          url: 'http://localhost:8000/admin/enable_ads',
          data: {
            inputID: inputID
          },
          type: 'POST',
          success: function (data) {
            load();
          }
        })
      }
    } else {
      inputID = a;
      $.ajax({
        url: 'http://localhost:8000/admin/disable_ads',
        data: {
          inputID: inputID
        },
        type: 'POST',
        success: function (data) {
          load();
        }
      })
    }
  }

  var object
  $.Dqdt_CountDown = function (obj, options) {
    this.options = $.extend({
      autoStart: true,
      LeadingZero: true,
      DisplayFormat: '<div><span>%%D%%</span> Days</div><div><span>%%H%%</span> Hours</div><div><span>%%M%%</span> Mins</div><div><span>%%S%%</span> Secs</div>',
      FinishMessage: 'Hết hạn',
      CountActive: true,
      TargetDate: null
    }, options || {})
    if (this.options.TargetDate == null || this.options.TargetDate == '') {
      return
    }
    this.timer = null
    this.element = obj
    object = obj
    this.CountStepper = -1
    this.CountStepper = Math.ceil(this.CountStepper)
    this.SetTimeOutPeriod = (Math.abs(this.CountStepper) - 1) * 1000 + 990
    var dthen = new Date(this.options.TargetDate)
    var dnow = new Date()
    if (this.CountStepper > 0) {
      ddiff = new Date(dnow - dthen)
    } else {
      ddiff = new Date(dthen - dnow)
    }
    gsecs = Math.floor(ddiff.valueOf() / 1000)
    this.CountBack(gsecs, this)
  }
  $.Dqdt_CountDown.fn = $.Dqdt_CountDown.prototype
  $.Dqdt_CountDown.fn.extend = $.Dqdt_CountDown.extend = $.extend
  $.Dqdt_CountDown.fn.extend({
    calculateDate: function (secs, num1, num2) {
      var s = ((Math.floor(secs / num1)) % num2).toString()
      if (this.options.LeadingZero && s.length < 2) {
        s = '0' + s
      }
      return '<b>' + s + '</b>'
    },
    CountBack: function (secs, self) {
      if (secs < 0) {
        success(object.id)
        return
      }
      clearInterval(self.timer)
      DisplayStr = self.options.DisplayFormat.replace(/%%D%%/g, self.calculateDate(secs, 86400, 100000))
      DisplayStr = DisplayStr.replace(/%%H%%/g, self.calculateDate(secs, 3600, 24))
      DisplayStr = DisplayStr.replace(/%%M%%/g, self.calculateDate(secs, 60, 60))
      DisplayStr = DisplayStr.replace(/%%S%%/g, self.calculateDate(secs, 1, 60))
      self.element.innerHTML = DisplayStr
      if (self.options.CountActive) {
        self.timer = null
        self.timer = setTimeout(function () {
          self.CountBack((secs + self.CountStepper), self)
        }, (self.SetTimeOutPeriod))
      }
    }

  })

  function checkTime(a) {
    $('[data-countdown="' + a + '"]').each(function (index, el) {
      var $this = $(this)
      var $date = $this.data('date').split('-')
      $this.Dqdt_CountDown({
        TargetDate: $date[0] + '/' + $date[1] + '/' + $date[2] + ' ' + $date[3] + ':' + $date[4] + ':' +
          $date[5],
        DisplayFormat: '<div class="block-timer"><p>%%D%%</p><span>Ngày</span></div><div class="doted-timer hidden"><li></li><li></li></div><div class="block-timer"><p>%%H%%</p><span>Giờ</span></div><div class="doted-timer hidden"><li></li><li></li></div><div class="block-timer"><p>%%M%%</p><span>Phút</span></div><div class="doted-timer hidden"><li></li><li></li></div><div class="block-timer"><p>%%S%%</p><span>Giây</span></div>',
        FinishMessage: 'Hết hạn'
      })
    })
  }
  function load() {
    $('#result').html('')
    $.ajax({
      url: 'http://localhost:8000/admin/getAllAdsActiving',
      type: 'GET',
      async: false,
      success: function (data) {
        $.each(data, function (i, item) {
          html = '';
          html += '<div style="display:none;" id="' + item['id'] +
            '"  class="timer-view" data-countdown="countdown" data-date="' + item['end'] + '"></div>';
          $('#result').append(html)
        })
      }
    })
    checkTime('countdown')
  }
  $(document).ready(function () {
    load();
  });
})(jQuery)


function pageRedirect(url) {
  window.location.replace(url);
}
