from django.contrib import admin
from .models import Product, Image, Variation
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
	date_hierarchy = 'time'
	search_fields = ['title', 'price']
	list_filter = ['active', 'price']
	list_display = ['title', 'price', 'description', 'time', 'active']
	list_editable = ['price', 'active']
	readonly_fields = ['time']
	prepopulated_fields = {'slug': ('title',)}
	class Meta:
		model = Product


admin.site.register(Product, ProductAdmin)

admin.site.register(Image)

admin.site.register(Variation)



