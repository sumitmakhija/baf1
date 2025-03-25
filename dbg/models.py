from django.db import models
from core.models import *
from islamic_core.models import *
from premier_core.models import *
# Create your models here.

class KeyFactsSection(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='key_facts_images/', blank=True, null=True)
    cta_text = models.CharField(max_length=100, blank=True, null=True)
    cta_link = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Key Facts Sections"

    def __str__(self):
        return self.title

class DBGAllText(models.Model):
    show_title = models.BooleanField(default=False)
    title = models.CharField(max_length=255,null=True,blank=True)
    description = RichTextField()

    class Meta:
        verbose_name_plural = "DBG All Texts"

    def __str__(self):
        return self.title
    
class DBGVideoSection(models.Model):
    heading = models.CharField(max_length=255)
    video = models.FileField(upload_to="videos/", help_text="Upload the video file.")

    class Meta:
        verbose_name_plural = "DBG Video Sections"

    def __str__(self):
        return self.heading
    
class ProductTextDBG(models.Model):
    heading = models.CharField(max_length=255)
    description = RichTextField()

    class Meta:
        verbose_name_plural = "Product Text DBGs"

    def __str__(self):
        return self.heading
    
class TextFullDBG(models.Model):
    heading = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Text Full DBGs"

    def __str__(self):
        return self.heading
    
class TextFullDBGEntry(models.Model):
    text_full_dbg = models.ForeignKey(
        TextFullDBG,
        on_delete=models.CASCADE,
        related_name="dbg_full_entries",
    )
    main_heading = models.CharField(max_length=255)
    main_description = RichTextField()

    class Meta:
        verbose_name_plural = "Text Full DBG Entries"

    def __str__(self):
        return f"{self.main_heading} - {self.main_description}"
    
class TextColDBG(models.Model):
    heading = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Text Col DBGs"

    def __str__(self):
        return self.heading

class TextColDBGEntry(models.Model):
    text_full_dbg = models.ForeignKey(
        TextColDBG,
        on_delete=models.CASCADE,
        related_name="dbg_col_entries",
    )
    main_heading_column1 = models.CharField(max_length=255, blank=True, null=True)
    main_description_column1 = RichTextField(blank=True, null=True)
    main_heading_column2 = models.CharField(max_length=255, blank=True, null=True)
    main_description_column2 = RichTextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Text Col DBG Entries"

    def __str__(self):
        return f"Column 1: {self.main_heading_column1}, Column 2: {self.main_heading_column2}"

class SupportServices(models.Model):
    heading = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Support Services"

    def __str__(self):
        return self.heading

class SupportServicesEntry(models.Model):
    support_service = models.ForeignKey(
        SupportServices,
        on_delete=models.CASCADE,
        related_name="service_entries",
    )
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="support_service_logos/", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Support Services Entries"

    def __str__(self):
        return f"{self.name}"

class BoxPromo(models.Model):
    heading = models.CharField(max_length=255)
    description = RichTextField()

    class Meta:
        verbose_name_plural = "Box Promos"

    def __str__(self):
        return self.heading

class BoxPromoEntry(models.Model):
    box_promo = models.ForeignKey(
        BoxPromo,
        on_delete=models.CASCADE,
        related_name="service_entries",
    )
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="dbg_box_promo_logos/", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Box Promo Entries"

    def __str__(self):
        return f"{self.name}"
    
