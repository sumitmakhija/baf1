# models.py

from django.db import models
from ckeditor.fields import RichTextField
import os
from django.utils.html import strip_tags
# Homepage Sections Models Start
class NavbarMainItem(models.Model):
    name = models.CharField(max_length=255, help_text="Main navigation item")
    TYPE_CHOICES = [
        ('Conventional', 'Conventional'),
        ('Islamic', 'Islamic'),
        ('Premier', 'Premier'),
        
    ]
    nav_type = models.CharField(max_length=255,choices=TYPE_CHOICES,default="Conventional")
    nav_bg = models.ImageField(upload_to='navbar-bg/', null=True, blank=True, help_text="Background image for the main item")
    url_text = models.CharField(blank=True, null=True)
    url = models.CharField(blank=True, null=True, help_text="Optional URL for the main item")
    order = models.PositiveIntegerField(default=0, help_text="Order of the main item")
    is_active = models.BooleanField(default=True, help_text="Whether to display this item")

    class Meta:
        verbose_name_plural = "Navbar Main Items"
        ordering = ['order']

    def __str__(self):
        return self.name + " (" + self.nav_type + ")"


class NavbarSubTab(models.Model):
    main_item = models.ForeignKey(
        NavbarMainItem,
        related_name='sub_tabs',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255, help_text="Tab name under the main item")
    url = models.CharField(blank=True, null=True, help_text="Optional URL for the sub-tab")
    order = models.PositiveIntegerField(default=0, help_text="Order of the sub-tab")
    is_active = models.BooleanField(default=True, help_text="Whether to display this tab")

    class Meta:
        verbose_name_plural = "Navbar Sub Tabs"
        ordering = ['order']

    def __str__(self):
        return self.name


class NavbarContentLink(models.Model):
    sub_tab = models.ForeignKey(
        NavbarSubTab,
        related_name='links',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255, help_text="Link name")
    url = models.CharField(help_text="Link URL")
    is_active = models.BooleanField(default=True, help_text="Whether to display this link")

    class Meta:
        verbose_name_plural = "Navbar Content Links"

    def __str__(self):
        return self.name

class NavigationMain(models.Model):
    title = models.CharField(max_length=255)
    navbar = models.ManyToManyField(NavbarMainItem, blank=True)
    logo = models.ImageField(upload_to='navbar-logos/', null=True, blank=True, help_text="Logo to be displayed in the navbar")
    title1 = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Navigation Main"

    def __str__(self):
        return self.title


class FooterSection(models.Model):
    title = models.CharField(max_length=255)
    footer_logo = models.ImageField(upload_to='footer-logos/')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Footer Sections"

class FooterLink(models.Model):
    section = models.ForeignKey(FooterSection, related_name='links', on_delete=models.CASCADE)
    link_text = models.CharField(max_length=255)
    link_url = models.CharField(max_length=200)

    def __str__(self):
        return self.link_text

    class Meta:
        verbose_name_plural = "Footer Links"

class HeroSection(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='hero-images/')
    description = RichTextField(config_name='default',blank=True)
    cta_text = models.CharField(max_length=50, blank=True, null=True)
    cta_link = models.CharField(max_length=150, blank=True, null=True)
    show_app_buttons = models.BooleanField(default=False)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Hero Sections"

