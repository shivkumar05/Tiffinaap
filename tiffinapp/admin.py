from django.contrib import admin
from tiffinapp.models.manus import  add_new_manu 
from tiffinapp.models.users import  sigin , account , center
from tiffinapp.models.category import Category 
from tiffinapp.models.orderlist import Cart , OderItem
from tiffinapp.models.forget import Profile


# class Adminadd_new_manu(admin.ModelAdmin):
#    list_display = ['image' ,'Tiffin_Name' , ' categery' , ' Tiffin_Price' ,' Offer_price' ,' Description']

# class Adminaccount(admin.ModelAdmin):
#   list_display = [' Name' ,' phone_number' , 'choose_center' , 'email' ,'password' ]

admin.site.register(sigin)
admin.site.register(account)
admin.site.register(add_new_manu)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(OderItem)
admin.site.register(center)
admin.site.register(Profile)

# class add_new_manueAdmin(admin.ModelAdmin):
#      list_display = ['image' , ' Tiffin_Name' , 'Tiffin_Price' , 'Offer_price' , 'Description']         
# admin.site.register(add_new_manu , add_new_manueAdmin)
     