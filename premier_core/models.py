from django.db import models
from core.models import *
from islamic_core.models import *
# Create your models here.
class Homepage(models.Model):
    title = models.CharField(max_length=255)
    hero_slider_sections = models.ManyToManyField(HeroSectionSlider, related_name='prem_homepages', blank=True)
    navbar = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=4,related_name='prem_home')
    subnav = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=2,related_name="prem_sub_nav")
    hero_sections = models.ManyToManyField(HeroSection, related_name='prem_home')
    account_promo = models.ForeignKey(AccountPromo, on_delete=models.SET_NULL, null=True, blank=True, related_name='prem_home')
    financial_solution_promo = models.ManyToManyField(FinancialSolutionPromo, related_name='prem_home', blank=True)
    offers_promo = models.ForeignKey(OffersPromo, on_delete=models.SET_NULL, null=True, blank=True, related_name='prem_home')  
    promo_banner = models.ForeignKey(PromoBanner, on_delete=models.SET_NULL, null=True, blank=True, related_name='prem_home')
    banking_promo = models.ManyToManyField(BankingPromo, related_name='prem_home', blank=True)
    reports_promo = models.ForeignKey(ReportsTabSection, on_delete=models.SET_NULL ,null=True,related_name='prem_financial_reports')
    footer_section = models.ForeignKey(FooterSection, on_delete=models.CASCADE, related_name='prem_home', default=3)  # Corrected ForeignKey field
    
    class Meta:
        verbose_name_plural = "Homepages"
    
    def __str__(self):
        return self.title
    
class PremierCardsPromoPages(models.Model):
    title = models.CharField(max_length=255)
    navbar = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=4)
    subnav = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=2,related_name="card_prem_sub_nav")
    hero_sections = models.ForeignKey(HeroSection, on_delete=models.SET_NULL ,null=True,related_name='prem_card_promo')
    cards = models.ForeignKey(CardPromoSection, on_delete=models.SET_NULL ,null=True,related_name='prem_card_promo')
    promo_banner = models.ForeignKey(PromoBanner, on_delete=models.SET_NULL, null=True, blank=True)
    footer_section = models.ForeignKey(FooterSection,on_delete=models.CASCADE, related_name='prem_card_promo',default=3)   

    class Meta:
        verbose_name_plural = "Premier Cards Promo Pages"

    def __str__(self):
        return self.title
    

class ColumnSection(models.Model):
    """Represents a section with a title and multiple column entries."""
    title = models.CharField(max_length=255)
    heading_full_width = models.CharField(max_length=255, blank=True, null=True)
    full_width_first_column_data = RichTextField(blank=True, null=True)
    full_width_second_column_data = RichTextField(blank=True, null=True)
    heading_half_width_1 = models.CharField(max_length=255, blank=True, null=True)
    half_width_1_data = RichTextField(blank=True, null=True)
    heading_half_width_2 = models.CharField(max_length=255, blank=True, null=True)
    half_width_2_data = RichTextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Column Sections"

    def __str__(self):
        return self.title


class MultiColumnFAQSection(models.Model):
    title = models.CharField(max_length=200,blank=True)

    class Meta:
        verbose_name_plural = "Multi Column FAQ Sections"

    def __str__(self):
        return self.title

