from django.shortcuts import render
from django.http import HttpResponse
from .forms import contrac_form
from django.views import View
class contrac(View):      
   def get(self, request):
      cf = contrac_form 
      return render(request, 'contract/contract.html',{'cf':cf})

   def post(self,request):
      if request.method == 'POST':
         cf = contrac_form(request.POST)
         if cf.is_valid():
            saveCF = contrac_form (user = cf.cleaned_data['user'], 
                                             email = cf.cleaned_data['email'],
                                             body = cf.cleaned_data['body'])
            saveCF.save()
            return HttpResponse("save successfull")
      else:
         return HttpResponse('not POST')