from django.shortcuts import render
from .blockchain import newNode
from . import forms
import time
from django.http import HttpResponse
from django.contrib.auth.models import user   #user info
# Entry.objects.order_by('-headline')[0]

# Create your views here.
# @login_required(login_url="/accounts/login/")
def dashboard(request):
    curr_user = request.user
    transactions = blockDB.objects.all() 
    
    
    return render(request,'dashboard.html',{'curr_user':curr_user})
    


def error(errorName):
    return HttpResponse(errorName)
    #return render(null,'crypto/error.html',{'error':errorName})
    

# -------------------------------------------------------------updating Data Function----------------------------------------------
def updateBalance():
    


# ----------------------------------------------------------updating Data Function ends--------------------------------------------



def sell_block(request):
    
    if request.method=='POST':
        
        # getting last row data from transactions table
        
        form=forms.SellBlock(request.POST)
        
        if form.is_valid():
            
            instance = form.save()
            
            # storing form data in a list
            mlist = [str(instance.data), str(instance.amount), str(instance.senderKey), str(instance.receiverKey)]
            
            print("mlist = ", mlist)
            
            ret = list(newNode(mlist))  # ret[0] = true /false  ret[1] = error string
            print(ret)
            if (ret[0]):
                return HttpResponse('DB saved')
                # update Balance
            else:
                # errorFunc(error parameter)
                # handle error case with errorFunc
                error(ret[1])
            
            
            

    else:
        form = forms.SellBlock()
    return render(request,'crypto/sell_block.html',{'form':form})
    
    
    

# --------------------------------------------users data---------------------------------------------------------------
