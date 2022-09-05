from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from tiffinapp.models.manus import add_new_manu
from tiffinapp.models.orderlist import Cart , OderItem
from rest_framework_simplejwt.authentication import JWTAuthentication
from tiffinapp.serializers import *




              
class CartView(APIView):
   authentication_classes = [JWTAuthentication]
   permission_classes = [IsAuthenticated]            
   def get(self , request):
    user = request.user
    cart = Cart.objects.filter(user = user , ordered = False).first()
    queryset = OderItem.objects.filter(cart = cart)
    serializer = OrderItemSerializer(queryset , many = True)
    return Response(serializer.data)


   def post(self , request):
    data = request.data 
    user = request.user
    cart,_ = Cart.objects.get_or_create(user = user , ordered = False)
    product = add_new_manu.objects.get( id = data.get('product')) 
    price = product.Offer_price
    quantity = data.get('quantity')
    cart_items = OderItem(user = user, cart = cart, product = product ,   price = price,  quantity =  quantity)
    cart_items.save()  
    total_price = 0
    cart_items = OderItem.objects.filter(user = user , cart = cart.id)
    for items in cart_items:
      total_price += items.price 
    cart.total_price = total_price
    cart.save()                 
    return Response({'success':'items add to the the carts'})

   def put(self , request):
      data = request.data
      cart_item = OderItem.objects.get(id = data.get('id'))            
      quantity = data.get("quantity")  
      cart_item.quantity += quantity 
      cart_item.save()
      return Response({'success':"item updated"})  
   
   def delete(self , request):
    user = request.user
    data = request.data
    cart_item = OderItem.objects.get(id = data.get('id'))
    cart_item.delete()
    cart = Cart.objects.filter(user = user , ordered = False).first()
    queryset = OderItem.objects.filter(cart = cart)
    serializer = OrderItemSerializer(queryset , many = True)
    return Response(serializer.data)
                                        
      



