from django.shortcuts import render
from basic_app.forms import ChatBotAdminForm as UserForm 
from basic_app.models import QandAModel
# Create your views here.


from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required



def index(request):
    if request.method=="POST":
        CountQuestion = request.POST["count"]
        QandA=""
        QandAModel.objects.all().delete()
        for i in range(int(CountQuestion)):
            try:
                
                A = request.POST.getlist('answer'+str(i+1))
                for j in A:
                   if j!="": 
                    QandA=QandA+j+";"    
                print(QandA)
                user=QandAModel.objects.get_or_create(Questions=request.POST["question"+str(i+1)],Answers=QandA)    
                QandA=""
                pass
            except:
                pass
        return render(request,'basic_app/success.html')    
          
    
   
    return render(request,'basic_app/index.html')
def register(request):
    logout(request)
    registered=False
    
    if request.method=="POST":
        
        user_form=UserForm(data=request.POST)
        
        if user_form.is_valid() :
            print("NAME: "+ user_form.cleaned_data['username'])
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            
            registered=True
        else:
                print(user_form.errors)
    else:
         user_form=UserForm ()

    return render (request,'basic_app/registration.html',
                   {'user_form':user_form,
                    'registered':registered})          

 
    
@login_required   
def special(request):
     return HttpResponse("your are logged in")     
    
@login_required   
def user_logout(request):
     logout(request)
     return HttpResponseRedirect(reverse('index'))    
   
def user_login(request):
    
       logout(request)    
       if request.method=="POST":
           username=request.POST.get('username')
           password=request.POST.get('password')
           
           user=authenticate(username=username,password=password)
          
           
           
           if user:
               
               if user.is_active:
                   login(request,user)
                   return HttpResponseRedirect(reverse('index'))
               else :
                   return HttpResponse("ACCOUNT NOT ACTIVE")
           else:
               print("someone tried to login and failed")
               print(f'username: {username} and password: {password} ')
               return HttpResponse("invalid login details supplied!!")
       else:
            return render(request,'basic_app/login.html')
               