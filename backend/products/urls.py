from django.urls import path
from . import views



    
urlpatterns = [
   path('',views.product_list_create_view),
   path('<int:pk>',views.product_detail_view,name='product-detail'),
   path('update/<int:pk>',views.product_update_view),
   path('delete/<int:pk>',views.product_delete_view),


   path('mixing/',views.product_mixing_view),
   path('mixing/<int:pk>',views.product_mixing_view),

   
]
   