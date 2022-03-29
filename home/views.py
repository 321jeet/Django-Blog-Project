

from django import views
from django.http import HttpResponse
from django.shortcuts import redirect, render
from home.models import Contact
from blog.models import Post
from django.contrib import messages
from django.contrib.auth .models import User
from django.contrib.auth import authenticate,login,logout



# Create your views here.


def home(request):
    views =Post.objects.filter()
    context={
        'views' :views
        
    }
    return render(request, 'home/home.html',context)


def about(request):
    return render(request, 'home/about.html')


def contact(request):

    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        subject = request.POST.get('subject')

        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(subject) < 5:
            messages.error(request, "please fill the forms correctly")
        elif contact =="":
            messages.error(request, "please fill the forms")
        else:
            contact = Contact(name=name, phone=phone,email=email, subject=subject)
            contact.save()
            messages.success(request, "your  submited ")
    return render(request, 'home/contact.html')


def search(request):
    search = request.GET['search']
    if len(search) > 78:
        allPosts = []
    else:
        allPostsTitle = Post.objects.filter(title__icontains=search)
        allPostsContent = Post.objects.filter(content__icontains=search)
        allPosts = allPostsTitle.union(allPostsContent)
    if allPosts.count() == 0:
        messages.warning(request, " NO search result")
    context = {'allPosts': allPosts, 'search': search}

    return render(request, 'home/search.html', context)


# Authentications Api

def singup(request):

    if request.method =='POST':
        username=request.POST['username']
        fname= request.POST['fname']
        lname =  request.POST['lname']
        email= request.POST['email']
        pass1=  request.POST['pass1']
        pass2=  request.POST['pass2']


        # user created the user
        myuser= User.objects.create_user(username, email, pass1)
        myuser.frist_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"your account have been successfully created")
        return redirect('/')
    else:
      return HttpResponse("404 not Allowed")

def handellogin(request):   

    if request.method == 'POST':
        loginusername=request.POST['loginusername']
        loginpass= request.POST['logpass']

        user = authenticate(username=loginusername,password=loginpass)

        if user is not None:
            login(request,user)
            messages.success(request,"successfully logged in")
            return redirect('home')
        else:
            messages.error(request,"invailid User ,please try agian") 
            return redirect('home')

    return HttpResponse("404 -Not found")
    
def handellogout(request):   
   
    logout(request)
    messages.success(request,"now you logout")
    return redirect('home')   
