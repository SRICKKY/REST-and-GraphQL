from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect, ensure_csrf_cookie
from django.core import serializers

from pprint import pprint
import json

from .models import Link
# Create your views here.

def index(request):
	data = Link.objects.all().values('id','url','description')
	
	return JsonResponse(list(data),safe=False)

def detail(request, id):
	data = dict()
	
	# if request.method == 'GET':
	try:
		data = Link.objects.get(id=id)

		response = json.dumps([{'url': data.url, 'description': data.description}])
	except:
		response = json.dumps([{'Error': 'No information exist'}])

	return HttpResponse(response, content_type='text/json')

@csrf_exempt
def add_link(request):
	if request.method == 'POST':
		payload = json.loads(request.body)
		url = payload['url']
		description = payload['description']

		link = Link(url=url,description=description)

		try:
			link.save()
			response = json.dumps([{ 'Success': 'Links added successfully' }])
		except:
			response = json.dumps([{ 'Error': 'Links cannot be added!' }])

		return HttpResponse(response, content_type='text/json')

@csrf_exempt
def delete_link(request, id):
	if request.method == 'DELETE':
		
		try:
			Link.objects.filter(id=id).delete()
			response = json.dumps([{ 'Success': 'Links deleted successfully' }])
		except:
			response = json.dumps([{ 'Error': 'Links cannot be deleted!' }])

	return HttpResponse(response, content_type='text/json')