class HeroSliderImage(models.Model):
    image = models.ImageField(upload_to='hero-slider-images/',null=True,blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    cta_text = models.CharField(max_length=50, blank=True, null=True)
    cta_link = models.CharField(max_length=150, blank=True, null=True)
    order = models.PositiveIntegerField(default=0, help_text="Order of the slide")
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Hero Slider Images"
        ordering = ['order']

class HeroSectionSlider(models.Model):
    title = models.CharField(max_length=100)
    slides = models.ManyToManyField(HeroSliderImage, related_name='sliders')

    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Hero Section Sliders"


class AccountPromo(models.Model):
    main_heading = models.CharField(max_length=255)
    description = RichTextField()
    features_heading = models.CharField(max_length=255)
    features = models.TextField(help_text="Enter each feature on a new line.")
    image = models.ImageField(upload_to='account-promo-img/')
    cta_text = models.CharField(max_length=255, help_text="Text for the call-to-action button.")
    cta_url = models.CharField(max_length=255,help_text="URL for the call-to-action button.")

    def get_features_list(self):
        return self.features.splitlines()

    def __str__(self):
        return self.main_heading

    class Meta:
        verbose_name_plural = "Account Promos"

class NewsUpdate(models.Model):
    heading = models.CharField(max_length=255)
    image = models.ImageField(upload_to='news-update-imgs/')
    headline = models.CharField(max_length=255)
    description = models.TextField()
    cta_text = models.CharField(max_length=100)  # CTA stands for Call To Action
    cta_link = models.CharField(max_length=255)

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name_plural = "News Updates"

class OfferImage(models.Model):
    image = models.ImageField(upload_to='offers-promo-images/')

    def __str__(self):
        return os.path.basename(self.image.name)

    class Meta:
        verbose_name_plural = "Offer Images"

class OffersPromo(models.Model):
    title = models.CharField(max_length=255,blank=True)
    header = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    cta_text = models.CharField(max_length=100,blank=True)
    link = models.CharField(max_length=250,blank=True)
    images = models.ManyToManyField(OfferImage, related_name='offers_promos')

    def __str__(self):
        return self.link

    class Meta:
        verbose_name_plural = "Offers Promos"

class FinancialSolutionPromo(models.Model):
    main_heading = models.CharField(max_length=255,blank=True)
    card_title = models.CharField(max_length=255,blank=True)
    card_header = models.CharField(max_length=255)
    card_description = models.TextField()
    card_image = models.ImageField(upload_to='financial-solution-promo-images/')
    cta_text = models.CharField(max_length=100)
    cta_link =  models.CharField(max_length=255)

    def __str__(self):
        return self.card_header if self.card_header else "No Header"

    class Meta:
        verbose_name_plural = "Financial Solution Promos"

class PromoBanner(models.Model):
    banner_text = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='promo-banner-images/')
    cta1_link = models.CharField(max_length=255)
    cta1_image = models.ImageField(upload_to='cta-images/')
    cta2_link = models.CharField(max_length=255)
    cta2_image = models.ImageField(upload_to='cta-images/')

    def __str__(self):
        return self.banner_text

    class Meta:
        verbose_name_plural = "Promo Banners"

class BankingPromo(models.Model):
    PROMO_CHOICES = [
        ('premier', 'Premier'),
        ('islamic', 'Islamic'),
        ('corporate', 'Corporate'),
    ]

    promo_type = models.CharField(max_length=20, choices=PROMO_CHOICES, default='Corporate')
    title = models.CharField(max_length=255)
    description = models.TextField()
    cta_text = models.CharField(max_length=50)
    cta_link = models.CharField(max_length=255)
    image = models.ImageField(upload_to='banking-promo-images/')

    def __str__(self):
        return f"{self.title} ({self.promo_type})"

    class Meta:
        verbose_name_plural = "Banking Promos"

# Model for Account Types
class Account(models.Model):
    TYPE_CHOICES = [
        ('Current Account', 'Current Account'),
        ('Saving Account', 'Saving Account'),
        ('Digital Accounts', 'Digital Accounts'),
        ('Fixed Deposit Account', 'Fixed Deposit Account'),
        ('Islamic Current Account', 'Islamic Current Account'),
        ('Islamic Saving Account', 'Islamic Saving Account'),
        ('Islamic Term Deposits', 'Islamic Term Deposits'),
        ('Islamic Installment Based Term Deposits', 'Islamic Installment Based Term Deposits'),
    ]

    type = models.CharField(max_length=40, choices=TYPE_CHOICES)
    image = models.ImageField(upload_to='account_tabs_images/', blank=True, null=True)
    cards = models.ManyToManyField('Card', related_name='account_types',default='Current Account')


    def __str__(self):
        return self.get_type_display()

    class Meta:
        verbose_name_plural = "Accounts"

