from django.shortcuts import render
import random

# Create your views here.

def index(request):
  return render(request, 'articles/index.html')

def greeting(request):
  foods = ['apple', 'banana']
  info = {
    'name': '희원',
  }
  context = {
    'foods': foods,
    'info': info,
  }
  return render(request, 'articles/greeting.html', context)


def dinner(request):
  foods = ['족발', '피자', '김밥']
  pick = random.choice(foods)
  context={
    'foods': foods,
    'pick': pick,
  }
  return render(request, 'articles/dinner.html', context)

def throw(request):
  return render(request, 'articles/throw.html')

def catch(request):
  message = request.GET.get('message')
  context = {
    'message': message,
  }
  return render(request, 'articles/catch.html', context)
