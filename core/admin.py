from django.contrib import admin
from django import forms
from .models import *
from django.urls import path
from django.utils.html import format_html


# Action to duplicate selected records
def duplicate_model(modeladmin, request, queryset):
    for obj in queryset:
        obj.pk = None  # Reset primary key to create a new record
        obj.save()  # Save the new object

duplicate_model.short_description = "Duplicate selected records"

# Admin classes
class AccountPromoAdmin(admin.ModelAdmin):
    list_display = ('main_heading', 'features_heading', 'cta_text')
    search_fields = ('main_heading', 'description')
    list_filter = ('features_heading',)
    fieldsets = (
        (None, {
            'fields': ('main_heading', 'description', 'features_heading', 'features', 'image', 'cta_text', 'cta_url')
        }),
    )
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        return obj.image.url if obj.image else "No Image"

    image_preview.short_description = 'Image Preview'

admin.site.register(AccountPromo, AccountPromoAdmin)

class NewsUpdateAdmin(admin.ModelAdmin):
    actions = [duplicate_model]
    list_display = ('heading', 'headline', 'cta_text')
    search_fields = ('heading', 'headline', 'description')
    list_filter = ('headline',)
    fieldsets = (
        (None, {
            'fields': ('heading', 'image', 'headline', 'description', 'cta_text', 'cta_link')
        }),
    )
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        return obj.image.url if obj.image else "No Image"

    image_preview.short_description = 'Image Preview'

admin.site.register(NewsUpdate, NewsUpdateAdmin)

class OffersPromoAdmin(admin.ModelAdmin):
    list_display = ('title', 'header', 'cta_text')
    search_fields = ('title', 'description')
    filter_horizontal = ('images',)

admin.site.register(OffersPromo, OffersPromoAdmin)
admin.site.register(OfferImage)

@admin.register(FinancialSolutionPromo)
class FinancialSolutionPromoAdmin(admin.ModelAdmin):
    actions = [duplicate_model]
    list_display = ('display_main_heading', 'card_title', 'cta_text')
    search_fields = ('main_heading', 'card_title', 'card_header')
    list_filter = ('card_title',)
    
    def display_main_heading(self, obj):
        return obj.main_heading if obj.main_heading else "No Main Heading"
    display_main_heading.short_description = 'Main Heading'
    
 

@admin.register(PromoBanner)
class PromoBannerAdmin(admin.ModelAdmin):
    list_display = ('banner_text', 'description')
    search_fields = ('banner_text', 'description')
@admin.register(PromoBannerFull)
class PromoBannerFullAdmin(admin.ModelAdmin):
    list_display = ('banner_text', 'description')
    search_fields = ('banner_text', 'description')
@admin.register(BankingPromo)
class BankingPromoAdmin(admin.ModelAdmin):
    list_display = ('title', 'promo_type', 'cta_text')
    search_fields = ('title', 'description')

@admin.register(AccountsPage)
class AccountsPageAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(AccountSection)
class AccountSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)

@admin.register(Account)
class AccountTypeAdmin(admin.ModelAdmin):
    list_display = ('type',)
    list_filter = ('type',)

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('title', 'tag')
    search_fields = ('title', 'tag')

class FAQItemInline(admin.TabularInline):
    model = FAQItem
    extra = 1  # Number of empty forms to display

@admin.register(FAQSection)
class FAQSectionAdmin(admin.ModelAdmin):
    inlines = [FAQItemInline]
    search_fields = ('title',)

admin.site.register(FAQItem)

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    
    list_display = ['title']

class HeroSliderImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']
    search_fields = ['title', 'description']

admin.site.register(HeroSliderImage, HeroSliderImageAdmin)

class HeroSectionSliderAdmin(admin.ModelAdmin):
    list_display = ['title']
    filter_horizontal = ('slides',)

admin.site.register(HeroSectionSlider, HeroSectionSliderAdmin)

class AccountFeatureInline(admin.TabularInline):
    model = AccountFeature
    extra = 1  # Number of empty forms to display

@admin.register(AccountFeaturesPromo)
class AccountFeaturesPromoAdmin(admin.ModelAdmin):
    inlines = [AccountFeatureInline]

