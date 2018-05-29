from django.contrib import admin
from .models import *
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

admin.site.register(Race)
admin.site.register(Chien)
admin.site.register(Proprietaire)
admin.site.register(Photo)
admin.site.register(Rental)

class RentalAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
    }
