from django.shortcuts import redirect

def auth_middleware(get_response):
    
    def middleware(request):
        print(request.session.get('Customer'))
        if not request.session.get('Customer'):
         return redirect('Login')
        response = get_response(request)

        return response

    return middleware