admin.site.register(AccountFeature)

class EligibilityDocTileInline(admin.TabularInline):
    model = EligibilityDocTile
    extra = 1  # Number of extra forms to display by default

@admin.register(EligibilityDocsSection)
class EligibilityDocsSectionAdmin(admin.ModelAdmin):
    list_display = ('title',)  # Display section title in the admin list view
    inlines = [EligibilityDocTileInline]  # Inline to manage tiles within the section

@admin.register(Homepage)
class HomepageAdmin(admin.ModelAdmin):
    list_display = ('title',)
    filter_horizontal = ('hero_slider_sections', 'news_updates', 'financial_solution_promo')

@admin.register(AccountDetails)
class AccountDetailsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    filter_horizontal = ('eligibility_docs','account_features')

class FooterLinkInline(admin.TabularInline):
    model = FooterLink
    extra = 1

@admin.register(FooterSection)
class FooterSectionAdmin(admin.ModelAdmin):
    inlines = [FooterLinkInline]
# Inline class for RedBoxPromoEntry to display promo entries within RedBoxPromo
class RedBoxPromoEntryInline(admin.TabularInline):
    model = RedBoxPromoEntry
    extra = 1  # Number of extra empty rows to display for adding new entries

# Register RedBoxPromo using @admin.register decorator
@admin.register(RedBoxPromo)
class RedBoxPromoAdmin(admin.ModelAdmin):
    inlines = [RedBoxPromoEntryInline]  # Inline for adding/editing RedBoxPromoEntry items within RedBoxPromo

# Register Careers model using @admin.register decorator
@admin.register(Careers)
class CareersAdmin(admin.ModelAdmin):
    list_display = ['title']  # Display 'title' in the admin list view
    filter_horizontal = ('careers_features',)  # Enable horizontal filter widget for ManyToManyField

@admin.register(ModalPromo)
class ModalPromoAdmin(admin.ModelAdmin):
    list_display = ('header', 'title', 'person_name', 'cta_text')

# Define an inline class for VisionMissionEntry to be displayed in the VisionMissionPromo admin
class VisionMissionEntryInline(admin.TabularInline):  # or admin.StackedInline for a different layout
    model = VisionMissionEntry
    extra = 1  # Number of empty forms displayed (for adding new entries)
    fields = ['logo', 'header', 'description']  # Fields to show for each entry

# Register VisionMissionPromo in the admin with the inline for VisionMissionEntry
@admin.register(VisionMissionPromo)
class VisionMissionPromoAdmin(admin.ModelAdmin):
    list_display = ('promo_title',)  # Show promo title in the listing
    inlines = [VisionMissionEntryInline]  # Add inline form to allow multiple entries

@admin.register(AboutUs)
class AboutusAdmin(admin.ModelAdmin):
    list_display = ['title']  # Display 'title' in the admin list view
    filter_horizontal = ('aboutus_features',)  # Enable horizontal filter widget for ManyToManyField

@admin.register(AwardsPage)
class AwardsAdmin(admin.ModelAdmin):
    list_display = ['title']  # Display 'title' in the admin list view
    
@admin.register(CareersOpportunityPage)
class CareersOppAdmin(admin.ModelAdmin):
    list_display = ['title']  # Display 'title' in the admin list view

@admin.register(HRMessage)
class HRMessageAdmin(admin.ModelAdmin):
    list_display = ('hrname', 'hrdesignation')  

class JobInline(admin.TabularInline):
    model = Jobs
    extra = 1

@admin.register(JobsPage)
class JobsSectionAdmin(admin.ModelAdmin):
    inlines = [JobInline]

@admin.register(JobsLP)
class JobsLPAdmin(admin.ModelAdmin):
    list_display = ['title']  # Display 'title' in the admin list view


@admin.register(FinancialReports)
class ReportsTypeAdmin(admin.ModelAdmin):
    list_display = ('type',)
    list_filter = ('type',)

@admin.register(FinancialReportsCard)
class ReportsCardAdmin(admin.ModelAdmin):
    actions = [duplicate_model]
    list_display = ('title','year')

