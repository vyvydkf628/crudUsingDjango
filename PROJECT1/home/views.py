from django.shortcuts import render, HttpResponse
import random
import requests
# Create your views here.


# Views > urls > templates

def index(request):
    return render(request,'home/index.html')

def hola(request):
    return render(request,'home/hola.html')

def midnight(request):
    menus= ['pizza','pasta','soodae','asdf']
    dinner = random.choice(menus)
    #DTL grammar
    return render(request,'home/midnight.html',{'menus':menus,'dinner':dinner})

def lottos(request):
    numbers = range(1,46)
    lottos = random.sample(numbers,6)
    real_lottos = [5,10,25,32,33,37]
    return render(request,'home/lottos.html',{'lottos':lottos,'real_lottos':real_lottos})


def hello(request,name):
    return render(request,'home/hello.html',{'name':name})

def cube(request,num):
    nums = num**3
    return render(request,'home/cube.html', {'nums':nums,'num':num})

def introduce(request,name,age):
    return render(request,'home/introduce.html',{'name':name,'age':age})

def template_language(request):
    my_list = ['a','b','c','d']
    messages = ['apple','banana','cucumber','mango','watermelon']
    empty_list = []

    return render(request,'home/template_language.html',{'my_list':my_list,'messages':messages,'empty_list':empty_list})

def ping(request):
    return render(request,'home/ping.html')

def pong(request):
    data = request.GET.get('data')
    return render(request,'home/pong.html',{'data':data})

def catch(request):
    return render(request,'home/catch.html')

def result(request):
    word = request.GET.get('word')

    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text 
    fonts= fonts.split('\n')

    font = random.choice(fonts)

    result = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text

    return render(request,'home/result.html',{'result':result}) 

def throw(request):
    return render(request,'home/throw.html')

def get(request):
    name = request.GET.get('name')
    lottos = range(1,46)
    picked = random.sample(lottos,6)
    return render(request,'home/get.html',{'name':name,'picked':picked})

def user_new(request):
    return render(request,'home/user_new.html')

def user_create(request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    return render(request,'home/user_create.html',{'name':name,'pwd':pwd})

def static_example(request):
    return render(request,'home/static_example.html')