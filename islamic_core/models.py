from django.db import models
from core.models import *

# Create your models here.

class IslamicHomepage(models.Model):
    title = models.CharField(max_length=255)
    hero_slider_sections = models.ManyToManyField(HeroSectionSlider, related_name='isl_homepages', blank=True)
    navbar = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,related_name='islamic_homepages')
    subnav = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=2,related_name="isl_sub_nav")
    hero_sections = models.ManyToManyField(HeroSection, related_name='islamic_homepages')
    account_promo = models.ForeignKey(AccountPromo, on_delete=models.SET_NULL, null=True, blank=True,related_name='islamic_homepages')
    news_updates = models.ManyToManyField(NewsUpdate, related_name='islamic_homepages')
    offers_promo = models.ForeignKey(OffersPromo, on_delete=models.SET_NULL, null=True, blank=True,related_name='islamic_homepages')  
    financial_solution_promo = models.ManyToManyField(FinancialSolutionPromo, related_name='islamic_homepages', blank=True)
    promo_banner = models.ForeignKey(PromoBanner, on_delete=models.SET_NULL, null=True, blank=True,related_name='islamic_homepages')
    banking_promo = models.ManyToManyField(BankingPromo, related_name='islamic_homepages', blank=True)      
    footer_section = models.ForeignKey(FooterSection, on_delete=models.CASCADE, related_name='islamic_homepages', default=1)  # Corrected ForeignKey field
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Islamic Homepage"
class FeaturesTab(models.Model):
    title = models.CharField(max_length=255)  # The name of the tab

    class Meta:
        verbose_name_plural = "Features Tabs"

    def __str__(self):
        return self.title

class TabData(models.Model):
    features_tab = models.ForeignKey(FeaturesTab, related_name='tab_data', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)  # Name field for each data entry
    content = RichTextField()  

    class Meta:
        verbose_name_plural = "Tab Data"

    def __str__(self):
        # Optional - Display a truncated version of content for clarity
        return f"{self.name} - {self.features_tab.title}"
    
class IslamicAccountFeature(models.Model):

    title = models.CharField(max_length=255)
    navbar = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=3)
    subnav = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=2,related_name="acc_feature_sub_nav")
    hero_sections = models.ForeignKey(HeroSection, on_delete=models.CASCADE,related_name='IslamicAccountFeature')
    eligibility_docs = models.ManyToManyField(EligibilityDocTile, blank=True)
    promo_banner = models.ForeignKey(PromoBanner, on_delete=models.SET_NULL, null=True, blank=True)
    promo_banner_full = models.ForeignKey(PromoBannerFull, on_delete=models.SET_NULL, null=True, blank=True)
    tab_section = models.ManyToManyField(TabData, related_name='IslamicAccountFeature') 
    card_info_1 = models.ForeignKey(TablePromo, on_delete=models.SET_NULL, null=True,blank=True, related_name='table_1')
    card_info_2 = models.ForeignKey(TablePromo, on_delete=models.SET_NULL, null=True,blank=True, related_name='table_2')
    faq_islamic = models.ManyToManyField(FAQItem, related_name='faq_islamic')

    footer_section = models.ForeignKey(FooterSection, on_delete=models.CASCADE, related_name='IslamicAccountFeature', default=1)  

    class Meta:
        verbose_name_plural = "Islamic Account Features"
    
    def __str__(self):
        return self.title

class CardPromoSection(models.Model):
    title = models.CharField(max_length=255,blank=True)
    description = models.TextField(blank=True)
    cards = models.ManyToManyField(Card, related_name='CardPromoSection')
    
    class Meta:
        verbose_name_plural = "Card Promo Sections"

    def __str__(self):
        return self.title if self.title else 'No title'
    
