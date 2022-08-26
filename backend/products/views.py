from rest_framework import generics,mixins , permissions,authentication
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import get_object_or_404
# from braces.views import CsrfExemptMixin

from .models import Product
from .serializers import ProductSerializer
from .permissions import  IsStaffEditorPermission
from api.authentication import TokenAuthentication






class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()                        # if request is get excute this part
    serializer_class = ProductSerializer
    authentication_classes = [
                                authentication.SessionAuthentication,
                                TokenAuthentication
                             ]
    permission_classes = [permissions.IsAdminUser,IsStaffEditorPermission]
    # permission_classes = [permissions.DjangoModelPermissions]
    # permission_classes = [permissions.IsAuthenticated]

    # if request is post excute this part
    def perform_create(self, serializer): # optional if need any modification before save data
        # serializer.save(user=self.request.user)
        # print(serializer.validated_data)
        serializer.save()

product_list_create_view = ProductListCreateAPIView.as_view()



class ProdctDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #lookup_field = 'pk

product_detail_view = ProdctDetailAPIView.as_view()



class ProdctUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer): # optional if need any modification before
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
                content = title
        instance = serializer.save(content=content)
        
product_update_view = ProdctUpdateAPIView.as_view()


class ProdctDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    # def perform_destroy(self, instance): # optional if need any modification before
    #     super().perform_destroy(instance)
        
product_delete_view = ProdctDestroyAPIView.as_view()



class ProductMixingView(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        generics.GenericAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):      # to save data because CreateModelMixin
        return self.create(request, *args, **kwargs)  

    def perform_create(self, serializer):          #optional if need any modification before save data
        # serializer.save(user=self.request.user)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = "this is a single view doing cool stuff"
        serializer.save(content=content)


product_mixing_view = ProductMixingView.as_view()



# not used just for informtaion purposes only
@api_view(['GET','POST'])
def product_alt(request,pk=None,*args,**kwargs):
    print("pk==",pk)
    method = request.method
    if method == 'GET':
        if pk :
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj,many=False).data
            return Response(data)
            
            queryset = Product.objects.filter(pk=pk)
            if not queryset.exists():
                raise Http404
        
        queryset = Product.objects.all()
        data = ProductSerializer(queryset,many=True).data
        return Response(data)

    if method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None

            if content is None:
                content = title

            serializer.save(content=content)
            return Response(serializer.data)




class ProductCreateAPIView(generics.CreateAPIView):
    '''
        not gonna use this because we have listcreate api view
    '''
    # queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer): # optional if need any modification before save data
        # serializer.save(user=self.request.user)
        # print(serializer.validated_data)
        serializer.save()

product_craete_view = ProductCreateAPIView.as_view()


class ProdctListAPIView(generics.ListAPIView):
    '''
        not gonna use this because we have listcreate api view
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #lookup_field = 'pk

product_list_view = ProdctListAPIView.as_view()