class MultiColumnFAQItem(models.Model):
    faq_section = models.ForeignKey(MultiColumnFAQSection, related_name='faq_items', on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    first_col_answer = RichTextField()
    second_col_answer = RichTextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Multi Column FAQ Items"

    def __str__(self):
        return f"Q: {self.question}"
    
class GoldenPromoCTAEntry(models.Model):
    title = models.CharField(max_length=200,blank=True)

    class Meta:
        verbose_name_plural = "Golden Promo CTA Entries"

    def __str__(self):
        return self.title
    
class GoldenPromoCTA(models.Model):
    gold_promo_main = models.ForeignKey(GoldenPromoCTAEntry, related_name='faq_items_golden', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = RichTextField()
    cta1_text = models.CharField(max_length=100, blank=True, null=True)
    cta1_url = models.CharField(blank=True, null=True)
    image = models.ImageField(upload_to='gold_promo_cta/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Golden Promo CTAs"

    def __str__(self):
        return self.title

class NestedFAQPremier(models.Model):
    title = models.CharField(max_length=255,null=True,blank=True)

    class Meta:
        verbose_name_plural = "Nested FAQ Premiers"

    def __str__(self):
        return self.title if self.title else 'No title'

class PremierFAQCategory(models.Model):
    nested_faq_section = models.ForeignKey(
        NestedFAQPremier,
        related_name='faq_premier',
        on_delete=models.CASCADE
    )
    header = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Premier FAQ Categories"

    def __str__(self):
        return self.header

class PremierFAQQuestionAnswer(models.Model):
    category = models.ForeignKey(
        PremierFAQCategory,
        related_name='faq_premier_question_answers',
        on_delete=models.CASCADE
    )
    question = models.CharField(max_length=255,null=True,blank=True)
    answer_col_1 = RichTextField()
    answer_col_2 = RichTextField(null=True,blank=True)

    class Meta:
        verbose_name_plural = "Premier FAQ Question Answers"

    def __str__(self):
        return self.question if self.question else 'No question provided'

class FinanceProgram(models.Model):
    title = models.CharField(max_length=255)  # Main title like 'Fuel Your Drive Toyota' or 'Suzuki Finance Arrangement Program (SFAP)'

    class Meta:
        verbose_name_plural = "Finance Programs"

    def __str__(self):
        return self.title


# Inline Model
class FinanceProgramDetail(models.Model):
    program = models.ForeignKey(FinanceProgram, on_delete=models.CASCADE, related_name='details')
    heading = models.CharField(max_length=255)  # 'What's included?'
    description = RichTextField() # Points like "All Toyota Variant, Preferred Delivery, etc."

    class Meta:
        verbose_name_plural = "Finance Program Details"

    def __str__(self):
        return f"{self.program.title} - {self.heading}"
    
class PremierIndividualAccounts(models.Model):
    title = models.CharField(max_length=255)
    navbar = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=4)
    subnav = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=2,related_name="prem_ind_sub_nav")

    hero_sections = models.ForeignKey(HeroSection, on_delete=models.SET_NULL ,null=True,related_name='prem_ind_details')
    financial_program_promo = models.ForeignKey(FinanceProgram, null=True, blank=True,on_delete=models.SET_NULL,related_name='prem_ind_finance')

    multi_column_faq_section = models.ForeignKey(MultiColumnFAQSection, null=True, blank=True,on_delete=models.SET_NULL,related_name='prem_ind_faq')
    account_features = models.ManyToManyField(AccountFeature,blank=True,related_name='prem_ind_details')
    golden_promo = models.ForeignKey(GoldenPromoCTAEntry, null=True, blank=True,on_delete=models.SET_NULL,related_name='prem_golden_promo')
    text_promo = models.ForeignKey(ArticleSection, on_delete=models.SET_NULL ,null=True,blank=True,related_name='prem_ind_text')
    prem_faq_nested = models.ForeignKey(NestedFAQPremier,null=True, blank=True,on_delete=models.SET_NULL, related_name='prem_ind_faq')
    table_1_prem = models.ForeignKey(TablePromo, on_delete=models.SET_NULL, null=True,blank=True, related_name='table_1_prem')
    table_2_prem = models.ForeignKey(TablePromo, on_delete=models.SET_NULL, null=True,blank=True, related_name='table_2_prem')
    promo_banner_full = models.ForeignKey(PromoBannerFull, on_delete=models.SET_NULL, null=True, blank=True)
    bullet_features = models.ForeignKey(ColumnSection, on_delete=models.SET_NULL, null=True, blank=True)
    footer_section = models.ForeignKey(FooterSection,on_delete=models.CASCADE, related_name='prem_ind_details',default=3)  

    class Meta:
        verbose_name_plural = "Premier Individual Accounts"

class ContactUsData(models.Model):
    title = models.CharField(max_length=100)  
    
    class Meta:
        verbose_name_plural = "Contact Us Data"

    def __str__(self):
        return self.title

class Location(models.Model):
    main_contact = models.ForeignKey(ContactUsData, on_delete=models.CASCADE, related_name='locations')  # Link to Region
    region_name = models.CharField(max_length=100,blank=True)  
    location_name = models.CharField(max_length=100,blank=True)
    poc_name = models.CharField(max_length=100,blank=True)
    poc_designation = models.CharField(max_length=100,blank=True)
    email = models.CharField(max_length=20,blank=True)  
    phone_number = models.CharField(max_length=20,blank=True)
    phone_number_2 = models.CharField(max_length=20,blank=True)
    
    class Meta:
        verbose_name_plural = "Locations"

    def __str__(self):
        return f"{self.region_name} ({self.phone_number})"

class ContactUsPage(models.Model):
    title = models.CharField(max_length=255)
    navbar = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=4)
    subnav = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=2,related_name="con_sub_nav")
    hero_sections = models.ForeignKey(HeroSection, on_delete=models.SET_NULL ,null=True,related_name='contact_us')
    location_data = models.ForeignKey(ContactUsData, on_delete=models.SET_NULL ,null=True,related_name='contact_us')
    footer_section = models.ForeignKey(FooterSection,on_delete=models.CASCADE, related_name='contact_us',default=3) 

    class Meta:
        verbose_name_plural = "Contact Us Pages"

