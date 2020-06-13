from django.shortcuts import render
import random
from datetime import datetime
import requests
# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def hello(request):
    menu = ['닭갈비', '탕수육', '초밥', '스파게티돈가스']
    pick = random.choice(menu)
    return render(request, 'pages/hello.html', {'pick':pick})

def name(request):
    my_name = '김성현'
    return render(request, 'pages/name.html', {'my_name':my_name})

def introduce(request):
    my_info = ['김성현', '28', '서울 관악구', 'https://github.com/kim-svadoz']
    name = my_info[0]
    age = my_info[1]
    home = my_info[2]
    git = my_info[3]
    context = {
        'name' : name,
        'age' : age,
        'home' : home,
        'git' : git
    }
    return render(request, 'pages/introduce.html', context)

def classRandomChoice(request):
    arr = ['백승재', '심재민', '유환우', '강인선', '신승환']
    pick = random.choice(arr)
    context = {
        'pick' : pick
    }
    return render(request, 'pages/classRandomChoice.html', context)

def yourname(request, name):
    name = name
    context={
        'name' : name
    }
    return render(request, 'pages/yourname.html', context)

def urlcopy(request, name, age):
    name = name
    age = age
    context={
        'name' : name,
        'age' : age
    }
    return render(request, 'pages/urlcopy.html', context)

def multiply(request, num1, num2):
    num1 = num1
    num2 = num2
    result = num1 * num2
    context = {
        'num1' : num1,
        'num2' : num2,
        'result' : result
    }
    return render(request, 'pages/multiply.html', context)

def multipletable(request, big, small):
    result = []
    if(big < small):
        big, small = small, big
    for num in range(1, small+1):
        result.append(big*num)
    context={
        'result' : result
    }
    return render(request, 'pages/multipletable.html', context)

def dtl(request):
    mList = ['짜장면', '차돌짬뽕', '탕수육', '콩국수']
    empty_list = []
    mString = "Life is short, You need Python"
    today = datetime.now()
    context = {
        'mList' : mList,
        'empty_list' : empty_list,
        'mString' : mString,
        'today' : today
    }
    return render(request, 'pages/dtl.html', context)

# 1. 간단한 반복문으로 리스트 각 요소를 출력
# 2. if, else 활용해서 문자열 비교
# 2-1. 내가 넘긴 문자열과 특정한 문자열 비교
# 3. if, elif, else 사용해보기
# 3-1. 문자열의 길이가 5 이하이면 short
# 3-2. 문자열의 길이가 10 이상이면 long
# 3-3. 모두 아니면 적당 출력

# 모두 작성했다면,
## 1) 반복문으로 리스트 각 요소를 출력해서
## 2) 해당 요소가 90 이상이면 A
## 3) 해당 요소가 70 이상이면 B
## 4) 그 외엔 C 출력
def forif(request):
    mList = [100, 50, 80, 71, 10]
    mString = '간단한 문자열zzzzzzzzzzzz'
    mInput = input("문자열을 입력하세요: ")
    data_a = '첫번째 데이터'
    data_b = '두번째 데이터'
    data_a, data_b = data_b, data_a
    context = {
        'mList' : mList,
        'mString' : mInput,
        'data_a' : data_a,
        'data_b' : data_b
    }
    return render(request, 'pages/forif.html', context)

def loop(request):
    nums = []
    for data in range(10):
        nums.append(data)
    context = {
        'nums': nums
    }
    return render(request, 'pages/loop.html', context)

def throw(request):
    return render(request, 'pages/throw.html')

def catch(request):
    # request parameter는 요청 정보가 담겨있다.
    # request.GET == 딕셔너리와 유사하다.
    # request.GET != dict()
    # data = request.GET['message']
    name = request.GET.get('name')
    age = request.GET.get('age')
    context ={ 
        'name' : name,
        'age' : age
    }
    return render(request, 'pages/catch.html', context)

# 1. 사용자가 숫자 입력
# 2. 입력 받은 횟수 만큼 반복해서
# 3. 리스트에 로또 번호 담는다.
# 3-1. random.sample(range(1, 46), 6)
# 4. 사용자가 입력한 숫자와 로또번호가 담긴 리스트를 출력
# 5. ul태그를 사용하여 각 번호들을 한줄 씩 출력
def lottoT(request):
    return render(request, 'pages/lottoT.html')

def lottoC(request):
    num = int(request.GET.get('num'))
    lottos = []
    for data in range(num):
        lottos.append(random.sample(range(1, 46), 6))
    context={
        'num' : num,
        'lottos' : lottos,
    }

    return render(request, 'pages/lottoC.html', context)

def artii(request):
    return render(request, 'pages/artii.html')

def result(request):
    msg = request.GET.get('msg')
    result = requests.get(f'http://artii.herokuapp.com/make?text={msg}').text
    context = {
        'result' : result
    }
    return render(request, 'pages/result.html', context)