# Model for Cards
class Card(models.Model):
    tag = models.CharField(max_length=50,blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    cta_text = models.CharField(max_length=50, blank=True, null=True)
    cta_link = models.CharField(max_length=200, blank=True, null=True)
    cta_text_2 = models.CharField(max_length=50, blank=True, null=True)
    cta_link_2 = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='account_card_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.tag})"

    class Meta:
        verbose_name_plural = "Cards"

# Model for Accounts
class AccountSection(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    account_types = models.ManyToManyField(Account, related_name='accounts')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Account Sections"

class FAQSection(models.Model):
    title = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.title if self.title else "No Title"

    class Meta:
        verbose_name_plural = "FAQ Sections"

class FAQItem(models.Model):
    faq_section = models.ForeignKey(FAQSection, related_name='faq_items', on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    answer = RichTextField()

    def __str__(self):
        return f"Q: {self.question} - A: {self.answer[:50]}..." 

    class Meta:
        verbose_name_plural = "FAQ Items"

class AccountFeaturesPromo(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Account Features Promos"

class AccountFeature(models.Model):
    ORIENTATION_CHOICES = [
        ('left', 'Left'),
        ('right', 'Right'),
    ]

    promo_section = models.ForeignKey(AccountFeaturesPromo, related_name='features', on_delete=models.CASCADE)
    title = RichTextField(max_length=200)
    description = RichTextField(help_text="Format as an unstyled list with check circle outlines by using the classes: 'list-unstyled list-check-circle-outline mt-4' on a ul element.")
    image = models.ImageField(upload_to='account_features_promo_images/')
    image_orientation = models.CharField(max_length=10, choices=ORIENTATION_CHOICES)

    class Meta:
        verbose_name_plural = "Account Features"
        ordering = ['id']  # This ensures the instances are ordered by creation (based on ID)

    def __str__(self):
        return strip_tags(f'{self.title} ({self.promo_section.title})')

class EligibilityDocsSection(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Eligibility Docs Sections"

class EligibilityDocTile(models.Model):
    section = models.ForeignKey(EligibilityDocsSection, related_name='tiles', on_delete=models.CASCADE)
    tile_title = models.CharField(max_length=255)
    tile_image = models.ImageField(upload_to='eligibility_doc_tiles/', blank=True, null=True)
    def __str__(self):
        section_description = strip_tags(self.section.description)
        return f"{section_description} ({self.tile_title})"

    class Meta:
        verbose_name_plural = "Eligibility Doc Tiles"

class PromoBannerFull(models.Model):
    banner_text = models.CharField(max_length=255)
    description = RichTextField()
    cta_link = models.CharField(max_length=255)
    cta_text = models.CharField(max_length=255)
    image = models.ImageField(upload_to='promo_banner_full_img/', blank=True, null=True)


    def __str__(self):
        return self.banner_text

    class Meta:
        verbose_name_plural = "Promo Banners Full"

class Homepage(models.Model):
    title = models.CharField(max_length=255)
    navbar = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True)
    subnav = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=2,related_name="sub_nav")
    hero_slider_sections = models.ManyToManyField(HeroSectionSlider, related_name='homepages', blank=True)
    account_promo = models.ForeignKey(AccountPromo, on_delete=models.SET_NULL, null=True, blank=True)
    news_updates = models.ManyToManyField(NewsUpdate, related_name='homepages')
    offers_promo = models.ForeignKey(OffersPromo, on_delete=models.SET_NULL, null=True, blank=True)  
    financial_solution_promo = models.ManyToManyField(FinancialSolutionPromo, related_name='homepages', blank=True)
    promo_banner = models.ForeignKey(PromoBanner, on_delete=models.SET_NULL, null=True, blank=True)
    banking_promo = models.ManyToManyField(BankingPromo, related_name='homepages', blank=True)      
    footer_section = models.ForeignKey(FooterSection, on_delete=models.CASCADE, related_name='homepages', default=2)  # Corrected ForeignKey field
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Homepages"

class AccountsPage(models.Model):
    title = models.CharField(max_length=255)
    subnav = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=2,related_name="acc_sub_nav")
    navbar = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=1)
    hero_sections = models.ForeignKey(HeroSection, on_delete=models.SET_NULL ,null=True,related_name='Account')
    accounts_promo_all = models.ForeignKey(AccountSection, on_delete=models.SET_NULL ,null=True,related_name='Account')
    faq = models.ManyToManyField('FAQItem', related_name='account_types',blank=True)
    footer_section = models.ForeignKey(FooterSection,on_delete=models.CASCADE, related_name='Account',default=2)   
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Accounts Pages"

class AccountDetails(models.Model):
    title = models.CharField(max_length=255)
    subnav = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=2,related_name="acc_details_sub_nav")
    navbar = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=1)
    hero_sections = models.ForeignKey(HeroSection, on_delete=models.SET_NULL ,null=True,default=1,related_name='AccountDetails')
    account_features = models.ManyToManyField('AccountFeature',related_name='AccountDetail')
    promo_banner = models.ForeignKey(PromoBanner, on_delete=models.SET_NULL, null=True, blank=True)
    eligibility_docs = models.ManyToManyField('EligibilityDocTile')
    promo_banner_full = models.ForeignKey(PromoBannerFull, on_delete=models.SET_NULL, null=True, blank=True)
    footer_section = models.ForeignKey(FooterSection,on_delete=models.CASCADE, related_name='AccountDetail',default=2)   

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Account Details"

class RedBoxPromo(models.Model):
    title = models.CharField(max_length=255)  # To name the entire promo set

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Red Box Promos"