class HomeFinancePage(models.Model):
    title = models.CharField(max_length=255)
    navbar = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=4)
    subnav = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=2,related_name="hf_sub_nav")
    hero_sections = models.ForeignKey(HeroSection, on_delete=models.SET_NULL ,null=True,related_name='home_finance_page')
    cards = models.ForeignKey(CardPromoSection, on_delete=models.SET_NULL ,null=True,blank=True,related_name='home_finance_page')
    multi_column_faq_section = models.ForeignKey(MultiColumnFAQSection, null=True, blank=True,on_delete=models.SET_NULL,related_name='home_finance_page')
    location_data = models.ForeignKey(ContactUsData, on_delete=models.SET_NULL ,null=True,blank=True,related_name='home_finance_page')
    promo_banner_full = models.ForeignKey(PromoBannerFull, on_delete=models.SET_NULL, null=True, blank=True)
    footer_section = models.ForeignKey(FooterSection,on_delete=models.CASCADE, related_name='home_finance_page',default=3) 

    class Meta:
        verbose_name_plural = "Home Finance Pages"

class StepsPromo(models.Model):
    title = models.CharField(max_length=255)  
    steps_image = models.ImageField(upload_to='steps_images/',blank=True)

    class Meta:
        verbose_name_plural = "Steps Promos"

    def __str__(self):
        return self.title


# Inline Model
class StepsPromoEntry(models.Model):

    step_main = models.ForeignKey(StepsPromo, on_delete=models.CASCADE, related_name='step_promo')
    step_no = models.CharField(max_length=255) 
    step_description = RichTextField() 

    class Meta:
        verbose_name_plural = "Steps Promo Entries"

    def __str__(self):
        return f"{self.step_no} - {self.step_description}"

class FinancingOptionPages(models.Model):
    title = models.CharField(max_length=255)
    navbar = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=4)
    subnav = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=2,related_name="fin_sub_nav")
    hero_sections = models.ForeignKey(HeroSection, on_delete=models.SET_NULL ,null=True,related_name='FinancingOptionPages')
    cards = models.ForeignKey(CardPromoSection, on_delete=models.SET_NULL ,null=True,blank=True,related_name='FinancingOptionPages')
    steps_promo = models.ForeignKey(StepsPromo, null=True, blank=True,on_delete=models.SET_NULL,related_name='FinancingOptionPages')
    account_features = models.ManyToManyField(AccountFeature,blank=True,related_name='FinancingOptionPages')
    table_1_prem = models.ForeignKey(TablePromo, on_delete=models.SET_NULL, null=True,blank=True, related_name='FinancingOptionPages')
    promo_banner_full = models.ForeignKey(PromoBannerFull, on_delete=models.SET_NULL, null=True, blank=True)
    footer_section = models.ForeignKey(FooterSection,on_delete=models.CASCADE, related_name='FinancingOptionPages',default=3) 

    class Meta:
        verbose_name_plural = "Financing Option Pages"

class OrbitPromo(models.Model):
    title = models.CharField(max_length=255)  
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Orbit Promos"

class OrbitPromoEntry(models.Model):

    orbit_main = models.ForeignKey(OrbitPromo, on_delete=models.CASCADE, related_name='orbit_promo')
    orbit_logo = models.ImageField(upload_to='steps_images/',blank=True)
    orbit_heading = models.CharField(max_length=255)  
    orbit_description = RichTextField() 
    orbit_cta_text = models.CharField(max_length=255) 
    orbit_cta_link = models.CharField(max_length=255) 

    class Meta:
        verbose_name_plural = "Orbit Promo Entries"

    def __str__(self):
        return self.orbit_heading

