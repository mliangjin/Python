from django.http import HttpResponseRedirect

def user_verify_login(fun):
    def login_fun(request, *args, **kargs):
        if request.session.has_key('user_id'):
            return fun(request, *args, **kargs)
        else:
            return HttpResponseRedirect('/user/login/')
    return login_fun