class AccountsPageIslamic(models.Model):
    title = models.CharField(max_length=255)
    navbar = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=3)
    subnav = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=2,related_name="acc_page_sub_nav")
    hero_sections = models.ForeignKey(HeroSection, on_delete=models.SET_NULL ,null=True,related_name='AccountsPageIslamic')
    accounts_promo_all = models.ForeignKey(AccountSection, on_delete=models.SET_NULL ,null=True,related_name='AccountsPageIslamic')
    promo_banner = models.ForeignKey(PromoBanner, on_delete=models.SET_NULL, null=True, blank=True)
    footer_section = models.ForeignKey(FooterSection,on_delete=models.CASCADE, related_name='AccountsPageIslamic',default=1)   

    class Meta:
        verbose_name_plural = "Accounts Pages Islamic"

    def __str__(self):
        return self.title
    
class CardsPromoPages(models.Model):
    title = models.CharField(max_length=255)
    navbar = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=3)
    subnav = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=2,related_name="cards_promo_sub_nav")
    hero_sections = models.ForeignKey(HeroSection, on_delete=models.SET_NULL ,null=True,related_name='CardsPromoPages')
    cards = models.ForeignKey(CardPromoSection, on_delete=models.SET_NULL ,null=True,related_name='CardsPromoPages')
    promo_banner = models.ForeignKey(PromoBanner, on_delete=models.SET_NULL, null=True, blank=True)
    footer_section = models.ForeignKey(FooterSection,on_delete=models.CASCADE, related_name='CardsPromoPages',default=1)   

    class Meta:
        verbose_name_plural = "Cards Promo Pages"

    def __str__(self):
        return self.title

class CDMParentSection(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "CDM Parent Sections"

    def __str__(self):
        return self.title

class CDMDataSection(models.Model):
    parent_section = models.ForeignKey(CDMParentSection, on_delete=models.CASCADE, related_name="cdm_entries")
    city_name = models.CharField(max_length=255)
    description = RichTextField()

    class Meta:
        verbose_name_plural = "CDM Data Sections"

    def __str__(self):
        return f"{self.city_name}"
    
class CDMPage(models.Model):
    title = models.CharField(max_length=255)
    navbar = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=3)
    subnav = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=2,related_name="cdm_sub_nav")
    hero_sections = models.ForeignKey(HeroSection, on_delete=models.SET_NULL ,null=True,related_name='CDMPage')
    cdm_section = models.ForeignKey(CDMParentSection, on_delete=models.SET_NULL, null=True, blank=True, related_name="cdm_pages")
    promo_banner = models.ForeignKey(PromoBanner, on_delete=models.SET_NULL, null=True, blank=True)
    footer_section = models.ForeignKey(FooterSection,on_delete=models.CASCADE, related_name='CDMPage',default=1)   

    class Meta:
        verbose_name_plural = "CDM Pages"

    def __str__(self):
        return self.title

class GalleryMain(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Gallery Mains"

    def __str__(self):
        return self.title

class GalleryData(models.Model):
    main_gallery = models.ForeignKey(GalleryMain, on_delete=models.CASCADE, related_name="gallery_entries")
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='islamic_gallery/', null=True, blank=True)
    video = models.FileField(upload_to="aboutus_videos/", null=True, blank=True, help_text="Upload the video file.")

    class Meta:
        verbose_name_plural = "Gallery Data"

    def __str__(self):
        return f"{self.title}"

class GalleryPage(models.Model):
    title = models.CharField(max_length=255)
    navbar = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=3)
    subnav = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=2,related_name="gallery_sub_nav")
    hero_sections = models.ForeignKey(HeroSection, on_delete=models.SET_NULL ,null=True,related_name='GalleryPage')
    gallery_data = models.ForeignKey(GalleryMain, on_delete=models.SET_NULL, null=True, blank=True, related_name="gallery_page_entry")
    footer_section = models.ForeignKey(FooterSection,on_delete=models.CASCADE, related_name='GalleryPage',default=1)   

    class Meta:
        verbose_name_plural = "Gallery Pages"

    def __str__(self):
        return self.title