class RedBoxPromoEntry(models.Model):
    red_box_promo = models.ForeignKey(RedBoxPromo, related_name='entries', on_delete=models.CASCADE)  # Related to RedBoxPromo
    icon = models.ImageField(upload_to='red_box_icons/',blank=True)  # To upload icon images
    title = models.CharField(max_length=255)
    description = models.TextField()
    cta_text = models.CharField(max_length=100, verbose_name='CTA Text')  # Call to action text
    cta_url = models.CharField(max_length=255,verbose_name='CTA URL')  # Call to action URL

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Red Box Promo Entries"

class Careers(models.Model):
    title = models.CharField(max_length=255)
    navbar = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=1)
    subnav = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=2,related_name="careers_sub_nav")
    hero_sections = models.ForeignKey(HeroSection, on_delete=models.SET_NULL ,null=True,related_name='Careers')
    careers_features = models.ManyToManyField('AccountFeature',related_name='Career')
    red_box_promo = models.ForeignKey(RedBoxPromo, on_delete=models.SET_NULL, null=True, related_name='careers')  # Associate one RedBoxPromo
    management_promo = models.ForeignKey(OffersPromo, on_delete=models.SET_NULL, null=True, blank=True)
    footer_section = models.ForeignKey(FooterSection,on_delete=models.CASCADE, related_name='Career',default=2)   


    class Meta:
        verbose_name = 'Careers'  
        verbose_name_plural = "Careers"

class ModalPromo(models.Model):
    header = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = RichTextField()
    person_name = models.CharField(max_length=255)
    cta_text = models.CharField(max_length=100)
    cta_link = models.CharField(max_length=100)
    image_1 = models.ImageField(upload_to='modal_promo_images/')
    image_2 = models.ImageField(upload_to='modal_promo_images/')

    def __str__(self):
        return f"{self.header} - {self.title} (By {self.person_name})"

    class Meta:
        verbose_name_plural = "Modal Promos"

class VisionMissionPromo(models.Model):
    promo_title = models.CharField(max_length=255, help_text="Title of the promo section")

    def __str__(self):
        return self.promo_title

    class Meta:
        verbose_name_plural = "Vision Mission Promos"

class VisionMissionEntry(models.Model):
    promo = models.ForeignKey(VisionMissionPromo, related_name='entries', on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='vision_mission_logos/',blank=True)
    header = models.CharField(max_length=255)
    description = RichTextField()

    def __str__(self):
        return self.header

    class Meta:
        verbose_name_plural = "Vision Mission Entries"

class AboutUs(models.Model):
    title = models.CharField(max_length=255)
    navbar = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=1)
    subnav = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=2,related_name="about_us_sub_nav")
    hero_sections = models.ForeignKey(HeroSection, on_delete=models.SET_NULL ,null=True,related_name='about_us')
    aboutus_features = models.ManyToManyField('AccountFeature',related_name='about_us')
    modal_promo = models.ForeignKey(ModalPromo, on_delete=models.SET_NULL, null=True, related_name='about_us') 
    vision_mission_promo = models.ForeignKey(VisionMissionPromo, on_delete=models.SET_NULL, null=True, related_name='about_us')
    footer_section = models.ForeignKey(FooterSection,on_delete=models.CASCADE, related_name='about_us',default=2)   

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "About Us"

class AwardsPage(models.Model):
    title = models.CharField(max_length=255)
    navbar = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=1)
    hero_sections = models.ForeignKey(HeroSection, on_delete=models.SET_NULL ,null=True,related_name='awards')
    awards_promo = models.ManyToManyField('FAQItem', related_name='awards')
    footer_section = models.ForeignKey(FooterSection, on_delete=models.CASCADE, related_name='awards', default=2)  # Corrected ForeignKey field

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Awards Pages"

class HRMessage(models.Model):
    hrpicture = models.ImageField(upload_to='hr_pictures/')
    hrmessage = models.TextField()  
    hrname = models.CharField(max_length=255)
    hrdesignation = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.hrname} - {self.hrdesignation}"

    class Meta:
        verbose_name_plural = "HR Messages"

class CareersOpportunityPage(models.Model):
    title = models.CharField(max_length=255)
    navbar = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=1)
    subnav = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=2,related_name="careers_ops_sub_nav")
    hero_sections = models.ForeignKey(HeroSection, on_delete=models.SET_NULL ,null=True,related_name='careers_ops')
    programs = models.ManyToManyField(FinancialSolutionPromo, related_name='careers_ops', blank=True)
    hr_promo = models.ForeignKey(HRMessage, on_delete=models.CASCADE, related_name='careers_ops')  # Corrected ForeignKey field
    footer_section = models.ForeignKey(FooterSection, on_delete=models.CASCADE, related_name='careers_ops', default=2)  # Corrected ForeignKey field

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Careers Opportunity Pages"