class FeaturesBox(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Features Boxes"
  
    def __str__(self):
        return self.title

class FeaturesBoxEntry(models.Model):
    features_box = models.ForeignKey(
        FeaturesBox,
        on_delete=models.CASCADE,
        related_name="features_box_entries",
    )
    title = models.CharField(max_length=255)
    description = RichTextField()

    class Meta:
        verbose_name_plural = "Features Box Entries"

    def __str__(self):
        return f"{self.title}"
    
class DBGAccount(models.Model):
    TYPE_CHOICES = [
        ('Convetional', 'Convetional'),
        ('Islamic', 'Islamic'),
        ('RDA','RDA')
    ]
    type = models.CharField(max_length=40, choices=TYPE_CHOICES)
    image = models.ImageField(upload_to='dbg_account_tabs_images/', blank=True, null=True)

    cards = models.ManyToManyField(Card, related_name='dbg_account_types')

    class Meta:
        verbose_name_plural = "DBG Accounts"
    
    def __str__(self):
        return self.get_type_display()

class DBGAccountSection(models.Model):
    title = models.CharField(max_length=255, help_text="Main title for the section")
    secondary_title = models.CharField(max_length=255)
    account_types = models.ManyToManyField(DBGAccount, related_name='dbg_accounts')

    class Meta:
        verbose_name_plural = "DBG Account Sections"
    
    def __str__(self):
        return self.title

class DBGCard(models.Model):
    tag = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    cta_text = models.CharField(max_length=50, blank=True, null=True)
    cta_link = models.CharField(max_length=200, blank=True, null=True)
    cta_text_2 = models.CharField(max_length=50, blank=True, null=True)
    cta_link_2 = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='dbg_account_card_images/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "DBG Cards"
    
    def __str__(self):
        return f"{self.title} ({self.tag})"

class DBGPages(models.Model):
    title = models.CharField(max_length=255)
    navbar = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=1)

    hero_sections = models.ForeignKey(HeroSection, on_delete=models.SET_NULL ,null=True,related_name='dbg_hero')
    dbg_zigzag = models.ManyToManyField(AccountFeature,blank=True,related_name='dbg_zigzag')
    dbg_faq = models.ForeignKey(FAQSection,on_delete=models.SET_NULL,null=True,blank=True, related_name='dbg_faq')
    dbg_faq_2 = models.ForeignKey(FAQSection,on_delete=models.SET_NULL,null=True,blank=True, related_name='dbg_faq_2')
    key_facts = models.ForeignKey(KeyFactsSection, on_delete=models.SET_NULL, null=True,default=1, blank=True, related_name='dbg_key_facts')
    subnav = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=1,related_name='dbg_subnav')
    
    dbg_text_section = models.ForeignKey(DBGAllText,on_delete=models.SET_NULL,null=True,blank=True, related_name='dbg_text')
    dbg_reports_promo = models.ForeignKey(ReportsTabSection, on_delete=models.SET_NULL ,null=True,blank=True,related_name='dbg_reports')
    dbg_file_faq_section = models.ForeignKey(FileNestedFAQSection, null=True, blank=True,on_delete=models.SET_NULL,related_name='dbg_file_section')
    dbg_table_1 = models.ForeignKey(TablePromo, on_delete=models.SET_NULL, null=True,blank=True, related_name='dbg_table_1')
    dbg_table_2 = models.ForeignKey(TablePromo, on_delete=models.SET_NULL, null=True,blank=True, related_name='dbg_table_2')
    dbg_table_3 = models.ForeignKey(TablePromo, on_delete=models.SET_NULL, null=True,blank=True, related_name='dbg_table_3')
    dbg_table_4 = models.ForeignKey(TablePromo, on_delete=models.SET_NULL, null=True,blank=True, related_name='dbg_table_4')
    dbg_table_5 = models.ForeignKey(TablePromo, on_delete=models.SET_NULL, null=True,blank=True, related_name='dbg_table_5')

    services_promo_1 = models.ForeignKey(SupportServices, on_delete=models.SET_NULL, null=True,blank=True, related_name='dbg_service_1')
    services_promo_2 = models.ForeignKey(SupportServices, on_delete=models.SET_NULL, null=True,blank=True, related_name='dbg_service_2')
    services_promo_3 = models.ForeignKey(SupportServices, on_delete=models.SET_NULL, null=True,blank=True, related_name='dbg_service_3')
    services_promo_4 = models.ForeignKey(SupportServices, on_delete=models.SET_NULL, null=True,blank=True, related_name='dbg_service_4')
    services_promo_5 = models.ForeignKey(SupportServices, on_delete=models.SET_NULL, null=True,blank=True, related_name='dbg_service_5')
    services_promo_6 = models.ForeignKey(SupportServices, on_delete=models.SET_NULL, null=True,blank=True, related_name='dbg_service_6')

    red_promo = models.ForeignKey(GoldenPromoCTAEntry, null=True, blank=True,on_delete=models.SET_NULL,related_name='dbg_red_promo')
    red_promo_2 = models.ForeignKey(GoldenPromoCTAEntry, null=True, blank=True,on_delete=models.SET_NULL,related_name='dbg_red_promo_2')
    red_promo_3 = models.ForeignKey(GoldenPromoCTAEntry, null=True, blank=True,on_delete=models.SET_NULL,related_name='dbg_red_promo_3')

    dbg_cards = models.ForeignKey(CardPromoSection, on_delete=models.SET_NULL ,null=True,blank=True,related_name='dbg_cards')
    promo_banner = models.ForeignKey(PromoBanner, on_delete=models.SET_NULL, null=True, blank=True)
    promo_banner_full = models.ForeignKey(PromoBannerFull, on_delete=models.SET_NULL, null=True, blank=True)

    dbg_accounts = models.ForeignKey(AccountSection, on_delete=models.SET_NULL ,null=True,blank=True,related_name='dbg_accounts')
    dbg_video = models.ForeignKey(DBGVideoSection, on_delete=models.SET_NULL, null=True,blank=True, related_name='dbg_video')
    dbg_promo_orbit = models.ForeignKey(OrbitPromo, on_delete=models.SET_NULL, null=True,blank=True, related_name='dbg_orbit_rewards')
    dbg_faq_nested = models.ForeignKey(NestedFAQPremier,null=True, blank=True,on_delete=models.SET_NULL, related_name='dbg_faq_nested')
    dbg_full_text = models.ForeignKey(TextFullDBG, on_delete=models.SET_NULL ,null=True,blank=True,related_name='dbg_full_text')
    dbg_full_text_2 = models.ForeignKey(TextFullDBG, on_delete=models.SET_NULL ,null=True,blank=True,related_name='dbg_full_text_2')

    dbg_col_text = models.ForeignKey(TextColDBG, on_delete=models.SET_NULL ,null=True,blank=True,related_name='dbg_col_text')
    dbg_col_text_2 = models.ForeignKey(TextColDBG, on_delete=models.SET_NULL ,null=True,blank=True,related_name='dbg_col_text_2')
    dbg_col_text_3 = models.ForeignKey(TextColDBG, on_delete=models.SET_NULL ,null=True,blank=True,related_name='dbg_col_text_3')

    dbg_product_text = models.ForeignKey(ProductTextDBG, on_delete=models.SET_NULL ,null=True,blank=True,related_name='dbg_product_text')

    dbg_services = models.ForeignKey(SupportServices, on_delete=models.SET_NULL ,null=True,blank=True,related_name='dbg_services')
    dbg_box_promo = models.ForeignKey(BoxPromo, on_delete=models.SET_NULL ,null=True,blank=True,related_name='dbg_box')
    dbg_box_promo_2 = models.ForeignKey(BoxPromo, on_delete=models.SET_NULL ,null=True,blank=True,related_name='dbg_box_2')
    dbg_box_promo_3 = models.ForeignKey(BoxPromo, on_delete=models.SET_NULL ,null=True,blank=True, related_name='dbg_box_3')

    dbg_tips = models.ForeignKey(SupportServices, on_delete=models.SET_NULL ,null=True,blank=True,related_name='dbg_tips')
    dbg_features = models.ForeignKey(FeaturesBox, on_delete=models.SET_NULL ,null=True,blank=True,related_name='dbg_features')
    dbg_accounts_promo_all = models.ForeignKey(DBGAccountSection, on_delete=models.SET_NULL ,null=True,blank=True,related_name='DBG_Account')

    footer_section = models.ForeignKey(FooterSection,on_delete=models.CASCADE, related_name='dbg_footer',default=2) 

    class Meta:
        verbose_name_plural = "DBG Pages"

    def __str__(self):
        return self.title