class IslamicRecurringDepositPage(models.Model):
    title = models.CharField(max_length=255)
    navbar = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=3)
    subnav = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=2,related_name="rec_sub_nav")
    hero_sections = models.ForeignKey(HeroSection, on_delete=models.SET_NULL ,null=True,related_name='IslamicRecurringDepositPage')
    tab_section = models.ManyToManyField(TabData, related_name='IslamicRecurringDepositPage') 
    promo_banner = models.ForeignKey(PromoBanner, on_delete=models.SET_NULL, null=True, blank=True)
    eligibility_docs = models.ManyToManyField(EligibilityDocTile, blank=True)
    faq_islamic_recurring = models.ManyToManyField(FAQItem, related_name='IslamicRecurringDepositPage')
    footer_section = models.ForeignKey(FooterSection,on_delete=models.CASCADE, related_name='IslamicRecurringDepositPage',default=1)   

    class Meta:
        verbose_name_plural = "Islamic Recurring Deposit Pages"

    def __str__(self):
        return self.title
    
class multirowpromo(models.Model):

    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Multi Row Promos"

    def __str__(self):
        return self.title


class multirowpromoItem(models.Model):
 
    section = models.ForeignKey(
        multirowpromo,
        on_delete=models.CASCADE,
        related_name="multirowpromo"
    )
    header = models.CharField(max_length=255,blank=True)
    description = RichTextField()

    class Meta:
        verbose_name_plural = "Multi Row Promo Items"

    def __str__(self):
        return self.header

class SupplyChainFinancePage(models.Model):
    title = models.CharField(max_length=255)
    navbar = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=3)
    subnav = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=2,related_name="sup_sub_nav")
    hero_sections = models.ForeignKey(HeroSection, on_delete=models.SET_NULL ,null=True,related_name='SupplyChainFinancePage')
    tab_section = models.ManyToManyField(TabData, related_name='SupplyChainFinancePage') 
    row_promo_1 = models.ForeignKey(multirowpromo, on_delete=models.SET_NULL, null=True, blank=True,related_name='row_promo_1')
    row_promo_2 = models.ForeignKey(multirowpromo, on_delete=models.SET_NULL, null=True, blank=True,related_name='row_promo_2')
    faq_islamic_recurring = models.ManyToManyField(FAQItem, related_name='SupplyChainFinancePage')
    footer_section = models.ForeignKey(FooterSection,on_delete=models.CASCADE, related_name='SupplyChainFinancePage',default=1)   

    class Meta:
        verbose_name_plural = "Supply Chain Finance Pages"

    def __str__(self):
        return self.title

class IslamicFAQSection(models.Model):
    title = models.CharField(max_length=200,blank=True)

    class Meta:
        verbose_name_plural = "Islamic FAQ Sections"

    def __str__(self):
        return self.title

class IslamicFAQItem(models.Model):
    faq_section = models.ForeignKey(IslamicFAQSection, related_name='islamic_faq_items', on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    top_description = RichTextField()
    mid_description = RichTextField()
    bottom_description = RichTextField()
    image = models.ImageField(upload_to='faq_islamic_images/')

    class Meta:
        verbose_name_plural = "Islamic FAQ Items"

    def __str__(self):
        return f"Q: {self.question}"

class WomenServicesPage(models.Model):
    title = models.CharField(max_length=255)
    navbar = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=3)
    subnav = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=2,related_name="wom_sub_nav")
    hero_sections = models.ForeignKey(HeroSection, on_delete=models.SET_NULL ,null=True,related_name='WomenServicesPage')
    faq_islamic = models.ManyToManyField(IslamicFAQItem, related_name='WomenServicesPage')
    promo_banner = models.ForeignKey(PromoBanner, on_delete=models.SET_NULL, null=True, blank=True)
    footer_section = models.ForeignKey(FooterSection,on_delete=models.CASCADE, related_name='WomenServicesPage',default=1)   

    class Meta:
        verbose_name_plural = "Women Services Pages"

    def __str__(self):
        return self.title