class JobsPage(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField()  # You can use CharField if not rich text is needed


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Jobs Pages"

class Jobs(models.Model):
    job_section = models.ForeignKey('JobsPage', on_delete=models.CASCADE, related_name='jobs')  # ForeignKey to JobsSection
    job_title = RichTextField() 
    job_description = RichTextField()  # RichTextField allows formatted text
    cta_text = models.CharField(max_length=100)
    cta_link = models.CharField(max_length=200)

    def __str__(self):
        return self.job_title

    class Meta:
        verbose_name_plural = "Jobs"

class JobsLP(models.Model):
    title = models.CharField(max_length=255)
    navbar = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=1)
    subnav = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=2,related_name="jobs_lp_sub_nav")
    hero_sections = models.ForeignKey(HeroSection, on_delete=models.SET_NULL ,null=True,related_name='jobs_lp')
    jobs = models.ForeignKey(JobsPage, on_delete=models.CASCADE,related_name='jobs_lp', blank=True)
    footer_section = models.ForeignKey(FooterSection, on_delete=models.CASCADE, related_name='jobs_lp', default=2)  # Corrected ForeignKey field

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Jobs LPs"

class FinancialReportsCard(models.Model):
    year = models.CharField(max_length=10,null=True,blank=True)
    header = models.CharField(max_length=255,null=True,blank=True)
    title = models.CharField(max_length=255)
    description = RichTextField(null=True,blank=True) 
    date = models.CharField(max_length=255,null=True,blank=True)
    cta_link = models.CharField(max_length=200, null=True,blank=True)
    image = models.ImageField(upload_to='finanical_reports_ceo_images/', null=True,blank=True)

    def __str__(self):
        return f"{self.title} ({self.year})"

    class Meta:
        verbose_name_plural = "Financial Reports Cards"

class FinancialReports(models.Model):
    TYPE_CHOICES = [
        ('Annual Reports', 'Annual Reports'),
        ('Analyst Briefing', 'Analyst Briefing'),
        ('Capital Adequacy Ratio', 'Capital Adequacy Ratio'),
        ('CEO Review', 'CEO Review'),
        ('Best Corporate Report', 'Best Corporate Report'),
        ('Credit Rating', 'Credit Rating'),
        ('Material Information', 'Material Information'),
        ('Unclaimed Deposits', 'Unclaimed Deposits'),
        ('Other', 'Other'),
    ]

    type = models.CharField(max_length=40, choices=TYPE_CHOICES)
    cards_reports = models.ManyToManyField('FinancialReportsCard', related_name='report_types',default='Annual Reports')

    def __str__(self):
        return self.get_type_display()

    class Meta:
        verbose_name_plural = "Financial Reports"

class ReportsTabSection(models.Model):
    title = models.CharField(max_length=255)
    report_types = models.ManyToManyField(FinancialReports, related_name='reports')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Reports Tab Sections"

class FinancialReportsPage(models.Model):
    title = models.CharField(max_length=255)
    navbar = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=1)
    subnav = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=2,related_name="financial_reports_sub_nav")
    hero_sections = models.ForeignKey(HeroSection, on_delete=models.SET_NULL ,null=True,related_name='financial_reports')
    reports_promo = models.ForeignKey(ReportsTabSection, on_delete=models.SET_NULL ,null=True,related_name='financial_reports')
    footer_section = models.ForeignKey(FooterSection,on_delete=models.CASCADE, related_name='financial_reports',default=2)   

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Financial Reports Pages"

class ElectionDirectorsPage(models.Model):
    title = models.CharField(max_length=255)
    navbar = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=1)
    subnav = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=2,related_name="election_directors_sub_nav")
    hero_sections = models.ForeignKey(HeroSection, on_delete=models.SET_NULL ,null=True,related_name='election_directors')
    election_promo = models.ForeignKey(ReportsTabSection, on_delete=models.SET_NULL ,null=True,related_name='election_directors')
    footer_section = models.ForeignKey(FooterSection,on_delete=models.CASCADE, related_name='election_directors',default=2)   

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Election Directors Pages"

class BranchPage(models.Model):
    title = models.CharField(max_length=255)
    navbar = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=1)
    subnav = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=2,related_name="branch_sub_nav")
    hero_sections = models.ForeignKey(HeroSection, on_delete=models.SET_NULL ,null=True,related_name='BranchPage')
    footer_section = models.ForeignKey(FooterSection,on_delete=models.CASCADE, related_name='branch',default=2)   

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Branch Pages"

