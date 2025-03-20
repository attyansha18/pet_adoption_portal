from django.contrib import admin
from .models import Pet

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'breed', 'adoption_status')
    search_fields = ('name', 'breed')
    list_filter = ('adoption_status',)
    ordering = ('name',)
