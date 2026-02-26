from django.contrib import admin
from .models import Banner, on_offer, sale_offer
# Register your models here.

admin.site.register(Banner)
admin.site.register(on_offer)
admin.site.register(sale_offer)

admin.site.site_header = "Jahed Admin Panel"
admin.site.site_title = "Jahed Dashboard"
admin.site.index_title = "Welcome to Custom Admin"