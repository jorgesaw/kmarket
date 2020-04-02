"""Customers models admin."""

# Django
from django.contrib import admin

# Models
from apps.persons.models import Address
from apps.customers.models import Customer


class AddressAdmin(admin.TabularInline):
    model = Address

    autocomplete_fields = ('city',)
    
    fields = ('street', 'number_street', 'city', 'type_address')
    list_display = ('get_address', 'city')

    ordering = ('id',)
    list_editable = ('street', 'number_street', 'city', 'type_address')
    list_select_related = ('city',)
    extra = 1

    def get_address(self, obj):
        return obj.__str__()
    get_address.short_description = "Dirección"

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    fields = ( 
        ('id_card', 'last_name'), 
        ('first_name', 'birth_date'), 
        ('movile_number', 'telephone_number'), 
    )
    readonly_fields = ('created', 'modified')
    list_display = ('full_name', 'movile_number')
    list_filter = ('last_name',)
    
    ordering = ('last_name', 'first_name', 'id_card')
    search_fields = ('id_card', 'last_name', 'first_name')
    date_hierarchy = 'modified' # Jerarquizar por fechas
    
    inlines = [AddressAdmin,]
