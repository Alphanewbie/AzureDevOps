# djanggo import style guide
# 1. standard library
# 2. 3rd party library
# 3. django
# 4. local django

import random
from pprint import pprint
from datetime import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def dinner(request):
    foods = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(foods)

    # context는 딕셔너리 형태로 보내준다.
    context = {
        'pick': pick,
    }
    return render(request, 'dinner.html', context)
    # return render(request, template_name='dinner.html', context={'pick': pick})


def picsum(request):
    imgLink = 'https://picsum.photos/200/300.jpg'

    context = {
        'imgLink': imgLink
    }
    return render(request, 'picsum.html', context)

# 이 두번째 이름은 무조건 맞춰줘야한다.
def hello(request, name):

    context = {
        'name': name,
    }
    return render(request, 'hello.html', context)


def iam(request, name, age):

    context = {
        'name': name,
        'age': age,
    }
    return render(request, 'whoareyou.html', context)


def multi(request, num1, num2):
    result = num1 * num2

    context = {
        "num1": num1,
        "num2": num2,
        "result": result,
    }
    return render(request, 'multi.html', context)


def dtl_practice(request):
    foods = ['짜장면', '초밥', '차돌짬뽕', '콩국수']
    empty_list = []
    messages = 'Life is shorts, You need Python'
    datetime_now = datetime.now()

    context = {
        'foods': foods,
        'empty_list': empty_list,
        'messages': messages,
        'datetime_now': datetime_now,
    }
    return render(request, 'dtl_practice.html', context)


def palindrome(request, word):
    check = '맞습니다.' if word == word[::-1] else '아닙니다.'

    context = {
        'check': check,
        'word': word,
    }
    return render(request, 'palindrome.html', context)

def throw(request) :
    return render(request, 'throw.html')

def catch(request) :
    # HTTP method 중 GET 
    # form 에서 중요한 것
    # 1. 데이터를 어디로 보낼 것인지 =>
    # 2. 어떤 방식으로 보낼지 =>
    # 3. 어떤 데이터를 보낼지 => input, type
    # 4. 데이터의 이름은 어떻게 붙일지
    # 5. 제출 => submit

    # pprint(request.META)
    # print(request.GET)
    # print(request.GET.get('message'))
    message = request.GET.get('message')
    happy = request.GET.get('happy')
    context = {
        'message' : message,
        'happy' : happy,
    }
    
    return render(request, 'catch.html', context)