class OrbitRewardPages(models.Model):
    title = models.CharField(max_length=255)
    navbar = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=4)
    subnav = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=2,related_name="orbit_sub_nav")
    hero_sections = models.ForeignKey(HeroSection, on_delete=models.SET_NULL ,null=True,related_name='OrbitRewardPages')
    account_features = models.ManyToManyField(AccountFeature,blank=True,related_name='OrbitRewardPages')
    orbit_promo = models.ForeignKey(OrbitPromo, on_delete=models.SET_NULL, null=True,blank=True, related_name='OrbitRewardPages')
    prem_faq_nested = models.ForeignKey(NestedFAQPremier,null=True, blank=True,on_delete=models.SET_NULL, related_name='OrbitRewardPages')
    footer_section = models.ForeignKey(FooterSection,on_delete=models.CASCADE, related_name='OrbitRewardPages',default=3) 


    class Meta:
        verbose_name_plural = "Orbit Reward Pages"

class LogosPromo(models.Model):
    title = models.CharField(max_length=255)  
    description = RichTextField()
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Logos Promos"

class LogosPromoEntry(models.Model):

    logo_promo_main = models.ForeignKey(LogosPromo, on_delete=models.CASCADE, related_name='logo_promo')
    perks_logo = models.ImageField(upload_to='logos_perks/',blank=True)
    perks_name = models.CharField(max_length=255)  
   

    class Meta:
        verbose_name_plural = "Logos Promo Entries"

    def __str__(self):
        return self.perks_name

class MiscellenousPages(models.Model):
    
    navbar = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=4)
    subnav = models.ForeignKey(NavigationMain, on_delete=models.SET_NULL, null=True, blank=True,default=2,related_name="miscel_sub")
    text_top = models.BooleanField(default=True)
    show_calculator = models.BooleanField(default=False)
    title = models.CharField(max_length=255)
    account_features = models.ManyToManyField(AccountFeature,blank=True,related_name='MiscellenousPages')
    multi_column_faq_section = models.ForeignKey(MultiColumnFAQSection, null=True, blank=True,on_delete=models.SET_NULL,related_name='MiscellenousPages')
    cards = models.ForeignKey(CardPromoSection, on_delete=models.SET_NULL ,null=True,blank=True,related_name='MiscellenousPages')
    hero_sections = models.ForeignKey(HeroSection, on_delete=models.SET_NULL ,null=True,related_name='MiscellenousPages')
    table_1 = models.ForeignKey(TablePromo, on_delete=models.SET_NULL, null=True,blank=True, related_name='MiscellenousPages')
    table_2 = models.ForeignKey(TablePromo, on_delete=models.SET_NULL, null=True,blank=True, related_name='MiscellenousPagesTable2')
    table_3 = models.ForeignKey(TablePromo, on_delete=models.SET_NULL, null=True,blank=True, related_name='MiscellenousPagesTable3')
    all_text_data = models.ForeignKey(ArticleSection, on_delete=models.SET_NULL ,null=True,blank=True,related_name='MiscellenousPages')
    golden_promo = models.ForeignKey(GoldenPromoCTAEntry, null=True, blank=True,on_delete=models.SET_NULL,related_name='MiscellenousPages')
    promo_banner = models.ForeignKey(PromoBanner, on_delete=models.SET_NULL, null=True, blank=True, related_name='MiscellenousPages')
    promo_banner_full = models.ForeignKey(PromoBannerFull, on_delete=models.SET_NULL, null=True, blank=True)
    logos_promo = models.ForeignKey(LogosPromo, on_delete=models.SET_NULL, null=True, blank=True)
    file_faq_section = models.ForeignKey(FileNestedFAQSection, null=True, blank=True,on_delete=models.SET_NULL,related_name='MiscellenousPages')
    bullet_features = models.ForeignKey(ColumnSection, on_delete=models.SET_NULL, null=True, blank=True)
    all_text_data_bottom = models.ForeignKey(ArticleSection, on_delete=models.SET_NULL ,null=True,blank=True,related_name='MiscellenousPagesTextBottom')
    location_data = models.ForeignKey(ContactUsData, on_delete=models.SET_NULL ,null=True,blank=True,related_name='MiscellenousPages')
    branch_logo_promo = models.ForeignKey(LogosPromo, on_delete=models.SET_NULL, null=True, blank=True,related_name='branch_logo')

    footer_section = models.ForeignKey(FooterSection,on_delete=models.CASCADE, related_name='MiscellenousPages',default=3) 

    class Meta:
        verbose_name_plural = "Miscellaneous Pages"