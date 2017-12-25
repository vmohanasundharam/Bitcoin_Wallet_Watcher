# -*- coding: utf-8 -*-
from random import randint
import smtplib
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from . import bitcoin


@csrf_exempt
def bit_coin(request):
	if request.method == "POST" :
		address = request.POST.get('w_addrs')
		obj = bitcoin.get_object(address)
		if obj.flag == True:
			balance = obj.wallet_balance()
			r_list = obj.transfers_to_wallet()
			s_list = obj.transfers_from_wallet()
			balance = obj.wallet_balance()
			return render(request, 'bitcoin/template.html', {'s_nodes':s_list,'r_nodes':r_list,'bal':balance,'h_address':'002d28cac852fc7d'})
		else:
			return render(request,'bitcoin/pages-blank.html',{'flag':True})

	if request.method == "GET" :
		return render(request,'bitcoin/pages-blank.html',{})


        