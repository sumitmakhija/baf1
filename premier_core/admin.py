from django.contrib import admin
from .models import *
import nested_admin
# Register your models here.

@admin.register(Homepage)
class HomepageAdmin(admin.ModelAdmin):
    list_display = ('title',)
    
@admin.register(PremierCardsPromoPages)
class CardsAdminPromoISlamic(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(PremierIndividualAccounts)
class IndAccountsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    actions = ['duplicate_records']

    @admin.action(description='Duplicate selected records')
    def duplicate_records(self, request, queryset):
        for obj in queryset:
            obj_copy = obj  # Create a copy of the object
            obj_copy.pk = None  # Reset the primary key to create a new record
            obj_copy.title = f"Copy of {obj.title}"  # Optionally modify the title to indicate duplication
            obj_copy.save()

@admin.register(ColumnSection)
class ColumnSectionAdmin(admin.ModelAdmin):
    list_display = ('title',)

class MultiColumnFAQItemInline(admin.StackedInline):
    model = MultiColumnFAQItem
    extra = 1  # Number of empty forms to display

@admin.register(MultiColumnFAQSection)
class MultiColumnFAQSectionAdmin(admin.ModelAdmin):
    inlines = [MultiColumnFAQItemInline]
    search_fields = ('title',)

# Inline admin for GoldenPromoCTA
class GoldenPromoCTAInline(admin.StackedInline):
    model = GoldenPromoCTA
    extra = 1  # Number of empty forms to display

# Register GoldenPromoCTAEntry with the inline
@admin.register(GoldenPromoCTAEntry)
class GoldenPromoCTAEntryAdmin(admin.ModelAdmin):
    inlines = [GoldenPromoCTAInline]  # Adding the inline to the parent model
    search_fields = ('title',)  # Allow searching by the title

class PremierFAQQuestionAnswerInline(nested_admin.NestedStackedInline):
    model = PremierFAQQuestionAnswer
    fields = ['question', 'answer_col_1', 'answer_col_2']
    extra = 1  # Number of empty forms to display


class PremierFAQCategoryInline(nested_admin.NestedStackedInline):
    model = PremierFAQCategory
    inlines = [PremierFAQQuestionAnswerInline]
    
    extra = 1  # Number of empty forms to display


@admin.register(NestedFAQPremier)
class NestedFAQSectionAdmin(nested_admin.NestedModelAdmin):
    inlines = [PremierFAQCategoryInline]
    search_fields = ('title',)

class LocationInline(admin.StackedInline):  # or use admin.StackedInline for a different layout
    model = Location
    extra = 1  # Number of extra blank forms to display

@admin.register(ContactUsData)
class RegionAdmin(admin.ModelAdmin):
    inlines = [LocationInline]  # Attach the inline model
    list_display = ['title']  # Display region name in admin list view

@admin.register(ContactUsPage)
class ContactUsPageAdmin(admin.ModelAdmin):
    list_display = ('title',)

class FinanceProgramDetailInline(admin.TabularInline):  # Use TabularInline for inline editing
    model = FinanceProgramDetail
    extra = 1  # Number of empty forms displayed

@admin.register(FinanceProgram)
class FinanceProgramAdmin(admin.ModelAdmin):
    inlines = [FinanceProgramDetailInline]
    list_display = ['title']


@admin.register(HomeFinancePage)
class HomeFinancePageAdmin(admin.ModelAdmin):
    list_display = ('title',)

class StepsPromoEntryInline(admin.TabularInline):  # Use TabularInline for inline editing
    model = StepsPromoEntry
    extra = 1  # Number of empty forms displayed

@admin.register(StepsPromo)
class StepsPromoAdmin(admin.ModelAdmin):
    inlines = [StepsPromoEntryInline]
    list_display = ['title']


@admin.register(FinancingOptionPages)
class FinancingOptionPagesAdmin(admin.ModelAdmin):
    list_display = ('title',)

class OrbitPromoEntryInline(admin.StackedInline):  
    model = OrbitPromoEntry
    extra = 1  # Number of empty forms displayed

@admin.register(OrbitPromo)
class OrbitPromoAdmin(admin.ModelAdmin):
    inlines = [OrbitPromoEntryInline]
    list_display = ['title']

@admin.register(OrbitRewardPages)
class OrbitRewardPagesAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(MiscellenousPages)
class MiscellenousPagesAdmin(admin.ModelAdmin):
    list_display = ('title',)

class LogosPromoEntryInline(admin.StackedInline):  
    model = LogosPromoEntry
    extra = 1  # Number of empty forms displayed

@admin.register(LogosPromo)
class LogosPromoAdmin(admin.ModelAdmin):
    inlines = [LogosPromoEntryInline]
    list_display = ['title']