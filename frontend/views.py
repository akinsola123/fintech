from django.shortcuts import redirect, render
from articles.models import Blog
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required

import json

# Create your views here.

def home (request):
    """
    Welcome page for our fintech application
    """
    all_posts = Blog.objects.all()
    context = {
        'all_posts':all_posts,
    }
    return render(request, 'pages/index.html', context)


# @login_required()
# def payment (request):
#     """
#     Welcome page for our fintech application
#     """
#     return render(request, 'pages/welcome.html')



class PaymentsView (View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pages/welcome.html')
        

    def post(self, *args, **kwargs):
        data = json.loads(self.request.body)
        status = data['status']
        transref = data['transref']
        amount = data['amount']
        currency = data['currency']


        print('my-status', status)
        print('my-transref', transref)
        print('my-amount', amount)
        print('my-currency', currency)


        return redirect('success')

def success(request):

    return render(request, 'pages/success.html')
