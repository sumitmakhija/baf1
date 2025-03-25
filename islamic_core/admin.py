from django.contrib import admin
from .models import *
from django.db import transaction   
# Register your models here.
import nested_admin


@admin.register(IslamicHomepage)
class IslamicHomepageAdmin(admin.ModelAdmin):
    list_display = ('title',)


class TabDataInline(admin.StackedInline):  # or use `admin.StackedInline` if you prefer
    model = TabData
    extra = 1  # Number of extra forms to display

@admin.register(FeaturesTab)
class FeaturesTabAdmin(admin.ModelAdmin):

    inlines = [TabDataInline]
    list_display = ('title',)  # Customize list display if needed
    

@admin.register(IslamicAccountFeature)
class IslamicAccFeature(admin.ModelAdmin):
    list_display = ('title',)
    actions = ['duplicate_islamic_account_feature']  # Add custom action

    @transaction.atomic
    def duplicate_islamic_account_feature(self, request, queryset):
        """
        Action to duplicate selected IslamicAccountFeature records with all related data.
        """
        for feature in queryset:
            # Duplicate the main IslamicAccountFeature object
            original_id = feature.id
            feature.pk = None  # Reset the primary key to create a new record
            feature.title = f"Copy of {feature.title}"  # Modify title to indicate duplication
            feature.save()

            # Duplicate and associate eligibility_docs
            new_eligibility_docs = []
            for doc in feature.eligibility_docs.all():
                doc.pk = None  # Reset the primary key to create a new record
                doc.save()
                new_eligibility_docs.append(doc)
            feature.eligibility_docs.set(new_eligibility_docs)  # Associate the new duplicated docs

            # Duplicate and associate tab_section
            new_tab_data = []
            for tab in feature.tab_section.all():
                tab.pk = None  # Reset the primary key to create a new record
                tab.save()
                new_tab_data.append(tab)
            feature.tab_section.set(new_tab_data)  # Associate the new duplicated tab data

            feature.save()  # Save the feature with its new associations

        self.message_user(request, "Selected IslamicAccountFeature records with all related data have been duplicated successfully.")

    duplicate_islamic_account_feature.short_description = "Duplicate selected IslamicAccountFeature records with all data"
@admin.register(CardPromoSection)
class AccountSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)

@admin.register(AccountsPageIslamic)
class AccountsPageAdminIslamic(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(CardsPromoPages)
class CardsAdminPromoISlamic(admin.ModelAdmin):
    list_display = ('title',)

class CDMDataSectionInline(admin.StackedInline):  # Use TabularInline for a compact view
    model = CDMDataSection
    extra = 1  # Number of empty forms to display

@admin.register(CDMParentSection)
class CDMParentSectionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [CDMDataSectionInline]

@admin.register(CDMPage)
class CDMPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'cdm_section')  # Display the title and linked CDMParentSection


class GalleryDataInline(admin.TabularInline):  # Use StackedInline for a more detailed view
    model = GalleryData
    extra = 1  # Number of empty forms to display

@admin.register(GalleryMain)
class GalleryDataAdmin(admin.ModelAdmin):
    list_display = ('title',)  # Display the title of the gallery
    inlines = [GalleryDataInline]  # Inline to add multiple entries

@admin.register(GalleryPage)
class GalleryPageAdmin(admin.ModelAdmin):
    list_display = ('title',)  

@admin.register(IslamicRecurringDepositPage)
class IslamicRecurringDepositPageAdmin(admin.ModelAdmin):
    list_display = ('title',)  

class multirowpromoItemInline(admin.StackedInline):
    model = multirowpromoItem
    extra = 1  # Number of blank entries to display by default

@admin.register(multirowpromo)
class HeaderDescriptionSectionAdmin(admin.ModelAdmin):
    list_display = ('title',)  # Display title in the admin list
    inlines = [multirowpromoItemInline]  # Add inline model

@admin.register(SupplyChainFinancePage)
class SupplyChainFinancePageAdmin(admin.ModelAdmin):
    list_display = ('title',) 


class IslamicFAQItemInline(admin.StackedInline):
    model = IslamicFAQItem
    extra = 1  # Number of empty forms to display

@admin.register(IslamicFAQSection)
class IslamicFAQSectionAdmin(admin.ModelAdmin):
    inlines = [IslamicFAQItemInline]
    search_fields = ('title',)

@admin.register(WomenServicesPage)
class WomenServicesPageAdmin(admin.ModelAdmin):
    list_display = ('title',) 

class FAQQuestionAnswerInline(nested_admin.NestedTabularInline):
    model = FAQQuestionAnswer
    extra = 1  # Number of empty forms to display


class FAQCategoryInline(nested_admin.NestedTabularInline):
    model = FAQCategory
    inlines = [FAQQuestionAnswerInline]
    extra = 1  # Number of empty forms to display


@admin.register(NestedFAQSection)
class NestedFAQSectionAdmin(nested_admin.NestedModelAdmin):
    inlines = [FAQCategoryInline]
    search_fields = ('title',)

class TilePromoItemInline(admin.TabularInline):  # Tabular for compact layout
    model = TilePromoItem
    extra = 1  # Display 1 empty form by default

@admin.register(TilePromoSection)
class TilePromoSectionAdmin(admin.ModelAdmin):
    inlines = [TilePromoItemInline]
    search_fields = ('title',)  # Enable search by title

@admin.register(GreenPromoCTA)
class SectionWithCTAsAdmin(admin.ModelAdmin):
    list_display = ('title',) 
@admin.register(AlfaBNPL)
class AlfaBNPLPageAdmin(admin.ModelAdmin):
    list_display = ('title',) 

@admin.register(AboutUsIslamic)
class AboutUsIslamicPageAdmin(admin.ModelAdmin):
    list_display = ('title',) 

# Inline for FileFAQQuestionAnswer
class FileFAQQuestionAnswerInline(nested_admin.NestedTabularInline):
    model = FileFAQQuestionAnswer
    extra = 1  # Number of empty forms to display
    fields = ['file_name', 'small_desc', 'file_cta_text', 'file_cta_url']

# Inline for FileFAQCategory
class FileFAQCategoryInline(nested_admin.NestedTabularInline):
    model = FileFAQCategory
    inlines = [FileFAQQuestionAnswerInline]  # Add inline for questions and answers
    extra = 1  # Number of empty forms to display
    fields = ['header']

# Admin for FileNestedFAQSection
@admin.register(FileNestedFAQSection)
class FileNestedFAQSectionAdmin(nested_admin.NestedModelAdmin):
    inlines = [FileFAQCategoryInline]  # Inline for categories
    search_fields = ('title',)

@admin.register(IslamicMisc)
class IslamicMiscPageAdmin(admin.ModelAdmin):
    list_display = ('title',) 