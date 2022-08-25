import json
from django.http import JsonResponse,HttpResponse
from django.forms.models import model_to_dict

from products.models import Product
from products.serializers import ProductSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET','POST'])
def api_home1(request,*args,**kwargs):
    return Response("test")



@api_view(['GET','POST'])
def api_home(request,*args,**kwargs):

    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        return Response(serializer.data)


    modelData = Product.objects.all().order_by('?').first()
        
    data = {}
    if modelData:
        # data = model_to_dict(modelData,fields=['id','title','price','content'])
        data = ProductSerializer(modelData).data
    return Response(data)
    return JsonResponse(data)
    return HttpResponse(data,headers={'Content-Type':'application/json'})


    print(request.GET) # url query params
    print(request.POST)
    body  = request.body
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)
