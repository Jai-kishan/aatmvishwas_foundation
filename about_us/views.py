from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from about_us.models import AboutUs
from about_us.serializers import AboutUsSerializers

# Create your views here.
@csrf_exempt
def about_us_list(request):
    """
    List all code Apps, or create a new snippet.
    """
    if request.method == 'GET':
        about_us = AboutUs.objects.all()
        serializer = AboutUsSerializers(about_us, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AboutUsSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
def about_us_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        about_us = AboutUs.objects.get(pk=pk)
    except AboutUs.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AboutUsSerializers(about_us)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AboutUsSerializers(about_us, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        about_us.delete()
        return HttpResponse(status=204)
