@login_required
@group_required
@Permission_required

@csrf_exempt
def user_login(request):
    error=''
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        return render_to_response('registration/login.html', {'error': error})
    else:
        render('/login.html', {'error': error})
