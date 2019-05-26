from django.shortcuts import render

def recassgin_login_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.groups.filter(name='RecAssign').exists:
            print('YES')
            return function(request, *args, **kwargs)
            # return render(request,'RDApp/MonitorBase.html',{})
        else:
            print(request.user)
            print('NO')
            return render(request,'RDApp/index.html',{})
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
