from django.shortcuts import redirect

def redirect_merchant_index(request):
    return redirect('/merchant/')
def redirect_admin_index(request):
    return redirect('/admin/')