from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
        'january': 'Hello January',
        'february': 'Hello February',
        'march': 'Hello March',
        'april': 'Hello April',
        'may': 'Hello May',
        'june': 'Hello June',
        'july': 'Hello July',
        'august': 'Hello August',
        'september': 'Hello September',
        'october': 'Hello October',
        'november': 'Hello November',
        'december': None
        }

def index(request):
    return render(request, 'challenges/index.html', {'months': list(monthly_challenges.keys())})

def index_old(request):
    li = [f"<li><a href='{reverse("month-challenge", args=[month])}'>{month.capitalize()}</a></li>" 
          for month in list(monthly_challenges.keys())]

    return HttpResponse('<ul>\n\t' + '\n\t'.join(li) + '\n</ul>')

def february(request):
    return HttpResponse("Hello February!")

def monthly_challenge(request, month):
    try:
        #  challenge_text = monthly_challenges[month]
        return render(request, 'challenges/challenge.html', {'month': month, 'message': monthly_challenges[month]})
    except:
        return HttpResponseNotFound('Month not supported yet')

def monthly_challenge_old(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(f'<h1>{challenge_text}</h1>')
    except:
        return HttpResponseNotFound('Month not supported')

#  Month by number
def monthly_challenge_by_number(request, month):
    # Starting from 1.
    month = month - 1
    if month > 12 or month < 1:
        return HttpResponseNotFound('Month not supported')
    try:
        str_month = list(monthly_challenges.keys())[month]
        return HttpResponseRedirect(reverse('month-challenge', args=[str_month]))
        #  return HttpResponseRedirect('/challenges/' + str_month)
    except:
        return HttpResponseNotFound('Month not supported')
