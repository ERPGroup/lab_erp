$(document).ready(function () {
  $('#click_drop_menu').click(function (e) {
    e.stopPropagation()
    $('#sub-menu').toggleClass('show-menu')
  })
  $('#click_drop_menu_fixed').click(function (e) {
    e.stopPropagation()
    $('#sub-menu').toggleClass('show-menu')
  })
  $('#sub-menu').click(function (e) {
    e.stopPropagation()
  })
  $('body,html').click(function (e) {
    $('#sub-menu').removeClass('show-menu')
  })
  $('#click_exit_menu').click(function () {
    $('#sub-menu').removeClass('show-menu')
  })
  $('#close_x').click(function () {
    var popup = document.getElementById('popup_quickview')
    popup.style.display = 'none'
    $('#over').remove()
  })
})
window.onscroll = function () {scrollFunction();fixMenuMobile();}

function scrollFunction () {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    document.getElementById('btnTop').style.display = 'block'
  } else {
    document.getElementById('btnTop').style.display = 'none'
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction () {
  document.body.scrollTop = 0 // For Safari
  $('body,html').animate({
    scrollTop: 0
  }, 800)
}

// Get the header
var header = document.getElementById('fixed_menu_top')

// Get the offset position of the navbar
var sticky = header.offsetTop

// Add the sticky class to the header when you reach its scroll position. Remove "sticky" when you leave the scroll position
function fixMenuMobile () {
  if (window.pageYOffset > 200) {
    header.classList.add('sticky')
  } else {
    header.classList.remove('sticky')
  }
}
function clickShowSearch(a){
  var x = document.getElementById(a)
  if (x.style.display == 'block') {
    x.style.display = 'none';
  }else {
    x.style.display = 'block'
  }
  $('html,body').animate({
    scrollTop: $("#goto_move").offset().top},
    'slow');
}
function clickShowCategory(a)
{
  var x = document.getElementById(a);
  $('#'+a).slideToggle();
    x.style.position = 'absolute';
    x.style.left ='0';
    x.style.right ='0';
    x.style.zIndex ='9999';
    x.style.background = 'white';
}
function clickShowFooter (a) {
  $('#'+a).slideToggle();
}

function forgot_password (){
  var c = document.getElementById('forgot_password')
  c.style.display = 'block';
  var x = document.getElementById('fr_login')
  x.style.display = 'none';
}
function show_login(){
  var c = document.getElementById('forgot_password')
  c.style.display = 'none';
  var x = document.getElementById('fr_login')
  x.style.display = 'block';
}
// function quick_view () {
//   var popup = document.getElementById('popup_quickview')
//   popup.style.display = 'block'
//   $('body').append('<div id="over">')
//   $('#over').fadeIn(300)
// }
function checkPassword () {
  var password = document.getElementById('inputPassword')
	var repassword = document.getElementById('inputRePassword')
	var checkPassword = document.getElementById('checkPassword')
	var error = document.getElementById('errors_rpw')
  if (password.value != repassword.value) {
		checkPassword.classList.add('has-error');
		error.innerHTML='Mật khẩu không khớp.';
  }else {
		checkPassword.classList.remove('has-error')
		error.innerHTML ='';
  }
}


function isEmail(emailStr) 
{
  var emailPat=/^(.+)@(.+)$/
  var specialChars="\\(\\)<>@,;:\\\\\\\"\\.\\[\\]"
  var validChars="\[^\\s" + specialChars + "\]"
  var quotedUser="(\"[^\"]*\")"
  var ipDomainPat=/^\[(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})\]$/
  var atom=validChars + '+'
  var word="(" + atom + "|" + quotedUser + ")"
  var userPat=new RegExp("^" + word + "(\\." + word + ")*$")
  var domainPat=new RegExp("^" + atom + "(\\." + atom +")*$")
  var matchArray=emailStr.match(emailPat)
  if (matchArray==null) {
          return false
  }
  var user=matchArray[1]
  var domain=matchArray[2]

  // See if "user" is valid
  if (user.match(userPat)==null) {
      return false
  }
  var IPArray=domain.match(ipDomainPat)
  if (IPArray!=null) {
      // this is an IP address
            for (var i=1;i<=4;i++) {
              if (IPArray[i]>255) {
                  return false
              }
      }
      return true
  }
  var domainArray=domain.match(domainPat)
  if (domainArray==null) {
      return false
  }

  var atomPat=new RegExp(atom,"g")
  var domArr=domain.match(atomPat)
  var len=domArr.length

  if (domArr[domArr.length-1].length<2 ||
      domArr[domArr.length-1].length>3) {
      return false
  }

  // Make sure there's a host name preceding the domain.
  if (len<2) 
  {
      return false
  }

  // If we've gotten this far, everything's valid!
  return true;
}