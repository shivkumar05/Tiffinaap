from django.db import models
from django.dispatch import receiver
from tiffinapp.models.users import sigin
from tiffinapp.models.manus import add_new_manu
from django.db.models.signals import pre_save , post_save
from django.contrib.auth.models import User   



class Cart(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False) 
    total_price = models.FloatField(default=0)
     
    def __str__(self):
        return str(self.user.username) + " " + str(self.total_price)                 
     
class OderItem(models.Model):
    cart = models.ForeignKey(Cart ,on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    product = models.ForeignKey(add_new_manu , on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=1)
     
    def __str__(self):
        return str(self.user.username)+ " " + str(self.product.Tiffin_Name)
     
@receiver(pre_save , sender = OderItem)
def correct_price(sender , **kwargs):
    cart_items = kwargs['instance']
    price_of_product = add_new_manu.objects.get(id = cart_items.product.id)
    cart_items.price = cart_items.quantity * float(price_of_product.Offer_price)
    total_cart_items = OderItem.objects.filter(user = cart_items.user)   
    # cart = Cart.objects.get(id = cart_items.cart.id)
    # cart.total_price = cart_items.price
    # cart.save()
    
               

     
       