from django.contrib import admin
from wolfapp.models import Post,Product,Contact

# Register your models here.
#admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):

    list_display=['fullname','age','gender','weight','cat','status','created_on']

    list_filter=['cat','status']

#register modeladmin class with model

admin.site.register(Post,PostAdmin)
admin.site.site_header="Foxx_Fitness"
admin.site.site_title="Come To Foxx_Fitness"
admin.site.index_title="Foxx_Fitness Site"


class ProductAdmin(admin.ModelAdmin):
    list_display=('name','price','Status')

admin.site.register(Product,ProductAdmin)

#class ContactAdmin(admin.ModelAdmin):
    
    
admin.site.register(Contact)