from django.contrib import admin
from .models import Post,Category,AboutUs

#Admin Post Modal Create
class PostAdmin(admin.ModelAdmin):
    list_display=('title','content')
    search_fields=('title','content')
    list_filter=('category','create_at')
    
# Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(AboutUs)
