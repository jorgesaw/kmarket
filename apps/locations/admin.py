"""Locations models admin."""

# Django
from django.contrib import admin

# Models
from apps.locations.models import State, City


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    fields = ( 'name',)
    readonly_fields = ('created', 'modified')
    list_display = ('name',)
    list_filter = ('name',)
    
    ordering = ('name',)
    search_fields = ('name',)
    date_hierarchy = 'modified'


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    autocomplete_fields = ('state',)
    
    fields = ( 'name', 'zip_city', 'ddn', 'state')
    readonly_fields = ('created', 'modified')
    list_display = ('name', 'zip_city', 'ddn', 'state')
    list_filter = ('name',)
    
    ordering = ('name',)
    search_fields = ('name',)
    date_hierarchy = 'modified'
    list_editable = ('zip_city', 'ddn')
    list_select_related = ('state',)

