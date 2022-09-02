from django.shortcuts import render

# Create your views here.
def dinner(request, 저녁메뉴, 인원수 ):
    context = {'저녁메뉴': 저녁메뉴,
                '인원수' : 인원수

                }

    return render(request, 'pages/dinner.html', context)

