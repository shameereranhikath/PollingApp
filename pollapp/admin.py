from django.contrib import admin
from .models import Poll

# Register your models here.
admin.site.site_header='Poll Admin'
admin.site.site_title='Poll Admin Area'
admin.site.index_title='Welcome to Poll Admin Area'

admin.site.register(Poll)
