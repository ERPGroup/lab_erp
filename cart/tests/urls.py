from django.conf.urls import url, patterns


urlpatterns = patterns('cart.tests.views',
    url(r'^show/$', 'show', name='cart-tests-show'),
    url(r'^add/$', 'add', name='cart-tests-add'),
    url(r'^remove/$', 'remove', name='cart-tests-remove'),
    url(r'^remove-single/$', 'remove_single', name='cart-tests-remove-single'),
    url(r'^clear/$', 'clear', name='cart-tests-clear'),
    url(r'^set-quantity/$', 'set_quantity', name='cart-tests-set-quantity'),
)
