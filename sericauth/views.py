from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User

# Create your views here.

def user_home(request):
    if 'uname' in request.session:
        data = {'name':request.session.get('uname')}

        if 'book_status' in request.session:
            data['status'] = request.session['book_status']

        return render(request,'user_home.html',context=data)
    else:
        data = {'status':'You need to login first'}
        return render(request,'registration.html',context=data)

#BACKEND -> For User Registration
def test(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        re_password = request.POST.get('repassword')

        if(password == re_password):
            user = User(name=name,email=email,mobile=mobile, gender=gender,password=password)
            user.save()
            request.session['uname'] = name
            return user_home(request)
        else:
            data = {'status':"Password and Re-entered password must be same"}
            return render(request,'registration.html',context=data)
    else:
        return render(request, 'registration.html')
        #return HttpResponse("Something went wrong!!!!!")

#BACKEND -> For User Login
def login_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        try:
            user = User.objects.get(name=name)
            print(user.name)

        except Exception as e:
            data = {'status': "User does not exists! You have to register first."}
            return render(request, 'registration.html', context=data)

        user = User.objects.get(name=name)

        if user.password == password:
            request.session['uname'] = name
            print("kkkkkk")
            return redirect("sericauth:user_home")
        else:
            data = {'status':"Incorrect Password!!!"}
            #return render(request,'registration.html',context=data)
            print("kkkkkk")
            return HttpResponse("login success")

        # except Exception as e:
        #     data = {'status':"User does not exists! You have to register first."}
        #     return render(request,'registration.html',context=data)
    else:
        return HttpResponse("Something went wrong!!!!!")