class ArticleSection(models.Model):
    show_title = models.BooleanField(default=True)
    title = models.CharField(max_length=255)
    description_before = RichTextField()
    image = models.ImageField(upload_to='articles/', null=True,blank=True)
    description_after = RichTextField(blank=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Article Sections"

class ArticlePage(models.Model):
    title = models.CharField(max_length=255)
    navbar = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=1)
    subnav = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=2,related_name="article_sub_nav")
    hero_sections = models.ForeignKey(HeroSection, on_delete=models.SET_NULL ,null=True,related_name='ArticlePage')
    article_section = models.ForeignKey(ArticleSection, on_delete=models.SET_NULL ,null=True,related_name='ArticlePage')
    footer_section = models.ForeignKey(FooterSection,on_delete=models.CASCADE, related_name='ArticlePage',default=2)  
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Article Pages"

class InvestorsPromo(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='articles/', null=True,blank=True)
    cta_link =  models.CharField(max_length=255)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Investors Promos"

class Investors(models.Model):
    title = models.CharField(max_length=255)
    navbar = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=1)
    subnav = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=2,related_name="investors_sub_nav")
    hero_sections = models.ForeignKey(HeroSection, on_delete=models.SET_NULL ,null=True,related_name='Investors')
    investor_promo = models.ManyToManyField('InvestorsPromo',related_name='Investors')
    footer_section = models.ForeignKey(FooterSection,on_delete=models.CASCADE, related_name='Investors',default=2)  
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Investors"

class Team(models.Model):
    # Choices for the category field
    CATEGORY_CHOICES = [
        ('board_of_directors', 'Board of Directors'),
        ('management_team', 'Management Team'),
    ]

    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team_images/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f'{self.name} ({self.designation}) - {self.get_category_display()}'

    class Meta:
        verbose_name_plural = "Teams"

class LeadershipPage(models.Model):
    title = models.CharField(max_length=255)
    navbar = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=1)
    subnav = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=2,related_name="leadership_sub_nav")
    hero_sections = models.ForeignKey(HeroSection, on_delete=models.SET_NULL ,null=True,related_name='LeadershipPage')
    team_promo = models.ManyToManyField('Team',related_name='LeadershipPage')
    footer_section = models.ForeignKey(FooterSection,on_delete=models.CASCADE, related_name='LeadershipPage',default=2)  
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Leadership Pages"

class MediaCards(models.Model):
    CATEGORY_CHOICES = [
        ('Glossary', 'Glossary'),
        ('All Banknotes', 'All Banknotes'),
        ('Press Releases', 'Press Releases'),
        ('Media Contacts', 'Media Contacts'),
        ('Images', 'Images'),
    ]
    year = models.CharField(max_length=50,blank=True)
    title = models.CharField(max_length=255)
    description = RichTextField(blank=True)
    cta_text = models.CharField(max_length=50, blank=True, null=True)
    cta_link = models.CharField(max_length=200, blank=True, null=True)
    tab_image = models.ImageField(upload_to='media_tab_image/', blank=True, null=True)
    image = models.ImageField(upload_to='account_card_images/', blank=True, null=True)
    tab = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    def __str__(self):
        if self.year:
            return f"{self.title} ({self.year})"
        else:
            return f"{self.title} (None)"

    class Meta:
        verbose_name_plural = "Media Cards"

class MediaPage(models.Model):
    title = models.CharField(max_length=255)
    navbar = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=1)
    subnav = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=2,related_name="media_sub_nav")
    hero_sections = models.ForeignKey(HeroSection, on_delete=models.SET_NULL ,null=True,related_name='MediaPage')
    media_tabs_promo = models.ManyToManyField('MediaCards',related_name='MediaPage')
    footer_section = models.ForeignKey(FooterSection,on_delete=models.CASCADE, related_name='MediaPage',default=2)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Media Pages"

class AssociatedCompaniesPromo(models.Model):
    promo_title = models.CharField(max_length=255, help_text="Title of the promo section")

    def __str__(self):
        return self.promo_title

    class Meta:
        verbose_name_plural = "Associated Companies Promos"

class AssociatedCompaniesPromoEntry(models.Model):
    promo = models.ForeignKey(AssociatedCompaniesPromo, related_name='entries_comp', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='associated_comp_logos/',blank=True)
    title = models.CharField(max_length=255)
    header = models.CharField(max_length=255)
    status_description = models.CharField(max_length=255)
    cta_text = models.CharField(max_length=255)
    cta_link = models.CharField(max_length=255)

    def __str__(self):
        return self.header

    class Meta:
        verbose_name_plural = "Associated Companies Promo Entries"

