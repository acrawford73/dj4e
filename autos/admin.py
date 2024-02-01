from django.contrib import admin
from .models import Autos, Make


# class MakeAdmin(admin.ModelAdmin):
# 	class Meta:
# 		model = Make

# class AutosAdmin(admin.ModelAdmin):
# 	class Meta:
# 		model = Autos


admin.site.register(Make)#, MakeAdmin)
admin.site.register(Autos)#, AutosAdmin)