class NestedFAQSection(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Nested FAQ Sections"

    def __str__(self):
        return self.title

class FAQCategory(models.Model):
    nested_faq_section = models.ForeignKey(
        NestedFAQSection,
        related_name='faq_categories',
        on_delete=models.CASCADE
    )
    category_title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "FAQ Categories"

    def __str__(self):
        return self.category_title

class FAQQuestionAnswer(models.Model):
    category = models.ForeignKey(
        FAQCategory,
        related_name='faq_question_answers',
        on_delete=models.CASCADE
    )
    question = models.CharField(max_length=255)
    answer = models.TextField()

    class Meta:
        verbose_name_plural = "FAQ Question Answers"

    def __str__(self):
        return self.question

class TilePromoSection(models.Model):
    title = models.CharField(max_length=255)  # Title of the section

    class Meta:
        verbose_name_plural = "Tile Promo Sections"

    def __str__(self):
        return self.title

class TilePromoItem(models.Model):
    section = models.ForeignKey(
        TilePromoSection, 
        related_name="tile_promo_items", 
        on_delete=models.CASCADE
    )
    icon = models.ImageField(upload_to='tilepromo_icons/')  # Icon image
    icon_text = models.CharField(max_length=255)  # Text associated with the icon

    class Meta:
        verbose_name_plural = "Tile Promo Items"

    def __str__(self):
        return self.icon_text

class GreenPromoCTA(models.Model):
    title = models.CharField(max_length=255, help_text="Title of the section")
    description = RichTextField()
    addrss_bar = RichTextField(blank=True, null=True)
    cta1_text = models.CharField(max_length=100, blank=True, null=True, help_text="Text for the first call-to-action button")
    cta1_url = models.CharField(blank=True, null=True, help_text="URL for the first call-to-action button")
    cta2_text = models.CharField(max_length=100, blank=True, null=True, help_text="Text for the second call-to-action button")
    cta2_url = models.CharField(blank=True, null=True, help_text="URL for the second call-to-action button")

    class Meta:
        verbose_name_plural = "Green Promo CTAs"

    def __str__(self):
        return self.title

class AlfaBNPL(models.Model):
    title = models.CharField(max_length=255)
    navbar = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=3)
    subnav = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=2,related_name="bnpl_sub_nav")
    hero_sections = models.ForeignKey(HeroSection,null=True, blank=True, on_delete=models.SET_NULL ,related_name='AlfaBNPL')
    tab_section = models.ManyToManyField(TabData, related_name='AlfaBNPL') 
    green_cta_promo = models.ForeignKey(GreenPromoCTA, null=True, blank=True,on_delete=models.SET_NULL,related_name='AlfaBNPL')
    tile_promo = models.ForeignKey(TilePromoSection, on_delete=models.SET_NULL, null=True, blank=True)
    faq_islamic_nested = models.ForeignKey(NestedFAQSection,null=True, blank=True,on_delete=models.SET_NULL, related_name='AlfaBNPL')
    footer_section = models.ForeignKey(FooterSection,on_delete=models.CASCADE, related_name='AlfaBNPL',default=1)   

    class Meta:
        verbose_name_plural = "Alfa BNPLs"

    def __str__(self):
        return self.title

