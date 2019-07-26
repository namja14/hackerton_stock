
from django.http import HttpResponse
from django.template import loader
from .models import Apply
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):# about 함수
    return render(request,'about.html')

def services(request):#검색한 정보 함수
    apply = Apply.objects
    return render(request,'services.html',{'apply': apply})

def contact(request):# 콘택트 함수
    return render(request,'contact.html')

def register(request):# 등록창 함수
    return render(request,'register.html')

def detail(request,apply_id):# 세부정보 함수
    apply_detail = get_object_or_404(Apply,pk=apply_id)
    return render(request,'detail.html',{'apply':apply_detail})

def create(request):#등록할때 쓰는 함수 
    apply = Apply()
    apply.title = request.GET['title']
    apply.body = request.GET['body']
    apply.pub_date = timezone.datetime.now()    
    apply.save()
    return redirect('/services/' + str(apply.id))