@admin.register(ReportsTabSection)
class ReportsTabSectionAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(FinancialReportsPage)
class FinancialReportPageAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(ElectionDirectorsPage)
class ElectionDirectorsPageAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(BranchPage)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(ArticleSection)
class ArticleSectionAdmin(admin.ModelAdmin):
    list_display = ('title',)
@admin.register(ArticlePage)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(InvestorsPromo)
class InvestorPromoAdmin(admin.ModelAdmin):
    list_display = ('title',)
@admin.register(Investors)
class InvestorsAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)
@admin.register(LeadershipPage)
class LeadershipPageAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(MediaCards)
class MediaCardsAdmin(admin.ModelAdmin):
    list_display = ('tab',)
@admin.register(MediaPage)
class MediaPageAdmin(admin.ModelAdmin):
    list_display = ('title',)


class CompaniesPromoInline(admin.TabularInline):  # or admin.StackedInline for a different layout
    model = AssociatedCompaniesPromoEntry
    extra = 1  # Number of empty forms displayed (for adding new entries)
    fields = ['image','title','header','status_description','cta_text','cta_link']  # Fields to show for each entry

# Register VisionMissionPromo in the admin with the inline for VisionMissionEntry
@admin.register(AssociatedCompaniesPromo)
class CompaniesPromoAdmin(admin.ModelAdmin):
    list_display = ('promo_title',)  # Show promo title in the listing
    inlines = [CompaniesPromoInline]  # Add inline form to allow multiple entries

@admin.register(CompanyDetails)
class CompanyInfo(admin.ModelAdmin):
    list_display = ('status_description',)

@admin.register(TablePromo)
class TablePromoAdmin(admin.ModelAdmin):
    list_display = ('title',)
@admin.register(CompanyProfile)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(LegalAdvisorsPromo)
class LegalAdvisorsPromoAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(GovernancePage)
class GovernanceAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(QuickLinks)
class LinksAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(ComplaintFormData)
class CustomerComplaint(admin.ModelAdmin):
    list_display = ('customer_name',)

@admin.register(FraudulentFundTransferComplaint)
class FraudulentFundTransferComplaintAdmin(admin.ModelAdmin):
    list_display = ('customer_name',)

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('cta_text',)

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(InvestorRelation)
class InvestorRelationAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(GrievancePromo)
class GrievancePromo(admin.ModelAdmin):
    list_display = ('title',)

import nested_admin

class NavbarContentLinkInline(nested_admin.NestedTabularInline):
    model = NavbarContentLink
    extra = 1
    fields = ['name', 'url', 'is_active']


class NavbarSubTabInline(nested_admin.NestedStackedInline):
    model = NavbarSubTab
    inlines = [NavbarContentLinkInline]  # Include content link inline
    extra = 1
    fields = ['name','url', 'order', 'is_active']


class NavbarMainItemAdmin(nested_admin.NestedModelAdmin):
    model = NavbarMainItem
    inlines = [NavbarSubTabInline]  # Include sub-tab inline
    list_display = ['name', 'order','nav_type' ]
    list_editable = ['order', ]


admin.site.register(NavbarMainItem, NavbarMainItemAdmin)

@admin.register(NavigationMain)
class NavigationMainAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(EmploymentApplication)
class EmploymentApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'mobile_number', 'cnic', 'created_at')
    search_fields = ('full_name', 'email', 'cnic')
    list_filter = ('city', 'qualification', 'created_at')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(FileUpload)
class FileUploadAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'upload_date', 'file_url_display')
    search_fields = ('name', 'description')
    readonly_fields = ('upload_date', 'file_url_display')
    
    def file_url_display(self, obj):
        if obj.file:
            return format_html('<a href="{}" target="_blank">Download</a>', obj.file.url)
        return "No file"
    
    file_url_display.short_description = 'File Download'

@admin.register(EmploymentApplicationPage)
class EmploymentApplicationPageAdmin(admin.ModelAdmin):
    list_display = ('title',)
    filter_horizontal = ('hero_sections',) if hasattr(EmploymentApplicationPage, 'hero_sections') and isinstance(EmploymentApplicationPage._meta.get_field('hero_sections'), models.ManyToManyField) else ()