class CompanyDetails(models.Model):

    status_description = RichTextField()
    def __str__(self):
        return self.status_description

    class Meta:
        verbose_name_plural = "Company Details"

class TablePromo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    table = RichTextField()
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Table Promos"

class CompanyProfile(models.Model):
    title = models.CharField(max_length=255)
    navbar = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=1)
    subnav = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=2,related_name="company_profile_sub_nav")
    hero_sections = models.ForeignKey(HeroSection, on_delete=models.SET_NULL ,null=True,related_name='CompanyProfile')
    vision_mission_promo = models.ForeignKey(VisionMissionPromo, on_delete=models.SET_NULL, null=True, related_name='CompanyProfile')
    companies_promo = models.ForeignKey(AssociatedCompaniesPromo, on_delete=models.SET_NULL, null=True, related_name='CompanyProfile')
    company_detail = models.ForeignKey(CompanyDetails, on_delete=models.SET_NULL, null=True, related_name='CompanyProfile')
    company_table_promo = models.ForeignKey(TablePromo, on_delete=models.SET_NULL, null=True, related_name='CompanyProfile')
    footer_section = models.ForeignKey(FooterSection,on_delete=models.CASCADE, related_name='CompanyProfile',default=2)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Company Profiles"

class LegalAdvisorsPromo(models.Model):
    title = models.CharField(max_length=255)
    name_auditor = models.CharField(max_length=255)
    organization_auditor = models.CharField(max_length=255)
    name_legal_advisor = models.CharField(max_length=255)
    organization_legal_advisor = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Legal Advisors Promos"

class GrievancePromo(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField()
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255,blank=True)
    email = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    location= models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Grievance Promos"

class GovernancePage(models.Model):
    title = models.CharField(max_length=255)
    navbar = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=1)
    subnav = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=2,related_name="governance_sub_nav")
    hero_sections = models.ForeignKey(HeroSection, on_delete=models.SET_NULL ,null=True,related_name='GovernancePage')
    team_promo = models.ManyToManyField('Team',related_name='GovernancePage')
    legal_promo = models.ForeignKey(LegalAdvisorsPromo, on_delete=models.SET_NULL ,null=True,related_name='GovernancePage')
    grievance_promo = models.ForeignKey(GrievancePromo, on_delete=models.SET_NULL ,null=True,related_name='GovernancePage')

    footer_section = models.ForeignKey(FooterSection,on_delete=models.CASCADE, related_name='GovernancePage',default=2)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Governance Pages"

class QuickLinks(models.Model):
    title = models.CharField(max_length=255)
    navbar = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=1)
    subnav = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=2,related_name="quick_links_sub_nav")
    hero_sections = models.ForeignKey(HeroSection, on_delete=models.SET_NULL ,null=True,related_name='QuickLinks')
    shareholding_info = models.ForeignKey(TablePromo, on_delete=models.SET_NULL, null=True, related_name='QuickLinks')
    others_info = models.ForeignKey(TablePromo, on_delete=models.SET_NULL, null=True, related_name='QuickLinks_2')
    footer_section = models.ForeignKey(FooterSection,on_delete=models.CASCADE, related_name='QuickLinks',default=2)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Quick Links"

class ComplaintFormData(models.Model):
    customer_name = models.CharField(max_length=255)
    customer_email = models.CharField(max_length=255)
    customer_contact_no = models.CharField(max_length=255)
    customer_contact_no_landline = models.CharField(max_length=255)
    customer_contact_acc_no = models.CharField(max_length=255)
    customer_city = models.CharField(max_length=255)
    product_detail = models.CharField(max_length=255)
    complaint_detail = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.customer_name} - {self.complaint_detail}'

    class Meta:
        verbose_name_plural = "Complaint Form Data"

class FraudulentFundTransferComplaint(models.Model):
    customer_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    cnic_no = models.CharField(max_length=255)
    transaction_date = models.CharField(max_length=255)
    transaction_amount = models.CharField(max_length=255)
    account_amount = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=255)
    customer_remarks = models.CharField(max_length=255)
    other_information = models.CharField(max_length=255)

    def __str__(self):
        return self.customer_name

    class Meta:
        verbose_name_plural = "Fraudulent Fund Transfer Complaints"

class ContactInfo(models.Model):
    logo = models.ImageField(upload_to='logos/',blank=True)
    cta_link = models.CharField(max_length=255)
    cta_text = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.cta_text}'

    class Meta:
        verbose_name_plural = "Contact Info"

