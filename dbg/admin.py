from django.contrib import admin
from dbg.models import *
# Register your models here.

@admin.register(DBGAllText)
class DBGTextPromoAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(DBGVideoSection)
class DBGVideoSectionAdmin(admin.ModelAdmin):
    list_display = ('heading',)

class TextFullDBGEntryInline(admin.TabularInline):
    model = TextFullDBGEntry
    extra = 1  


@admin.register(TextFullDBG)
class TextFullDBGAdmin(admin.ModelAdmin):
    list_display = ("heading",)
    inlines = [TextFullDBGEntryInline]  
class TextColDBGEntryInline(admin.StackedInline):
    model = TextColDBGEntry
    extra = 1  


@admin.register(TextColDBG)
class TextColDBGAdmin(admin.ModelAdmin):
    list_display = ("heading",)
    inlines = [TextColDBGEntryInline] 
@admin.register(ProductTextDBG)
class ProductTextDBGAdmin(admin.ModelAdmin):
    list_display = ('heading',)

class SupportServicesEntryInline(admin.StackedInline):
    model = SupportServicesEntry
    extra = 1  


@admin.register(SupportServices)
class SupportServicesAdmin(admin.ModelAdmin):
    list_display = ("heading",)
    inlines = [SupportServicesEntryInline] 

class BoxPromoEntryInline(admin.StackedInline):
    model = BoxPromoEntry
    extra = 1  


@admin.register(BoxPromo)
class BoxPromoEntryAdmin(admin.ModelAdmin):
    list_display = ("heading",)
    inlines = [BoxPromoEntryInline] 


class FeatureBoxEntryInline(admin.StackedInline):
    model = FeaturesBoxEntry
    extra = 1  


@admin.register(FeaturesBox)
class FeaturesBoxEntryAdmin(admin.ModelAdmin):
    list_display = ("title",)
    inlines = [FeatureBoxEntryInline] 

@admin.register(DBGPages)
class DBGPagesAdmin(admin.ModelAdmin):
    list_display = ('title',)
admin.site.register(DBGAccount)
admin.site.register(DBGCard)
admin.site.register(DBGAccountSection)

@admin.register(KeyFactsSection)
class KeyFactsSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'cta_text')