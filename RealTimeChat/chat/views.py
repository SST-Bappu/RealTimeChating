from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from .form import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model,login,logout,get_user
from django.contrib.auth.decorators import login_required
from .decorator import*
from .models import*
# Create your views here.
@login_required(login_url='login')
def home(request):
    user = request.user
    context={'username':user}
    return render(request,'index.html',context)

def registerUser(request):
    form = CreateUserForm()
    context ={'form':form}
    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            '''group = Group.objects.get(name='customer')
            user.groups.add(group)
            Customer.objects.create(
                user = user,
            )'''
            messages.success(request,'User Account has been created for ' + username)
            return redirect('registration')
        else:
            pass1 = form.cleaned_data.get('password1')
            pass2 = form.cleaned_data.get('password2')
            if pass1 != pass2:
                messages.error(request,"Password didn't match")
            else:
                messages.error(request,"Fill all the required fields correctly")
            return redirect('registration')
    return render(request,'registration.html',context)

@unauthenticated_user
def Userlogin(request):
    context={}
    print("Got here")
    if request.POST:
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,"Username or Password is incorrect!")
    return render(request,'login.html',context)

@login_required(login_url='login')
def generateRoom(request):
    user = request.user
    send_to = request.POST['username']
    User = get_user_model()
    users = User.objects.all()
    users = [u.username for u in users]
    if not (send_to in users):
        messages.error(request,"This user is not available")
        return redirect('home')
    match1 = user.username.lower()+send_to.lower()
    match2 = send_to.lower()+user.username.lower()
    conv = None
    if room.objects.filter(name=match1).exists() or room.objects.filter(name=match2).exists():
        
        if room.objects.filter(name=match1).exists():
            conv = room.objects.get(name=match1)
        else:
            conv = room.objects.get(name=match2)
    else:
        conv = room.objects.create(name=match1)
        conv.save()
    return render(request,'chat.html',
    {
        'username':user,
        'room': conv.id,
        'room_details':conv,
    })



@login_required(login_url='login')
def send(request):
    msg = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']
    new_message = message.objects.create(value=msg,room=room_id,user= username)
    new_message.save()
    return HttpResponse('Message sent successfully!')
@login_required(login_url='login')
def getMessage(request,room_id):
    messages = message.objects.filter(room=room_id)
    return JsonResponse({'messages':list(messages.values())})

