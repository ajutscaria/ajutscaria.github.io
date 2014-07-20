from django.contrib import admin
from search.models import DestinationCategory, AttractionCategory, Destination, Attraction

#class AttractionCategoryInline(admin.StackedInline):
#    model = AttractionCategory
#    extra = 1

#class AttractionAdmin(admin.ModelAdmin):
#    inlines = [AttractionCategoryInline]

#class DestinationCategoryInline(admin.StackedInline):
#    model = DestinationCategory
#    extra = 1

#class DestinationAdmin(admin.ModelAdmin):
#    inlines = [DestinationCategoryInline]

admin.site.register(AttractionCategory)
admin.site.register(DestinationCategory)
admin.site.register(Attraction)
admin.site.register(Destination)