class FileNestedFAQSection(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "File Nested FAQ Sections"

    def __str__(self):
        return self.title

class FileFAQCategory(models.Model):
    nested_faq_section = models.ForeignKey(
        FileNestedFAQSection,
        related_name='file_faq_categories',
        on_delete=models.CASCADE
    )
    header = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "File FAQ Categories"

    def __str__(self):
        return self.header

class FileFAQQuestionAnswer(models.Model):
    category = models.ForeignKey(
        FileFAQCategory,
        related_name='file_faq_question_answers',
        on_delete=models.CASCADE
    )
    file_name = models.CharField(max_length=255)
    small_desc = models.CharField(max_length=255)
    file_cta_text = models.CharField(max_length=255)
    file_cta_url = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "File FAQ Question Answers"

    def __str__(self):
        return self.file_name

class AboutUsIslamic(models.Model):
    title = models.CharField(max_length=255)
    navbar = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=3)
    subnav = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=2,related_name="abt_us_sub_nav")
    hero_sections = models.ForeignKey(HeroSection,null=True, blank=True, on_delete=models.SET_NULL ,related_name='AboutUsIslamic')
    text_data = models.ForeignKey(ArticleSection, on_delete=models.SET_NULL ,null=True,related_name='AboutUsIslamic')
    image_text_promo = models.ManyToManyField(AccountFeature,related_name='AboutUsIslamic')
    
    file_faq_section = models.ForeignKey(FileNestedFAQSection, null=True, blank=True,on_delete=models.SET_NULL,related_name='AboutUsIslamic')
    green_cta_promo = models.ForeignKey(GreenPromoCTA, null=True, blank=True,on_delete=models.SET_NULL,related_name='AboutUsIslamic')

    promo_banner = models.ForeignKey(PromoBanner, on_delete=models.SET_NULL, null=True, blank=True)
    footer_section = models.ForeignKey(FooterSection,on_delete=models.CASCADE, related_name='AboutUsIslamic',default=1)   

    class Meta:
        verbose_name_plural = "About Us Islamic"

    def __str__(self):
        return self.title



from dbg.models import TextFullDBG,OrbitPromo,TextColDBG
from premier_core.models import GoldenPromoCTAEntry

class IslamicMisc(models.Model):
    title = models.CharField(max_length=255)
    navbar = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=3)
    subnav = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=2,related_name="misc_sub_nav")
    hero_sections = models.ForeignKey(HeroSection,null=True, blank=True, on_delete=models.SET_NULL ,related_name='islamic_misc')
    isl_full_text = models.ForeignKey(TextFullDBG, on_delete=models.SET_NULL ,null=True,blank=True,related_name='isl_full_text')
    isl_table_1 = models.ForeignKey(TablePromo, on_delete=models.SET_NULL, null=True,blank=True, related_name='isl_table_1')
    isl_table_2 = models.ForeignKey(TablePromo, on_delete=models.SET_NULL, null=True,blank=True, related_name='isl_table_2')
    isl_full_text_2 = models.ForeignKey(TextFullDBG, on_delete=models.SET_NULL ,null=True,blank=True,related_name='isl_full_text_2')
    isl_full_text_3 = models.ForeignKey(TextFullDBG, on_delete=models.SET_NULL ,null=True,blank=True,related_name='isl_full_text_3')
    isl_full_text_4 = models.ForeignKey(TextFullDBG, on_delete=models.SET_NULL ,null=True,blank=True,related_name='isl_full_text_4')
    isl_col_text = models.ForeignKey(TextColDBG, on_delete=models.SET_NULL ,null=True,blank=True,related_name='isl_col_text')
    isl_col_text_2 = models.ForeignKey(TextColDBG, on_delete=models.SET_NULL ,null=True,blank=True,related_name='isl_col_text_2')
    isl_faq = models.ForeignKey(FAQSection,on_delete=models.SET_NULL,null=True,blank=True, related_name='isl_faq')
    isl_promo_orbit = models.ForeignKey(OrbitPromo, on_delete=models.SET_NULL, null=True,blank=True, related_name='isl_orbit_rewards')
    isl_zigzag = models.ManyToManyField(AccountFeature,blank=True,related_name='isl_zigzag')
    green_cta_promo = models.ForeignKey(GoldenPromoCTAEntry, null=True, blank=True,on_delete=models.SET_NULL,related_name='green_cta_promo')
    footer_section = models.ForeignKey(FooterSection,on_delete=models.CASCADE, related_name='misc_footer',default=1)   

    class Meta:
        verbose_name_plural = "Islamic Misc"

    def __str__(self):
        return self.title