class ContactUs(models.Model):
    title = models.CharField(max_length=255)
    navbar = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=1)
    subnav = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=2,related_name="contact_us_sub_nav")
    hero_sections = models.ForeignKey(HeroSection, on_delete=models.SET_NULL ,null=True,related_name='ContactUs')
    vision_mission_promo = models.ForeignKey(VisionMissionPromo, on_delete=models.SET_NULL, null=True, related_name='ContactUs')
    contact_info = models.ManyToManyField('ContactInfo', related_name='ContactUs')
    footer_section = models.ForeignKey(FooterSection,on_delete=models.CASCADE, related_name='ContactUs',default=2)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Contact Us"

class InvestorRelation(models.Model):
    title = models.CharField(max_length=255)
    navbar = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=1)
    subnav = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=2,related_name="investor_relation_sub_nav")
    hero_sections = models.ForeignKey(HeroSection, on_delete=models.SET_NULL ,null=True,related_name='InvestorRelation')
    article_section = models.ForeignKey(ArticleSection, on_delete=models.SET_NULL ,null=True,related_name='InvestorRelation')
    grievance_promo = models.ForeignKey(GrievancePromo, on_delete=models.SET_NULL ,null=True,related_name='InvestorRelation')
    footer_section = models.ForeignKey(FooterSection,on_delete=models.CASCADE, related_name='InvestorRelation',default=2)

    class Meta:
        verbose_name_plural = "Investor Relations"

    def __str__(self):
        return self.title

from django.core.files.storage import FileSystemStorage
from cryptography.fernet import Fernet
import base64
from django.conf import settings
import os

class EncryptedField(models.TextField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_fernet(self):
        key = settings.ENCRYPTION_KEY.encode()
        return Fernet(base64.urlsafe_b64encode(key.ljust(32)[:32]))

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        f = self.get_fernet()
        try:
            return f.decrypt(value.encode()).decode()
        except:
            return value

    def to_python(self, value):
        if value is None:
            return value
        return value

    def get_prep_value(self, value):
        if value is None:
            return value
        f = self.get_fernet()
        return f.encrypt(str(value).encode()).decode()

class EmploymentApplication(models.Model):
    # Personal Details
    full_name = EncryptedField()
    email = EncryptedField()
    mobile_number = EncryptedField()
    cnic = EncryptedField()
    date_of_birth = EncryptedField()
    emergency_number = EncryptedField()
    address = EncryptedField()
    city = EncryptedField()
    
    # Education Details
    qualification = EncryptedField()
    institution = EncryptedField()
    additional_certification = EncryptedField(null=True, blank=True)
    education_start_date = EncryptedField()
    education_end_date = EncryptedField(null=True, blank=True)
    education_in_process = models.BooleanField(default=False)
    
    # Experience Details
    industry_type = EncryptedField(null=True, blank=True)
    designation = EncryptedField(null=True, blank=True)
    organization = EncryptedField(null=True, blank=True)
    job_tenure_from = EncryptedField(null=True, blank=True)
    job_tenure_to = EncryptedField(null=True, blank=True)
    job_tenure_in_process = models.BooleanField(default=False)
    
    # Additional Education and Experience (JSON fields to store multiple entries)
    additional_education = models.JSONField(null=True, blank=True)
    additional_experience = models.JSONField(null=True, blank=True)
    
    # CV Upload
    cv_file = models.FileField(upload_to='employment_applications/cv/')
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Application by {self.full_name}"

    class Meta:
        verbose_name = "Employment Application"
        verbose_name_plural = "Employment Applications"

class EmploymentApplicationPage(models.Model):
    title = models.CharField(max_length=255)
    navbar = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True, default=1)
    subnav = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True, default=2, related_name="employment_page_sub_nav")
    hero_sections = models.ForeignKey(HeroSection, on_delete=models.SET_NULL, null=True, blank=True, related_name='employment_page')
    footer_section = models.ForeignKey(FooterSection, on_delete=models.CASCADE, related_name='employment_page', default=2)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Employment Application Page"
        verbose_name_plural = "Employment Application Pages"

class FileUpload(models.Model):
    name = models.CharField(max_length=255, help_text="Name of the file")
    description = models.TextField(blank=True, null=True, help_text="Optional description of the file")
    file = models.FileField(upload_to='uploads/', help_text="The uploaded file")
    upload_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    @property
    def file_url(self):
        """
        Returns the URL of the file for downloading
        """
        return self.file.url if self.file else None
    
    class Meta:
        verbose_name = "File Upload"
        verbose_name_plural = "File Uploads"
