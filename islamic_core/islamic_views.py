from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from islamic_core.models import *
# Create your views here.

def homepage_view(request):
    # Assuming there is only one Homepage instance
    homepage = IslamicHomepage.objects.first()
    hero_slider_sections = homepage.hero_slider_sections.all() if homepage else []
    account_promo = homepage.account_promo if homepage else None
    updates_slider = homepage.news_updates.all() if homepage else []
    offers_promo = homepage.offers_promo if homepage else None
    financial_solution_promos = homepage.financial_solution_promo.all() if homepage else []
    promo_banner = homepage.promo_banner if homepage else None
    banking_promos = homepage.banking_promo.all() if homepage else []
    footer = homepage.footer_section.links.all() if homepage else None
    footer_image = homepage.footer_section if homepage else None
   
    # Get all navigation bars for the homepage
    navigation_main = homepage.navbar
    navbar_items = navigation_main.navbar.prefetch_related('sub_tabs__links')

    navbar_data = [
        {
            'main_item': item,
            'sub_tabs': [
                {
                    'sub_tab': sub_tab,
                    'links': list(sub_tab.links.all())
                }
                for sub_tab in item.sub_tabs.all()
            ],
        }
        for item in navbar_items
        ]
    subnav = homepage.subnav if homepage else None
    subnav_items = []
    
    if subnav:
     
        subnav_items = subnav.navbar.all()



    print(hero_slider_sections)
    return render(request, 'islamic_home.html', {'hero_slider_sections': hero_slider_sections,'navbar_data':navbar_data,'subnav_items': subnav_items,'navigation_logo_url':navigation_main.logo.url,'account_promo':account_promo,'news_updates':updates_slider,'offers_promo':offers_promo, 'financial_solution_promos': financial_solution_promos,'promo_banner': promo_banner,'banking_promos': banking_promos,'footer':footer,'footer_image':footer_image})

def accounts_detail_view_islamic(request,section):
    try:
        titles_mapping = {
        "Foreign Currency Debit Card": "Bank Alfalah VISA Islamic Foreign Currency Debit Card",
        "Bank Alfalah Islamic Asaan Remittance Savings Account": "Bank Alfalah Islamic Asaan Remittance Savings Account",
        "Bank Alfalah Islamic Asaan Digital Remittance Savings Account":"Bank Alfalah Islamic Asaan Digital Remittance Savings Account",
        "Bank Alfalah Asaan Women Digital Savings Account":"Bank Alfalah Asaan Women Digital Savings Account",
        "Bank Alfalah Islamic Asaan Digital Savings Account":"Bank Alfalah Islamic Asaan Digital Savings Account",
        "Bank Alfalah Senior Citizens Savings Account":"Bank Alfalah Senior Citizens Savings Account",
        "Bank Alfalah Islamic Profex Account":"Bank Alfalah Islamic Profex Account",
        "Bank Alfalah Mahana Amdani Account":"Bank Alfalah Mahana Amdani Account",
        "Bank Alfalah Islamic Asaan Savings Account":"Bank Alfalah Islamic Asaan Savings Account",
        "Bank Alfalah Business Account":"Bank Alfalah Business Account",
        "Bank Alfalah Musharakah Savings Account":"Bank Alfalah Musharakah Savings Account",
        "Bank Alfalah Islamic Foreign Currency Savings Account":"Bank Alfalah Islamic Foreign Currency Savings Account",
        "Bank Alfalah Islamic Khayaal Rakhna Account":"Bank Alfalah Islamic Khayaal Rakhna Account",
        "Bank Alfalah Islamic Senior Citizens Term Deposit":"Bank Alfalah Islamic Senior Citizens Term Deposit",
        "Bank Alfalah Islamic Premium Term Deposits":"Bank Alfalah Islamic Premium Term Deposits",
        "Bank Alfalah 3 Year Term Deposit":"Bank Alfalah 3 Year Term Deposit",
        "Bank Alfalah Mahana Munafa Term Deposit":"Bank Alfalah Mahana Munafa Term Deposit",
        "Bank Alfalah Term Deposits":"Bank Alfalah Term Deposits",
        "Bank Alfalah Islamic Foreign Currency Term Deposits":"Bank Alfalah Islamic Foreign Currency Term Deposits",
        "Bank Alfalah Islamic Asaan Current Account":"Bank Alfalah Islamic Asaan Current Account",
        "Bank Alfalah Islamic Asaan Remittance Current Account":"Bank Alfalah Islamic Asaan Remittance Current Account",
        "Bank Alfalah Islamic Business Way and Payroll":"Bank Alfalah Islamic Business Way and Payroll",
        "Bank Alfalah Islamic Current Account":"Bank Alfalah Islamic Current Account",
        "Trade Services":"Trade Services",
        "Target Savings Deposit":"Target Savings Deposit",
        "Freelancer Digital Saving":"Bank Alfalah Islamic Freelancer Digital Savings Account",
        "Bank Alfalah Basic Banking Account":"Bank Alfalah Basic Banking Account",
        "Bank Alfalah Islamic Foreign Currency Current Account":"Bank Alfalah Islamic Foreign Currency Current Account",
        "Bank Alfalah Islamic Asaan Digital Current Account":"Bank Alfalah Islamic Asaan Digital Current Account",
        "Bank Alfalah Islamic Asaan Digital Remittance Current Account":"Bank Alfalah Islamic Asaan Digital Remittance Current Account",
        "Bank Alfalah Islamic Freelancer Digital Current Account":"Bank Alfalah Islamic Freelancer Digital Current Account",
        "Employee Banking - Alfalah Islamic Business Way":"Employee Banking - Alfalah Islamic Business Way",
        "Roshan Products":"Roshan Products",
        "Islamic Power Pack":"Islamic Power Pack",
        }
        
        if section in titles_mapping:
            accounts_detail = IslamicAccountFeature.objects.get(title=titles_mapping[section])
        hero_accounts = accounts_detail.hero_sections if accounts_detail else None
        navigation_main = accounts_detail.navbar
        navbar_items = navigation_main.navbar.prefetch_related('sub_tabs__links')
        navbar_data = [
            {
                'main_item': item,
                'sub_tabs': [
                    {
                        'sub_tab': sub_tab,
                        'links': list(sub_tab.links.all())
                    }
                    for sub_tab in item.sub_tabs.all()
                ],
            }
            for item in navbar_items
        ]
        subnav = accounts_detail.subnav if accounts_detail else None
        subnav_items = []
        
        if subnav:
        
            subnav_items = subnav.navbar.all()


        tabs_promo = accounts_detail.tab_section.all() if accounts_detail else None
        promo_banner = accounts_detail.promo_banner if accounts_detail else None
        promo_banner_full = accounts_detail.promo_banner_full if accounts_detail else None
        card_detail_1 = accounts_detail.card_info_1 if accounts_detail.card_info_1 else []
        card_detail_2 = accounts_detail.card_info_2 if accounts_detail.card_info_2 else []
        faqs = accounts_detail.faq_islamic.all() if accounts_detail else []

        footer_image = accounts_detail.footer_section if accounts_detail else None
        footer = accounts_detail.footer_section.links.all() if accounts_detail else None
        eligible_docs = accounts_detail.eligibility_docs.all() if accounts_detail else []
        for doc in eligible_docs:
            # Access the title and description from the related `EligibilityDocsSection`
            section = doc.section if hasattr(doc, 'section') else None
        
        eligible_docs_title = section.title if eligible_docs else None
        eligible_docs_desc = section.description if eligible_docs else None
    
        return render(request, 'foreign_currency_debit.html', {'hero_sections': hero_accounts,'navbar_data':navbar_data,'subnav_items': subnav_items,'navigation_logo_url':navigation_main.logo.url,'promo_banner':promo_banner,'eligible_docs':eligible_docs,'eligible_docs_title':eligible_docs_title,'eligible_docs_desc':eligible_docs_desc,'promo_banner_full':promo_banner_full,'card_table_1':card_detail_1,'card_table_2':card_detail_2,"faqs":faqs,'tabs_promo':tabs_promo,'footer_image':footer_image,'footer':footer})
    except ObjectDoesNotExist:
        return HttpResponse("User not found", status=404)
    # except Exception as e:
    #     return HttpResponse(f"An unexpected error occurred: {str(e)}", status=500)

def accounts_lp_view(request):
    
    accounts_islamic = AccountsPageIslamic.objects.first()
    navigation_main = accounts_islamic.navbar
    navbar_items = navigation_main.navbar.prefetch_related('sub_tabs__links')
    navbar_data = [
        {
            'main_item': item,
            'sub_tabs': [
                {
                    'sub_tab': sub_tab,
                    'links': list(sub_tab.links.all())
                }
                for sub_tab in item.sub_tabs.all()
            ],
        }
        for item in navbar_items
    ]
    subnav = accounts_islamic.subnav if accounts_islamic else None
    subnav_items = []
    
    if subnav:
        subnav_items = subnav.navbar.all()
    hero_accounts = accounts_islamic.hero_sections if accounts_islamic else None
    promo_banner = accounts_islamic.promo_banner if accounts_islamic else None
    accounts_promo_all = accounts_islamic.accounts_promo_all if accounts_islamic else None
    footer_image = accounts_islamic.footer_section if accounts_islamic else None
    footer = accounts_islamic.footer_section.links.all() if accounts_islamic else None
  
    return render(request, 'accounts_islamic_lp.html', {'hero_sections': hero_accounts,'navbar_data':navbar_data,'subnav_items': subnav_items,'navigation_logo_url':navigation_main.logo.url,'promo_banner':promo_banner,'accounts_promo':accounts_promo_all,'footer_image':footer_image,'footer':footer})

def cards_promo_islamic(request,section):
    
    titles_mapping = {
    "sme": "SME/Commercial Banking",
    "other": "Other Related Information",
    "sbp": "SBP Schemes",
    "digital-banking": "Digital Banking",
    "takaful": "Banca Takaful",
    "consumer": "Consumer Banking",
    "corporate": "Corporate Banking",
    "treasury": "Treasury & Capital Markets"
    }

    if section in titles_mapping:
        accounts_islamic = CardsPromoPages.objects.get(title=titles_mapping[section])
    
    hero_accounts = accounts_islamic.hero_sections if accounts_islamic else None
    navigation_main = accounts_islamic.navbar
    navbar_items = navigation_main.navbar.prefetch_related('sub_tabs__links')
    navbar_data = [
        {
            'main_item': item,
            'sub_tabs': [
                {
                    'sub_tab': sub_tab,
                    'links': list(sub_tab.links.all())
                }
                for sub_tab in item.sub_tabs.all()
            ],
        }
        for item in navbar_items
    ]
    subnav = accounts_islamic.subnav if accounts_islamic else None
    subnav_items = []
    
    if subnav:
        subnav_items = subnav.navbar.all()
    promo_banner = accounts_islamic.promo_banner if accounts_islamic else None
    cards_data = accounts_islamic.cards if accounts_islamic else None
    footer_image = accounts_islamic.footer_section if accounts_islamic else None
    footer = accounts_islamic.footer_section.links.all() if accounts_islamic else None
    

    return render(request, 'cards_promo.html', {'hero_sections': hero_accounts,'navbar_data':navbar_data,'subnav_items': subnav_items,'navigation_logo_url':navigation_main.logo.url,'promo_banner':promo_banner,'cards_data':cards_data,'footer_image':footer_image,'footer':footer})

def debit_cards_promo_islamic(request,section):

    accounts_islamic = CardsPromoPages.objects.get(title='Debit Cards')    
    navigation_main = accounts_islamic.navbar
    navbar_items = navigation_main.navbar.prefetch_related('sub_tabs__links')
    navbar_data = [
        {
            'main_item': item,
            'sub_tabs': [
                {
                    'sub_tab': sub_tab,
                    'links': list(sub_tab.links.all())
                }
                for sub_tab in item.sub_tabs.all()
            ],
        }
        for item in navbar_items
    ]
    subnav = accounts_islamic.subnav if accounts_islamic else None
    subnav_items = []
    
    if subnav:
     
        subnav_items = subnav.navbar.all()
    hero_accounts = accounts_islamic.hero_sections if accounts_islamic else None
    promo_banner = accounts_islamic.promo_banner if accounts_islamic else None
    cards_data = accounts_islamic.cards if accounts_islamic else None
    footer_image = accounts_islamic.footer_section if accounts_islamic else None
    footer = accounts_islamic.footer_section.links.all() if accounts_islamic else None
    
    
    return render(request, 'debit_cards.html', {'hero_sections': hero_accounts,'navbar_data':navbar_data,'subnav_items': subnav_items,'navigation_logo_url':navigation_main.logo.url,'promo_banner':promo_banner,'cards_data':cards_data,'footer_image':footer_image,'footer':footer})

def cdm_page_view(request):
    cdm_data = CDMPage.objects.first() 
    navigation_main = cdm_data.navbar
    navbar_items = navigation_main.navbar.prefetch_related('sub_tabs__links')
    navbar_data = [
        {
            'main_item': item,
            'sub_tabs': [
                {
                    'sub_tab': sub_tab,
                    'links': list(sub_tab.links.all())
                }
                for sub_tab in item.sub_tabs.all()
            ],
        }
        for item in navbar_items
    ]   
    subnav = cdm_data.subnav if cdm_data else None
    subnav_items = []
    
    if subnav:
     
        subnav_items = subnav.navbar.all()


    hero_accounts = cdm_data.hero_sections if cdm_data else None
    promo_banner = cdm_data.promo_banner if cdm_data else None
    cdm_table_data = cdm_data.cdm_section if cdm_data else None
    footer_image = cdm_data.footer_section if cdm_data else None
    footer = cdm_data.footer_section.links.all() if cdm_data else None
    
    cdm_context = {
        "title": cdm_table_data.title if cdm_table_data else None,
        "entries": [
            {"city": entry.city_name, "description": entry.description}
            for entry in cdm_table_data.cdm_entries.all()
        ] if cdm_table_data else [],
    }
     # Combine all context
    context = {
        "cdm_data": cdm_context,
        'navigation_logo_url':navigation_main.logo.url,
        "navbar_data": navbar_data,
        'subnav_items': subnav_items,
        "hero_sections": hero_accounts,
        "promo_banner": promo_banner,
        "footer_image": footer_image,
        "footer": footer,
    }
    return render(request, 'cdm.html', context)

def islamic_gallery(request,section):

    titles_mapping = {
    "islamic-gallery": "Bank Alfalah Islamic Gallery",
    "islamic-aboutus": "About Us Islamic",
    
    }
    if section in titles_mapping:
        gallery_page = GalleryPage.objects.get(title=titles_mapping[section])
 
    hero_accounts = gallery_page.hero_sections if gallery_page else None
    navigation_main = gallery_page.navbar
    navbar_items = navigation_main.navbar.prefetch_related('sub_tabs__links')
    navbar_data = [
        {
            'main_item': item,
            'sub_tabs': [
                {
                    'sub_tab': sub_tab,
                    'links': list(sub_tab.links.all())
                }
                for sub_tab in item.sub_tabs.all()
            ],
        }
        for item in navbar_items
    ]
    subnav = gallery_page.subnav if gallery_page else None
    subnav_items = []
    
    if subnav:
     
        subnav_items = subnav.navbar.all()



    gallery_data = gallery_page.gallery_data if gallery_page else None
    footer_image = gallery_page.footer_section if gallery_page else None
    footer = gallery_page.footer_section.links.all() if gallery_page else None
    
  
    return render(request, 'gallery.html', {'hero_sections': hero_accounts,'navbar_data':navbar_data,'subnav_items': subnav_items,'navigation_logo_url':navigation_main.logo.url,'gallery_data':gallery_data,'footer_image':footer_image,'footer':footer})

def islamic_recurring_deposit_page(request):

    islamic_deposit_data = IslamicRecurringDepositPage.objects.first()  
    navigation_main = islamic_deposit_data.navbar
    navbar_items = navigation_main.navbar.prefetch_related('sub_tabs__links')
    navbar_data = [
        {
            'main_item': item,
            'sub_tabs': [
                {
                    'sub_tab': sub_tab,
                    'links': list(sub_tab.links.all())
                }
                for sub_tab in item.sub_tabs.all()
            ],
        }
        for item in navbar_items
    ]  
    subnav = islamic_deposit_data.subnav if islamic_deposit_data else None
    subnav_items = []
    
    if subnav:
     
        subnav_items = subnav.navbar.all()

    hero_accounts = islamic_deposit_data.hero_sections if islamic_deposit_data else None
    tabs_promo = islamic_deposit_data.tab_section.all() if islamic_deposit_data else None

    eligible_docs = islamic_deposit_data.eligibility_docs.all() if islamic_deposit_data else []
    for doc in eligible_docs:
        # Access the title and description from the related `EligibilityDocsSection`
        section = doc.section if hasattr(doc, 'section') else None
    
    eligible_docs_title = section.title if eligible_docs else None
    eligible_docs_desc = section.description if eligible_docs else None
    faqs = islamic_deposit_data.faq_islamic_recurring.all() if islamic_deposit_data else []
    promo_banner = islamic_deposit_data.promo_banner if islamic_deposit_data else None

    footer_image = islamic_deposit_data.footer_section if islamic_deposit_data else None
    footer = islamic_deposit_data.footer_section.links.all() if islamic_deposit_data else None
    
  
    return render(request, 'islamic_recurring_deposit.html', {'hero_sections': hero_accounts,'navbar_data':navbar_data,'subnav_items': subnav_items,'navigation_logo_url':navigation_main.logo.url,'tabs_promo':tabs_promo,'eligible_docs':eligible_docs,'eligible_docs_title':eligible_docs_title,'eligible_docs_desc':eligible_docs_desc,'faqs':faqs,'promo_banner':promo_banner,'footer_image':footer_image,'footer':footer})

def islamic_supply_finance(request):

    supply_finance_data = SupplyChainFinancePage.objects.first()    
    navigation_main = supply_finance_data.navbar
    navbar_items = navigation_main.navbar.prefetch_related('sub_tabs__links')
    navbar_data = [
        {
            'main_item': item,
            'sub_tabs': [
                {
                    'sub_tab': sub_tab,
                    'links': list(sub_tab.links.all())
                }
                for sub_tab in item.sub_tabs.all()
            ],
        }
        for item in navbar_items
    ]
    subnav = supply_finance_data.subnav if supply_finance_data else None
    subnav_items = []
    
    if subnav:
     
        subnav_items = subnav.navbar.all()


    hero_accounts = supply_finance_data.hero_sections if supply_finance_data else None
    tabs_promo = supply_finance_data.tab_section.all() if supply_finance_data else None
    faqs = supply_finance_data.faq_islamic_recurring.all() if supply_finance_data else []
    row_promo_1 = supply_finance_data.row_promo_1 if supply_finance_data else None 
    row_promo_2 = supply_finance_data.row_promo_2 if supply_finance_data else None
    footer_image = supply_finance_data.footer_section if supply_finance_data else None
    footer = supply_finance_data.footer_section.links.all() if supply_finance_data else None
    
    return render(request, 'supply_finance.html', {'hero_sections': hero_accounts,'navbar_data':navbar_data,'subnav_items': subnav_items,'navigation_logo_url':navigation_main.logo.url,'tabs_promo':tabs_promo,'row_promo_1':row_promo_1,'row_promo_2':row_promo_2,'faqs':faqs,'footer_image':footer_image,'footer':footer})

def women_service_view(request):

    women_service = WomenServicesPage.objects.first()    
    navigation_main = women_service.navbar
    navbar_items = navigation_main.navbar.prefetch_related('sub_tabs__links')
    navbar_data = [
        {
            'main_item': item,
            'sub_tabs': [
                {
                    'sub_tab': sub_tab,
                    'links': list(sub_tab.links.all())
                }
                for sub_tab in item.sub_tabs.all()
            ],
        }
        for item in navbar_items
    ]
    subnav = women_service.subnav if women_service else None
    subnav_items = []
    
    if subnav:
     
        subnav_items = subnav.navbar.all()



    hero_accounts = women_service.hero_sections if women_service else None
    faqs_data = women_service.faq_islamic.all() if women_service else []
    promo_banner = women_service.promo_banner if women_service else None

    footer_image = women_service.footer_section if women_service else None
    footer = women_service.footer_section.links.all() if women_service else None
    
    return render(request, 'women_service.html', {'hero_sections': hero_accounts,'navbar_data':navbar_data,'subnav_items': subnav_items,'navigation_logo_url':navigation_main.logo.url,'faqs_data':faqs_data,'promo_banner':promo_banner,'footer_image':footer_image,'footer':footer})

def alfa_bnpl_view(request):

    alfa_bnpl = AlfaBNPL.objects.first()  
    navigation_main = alfa_bnpl.navbar
    navbar_items = navigation_main.navbar.prefetch_related('sub_tabs__links')
    navbar_data = [
        {
            'main_item': item,
            'sub_tabs': [
                {
                    'sub_tab': sub_tab,
                    'links': list(sub_tab.links.all())
                }
                for sub_tab in item.sub_tabs.all()
            ],
        }
        for item in navbar_items
    ]  
    subnav = alfa_bnpl.subnav if alfa_bnpl else None
    subnav_items = []
    
    if subnav:
     
        subnav_items = subnav.navbar.all()



    hero_accounts = alfa_bnpl.hero_sections if alfa_bnpl else None
    tabs_promo = alfa_bnpl.tab_section.all() if alfa_bnpl else None
    green_promo = alfa_bnpl.green_cta_promo if alfa_bnpl else None
    tile_promo = alfa_bnpl.tile_promo.tile_promo_items.all() if alfa_bnpl else None
    tile_promo_title = alfa_bnpl.tile_promo.title if alfa_bnpl else None  # Title of TilePromoSection
    faq_islamic_nested = alfa_bnpl.faq_islamic_nested if alfa_bnpl else None
    footer_image = alfa_bnpl.footer_section if alfa_bnpl else None
    footer = alfa_bnpl.footer_section.links.all() if alfa_bnpl else None

    return render(request, 'alfa_bnpl.html', {'hero_sections': hero_accounts,'navbar_data':navbar_data,'subnav_items': subnav_items,'navigation_logo_url':navigation_main.logo.url,'tile_promo_title':tile_promo_title,'tiles_promo_data':tile_promo,'green_promo_data':green_promo,'faq_islamic_nested_data':faq_islamic_nested,'tabs_promo':tabs_promo,'footer_image':footer_image,'footer':footer})

def islamic_about_us(request):

    about_us = AboutUsIslamic.objects.first()    
    hero_accounts = about_us.hero_sections if about_us else None
    text_promo = about_us.text_data if about_us else None
    acc_features = about_us.image_text_promo.all() if about_us else []
    green_promo = about_us.green_cta_promo if about_us else None
    navigation_main = about_us.navbar
    navbar_items = navigation_main.navbar.prefetch_related('sub_tabs__links')
    navbar_data = [
        {
            'main_item': item,
            'sub_tabs': [
                {
                    'sub_tab': sub_tab,
                    'links': list(sub_tab.links.all())
                }
                for sub_tab in item.sub_tabs.all()
            ],
        }
        for item in navbar_items
    ]

    subnav = about_us.subnav if about_us else None
    subnav_items = []
    
    if subnav:
     
        subnav_items = subnav.navbar.all()


   
    if about_us.file_faq_section:
    
    
    # Build `files_faq` structure
        files_faq = [
        {
            'title': about_us.file_faq_section.title,
            'categories': [
                {
                    'header': category.header,
                    'questions': [
                        {
                            'file_name': question.file_name,
                            'small_desc': question.small_desc,
                            'file_cta_text': question.file_cta_text,
                            'file_cta_url': question.file_cta_url,
                        }
                        for question in category.file_faq_question_answers.all()
                    ],
                }
                for category in about_us.file_faq_section.file_faq_categories.all()
            ],
        }
    ]

    else:
        files_faq = []

    
    
    promo_banner = about_us.promo_banner if about_us else None
    footer_image = about_us.footer_section if about_us else None
    footer = about_us.footer_section.links.all() if about_us else None
    

    return render(request, 'islamic-about-us.html', {'hero_sections': hero_accounts,'navbar_data':navbar_data,'subnav_items': subnav_items,'navigation_logo_url':navigation_main.logo.url,'text_promo':text_promo,'green_promo_data':green_promo,'files_faq':files_faq,'acc_features':acc_features,'promo_banner':promo_banner,'footer_image':footer_image,'footer':footer})

def islamic_misc(request,section):


    titles_mapping = {
    "islamic_accidents": "Free Takaful Coverage for Accidents, Household Events & Wallet Protection",
    "islamic_coverage": "Coverage Limits",
    "islamic-accident-faq":"FAQs: Free Personal Accident & Household Takaful Coverage",
    "islamic-nostro":"Nostro Accounts",
    "islamic-takaful-claims":"Takaful Claims",
    "islamic-treasury":"Treasury",
    }



    if section in titles_mapping:
        islamic_misc = IslamicMisc.objects.get(title=titles_mapping[section])
        

    hero_accounts = islamic_misc.hero_sections if islamic_misc else None    
    green_promo = islamic_misc.green_cta_promo.faq_items_golden.all() if islamic_misc.green_cta_promo else None
    isl_table_1 = islamic_misc.isl_table_1 if islamic_misc.isl_table_1 else []
    isl_table_2 = islamic_misc.isl_table_2 if islamic_misc.isl_table_2 else []
    isl_orbit_data = islamic_misc.isl_promo_orbit.orbit_promo.all() if islamic_misc.isl_promo_orbit else []
    isl_zigzag_data = islamic_misc.isl_zigzag.all() if islamic_misc else []
    footer_image = islamic_misc.footer_section if islamic_misc else None
    footer = islamic_misc.footer_section.links.all() if islamic_misc else None
    navigation_main = islamic_misc.navbar
    navbar_items = navigation_main.navbar.prefetch_related('sub_tabs__links')
    navbar_data = [
        {
            'main_item': item,
            'sub_tabs': [
                {
                    'sub_tab': sub_tab,
                    'links': list(sub_tab.links.all())
                }
                for sub_tab in item.sub_tabs.all()
            ],
        }
        for item in navbar_items
    ]
    subnav = islamic_misc.subnav if islamic_misc else None
    subnav_items = []
    
    if subnav:
     
        subnav_items = subnav.navbar.all()



    # Fetch DBGPages instance and related data in a single query
    islamic_misc_full_text = IslamicMisc.objects.filter(title=titles_mapping[section]).select_related(
        'isl_full_text',
        'isl_full_text_2',
        'isl_full_text_3',
        'isl_full_text_4'
    ).prefetch_related(
        'isl_full_text__dbg_full_entries',
        'isl_full_text_2__dbg_full_entries',
        'isl_full_text_3__dbg_full_entries',
        'isl_full_text_4__dbg_full_entries'
    ).first()
    
    # Prepare data for the first text section
    isl_full_text_data = []
    if islamic_misc_full_text and islamic_misc_full_text.isl_full_text:
        isl_full_text_data = [
            {
                "heading": entry.main_heading,
                "description": entry.main_description,
            }
            for entry in islamic_misc_full_text.isl_full_text.dbg_full_entries.all()
        ]

    # Prepare data for the second text section
    isl_full_text_2_data = []
    if islamic_misc_full_text and islamic_misc_full_text.isl_full_text_2:
        isl_full_text_2_data = [
            {
                "heading": entry.main_heading,
                "description": entry.main_description,
            }
            for entry in islamic_misc_full_text.isl_full_text_2.dbg_full_entries.all()
        ]
    isl_full_text_3_data = []
    if islamic_misc_full_text and islamic_misc_full_text.isl_full_text_3:
        isl_full_text_3_data = [
            {
                "heading": entry.main_heading,
                "description": entry.main_description,
            }
            for entry in islamic_misc_full_text.isl_full_text_3.dbg_full_entries.all()
        ]
    isl_full_text_4_data = []
    if islamic_misc_full_text and islamic_misc_full_text.isl_full_text_4:
        isl_full_text_4_data = [
            {
                "heading": entry.main_heading,
                "description": entry.main_description,
            }
            for entry in islamic_misc_full_text.isl_full_text_4.dbg_full_entries.all()
        ]
    faq_data = []
    if islamic_misc.isl_faq:
        faq_data = [
            {
                'faq_section': {'title': islamic_misc.isl_faq.title},
                'question': item.question,
                'answer': item.answer,
            }
            for item in islamic_misc.isl_faq.faq_items.all()
        ]



    entries = []
    if islamic_misc.isl_col_text and islamic_misc.isl_col_text.dbg_col_entries.exists():  # Ensure related entries exist
        entries = [
            {
                "column1": {
                    "heading": entry.main_heading_column1,
                    "description": entry.main_description_column1,
                },
                "column2": {
                    "heading": entry.main_heading_column2,
                    "description": entry.main_description_column2,
                },
            }
            for entry in islamic_misc.isl_col_text.dbg_col_entries.all()
        ]
    
    entries_2_col = []
    if islamic_misc.isl_col_text_2 and islamic_misc.isl_col_text_2.dbg_col_entries.exists():  # Ensure related entries exist
        entries_2_col = [
            {
                "column1": {
                    "heading": entry.main_heading_column1,
                    "description": entry.main_description_column1,
                },
                "column2": {
                    "heading": entry.main_heading_column2,
                    "description": entry.main_description_column2,
                },
            }
            for entry in islamic_misc.isl_col_text_2.dbg_col_entries.all()
        ]
    
   
    if islamic_misc.title == 'Free Takaful Coverage for Accidents, Household Events & Wallet Protection':

        return render(request, 'islamic_takaful_accident.html', {'hero_sections': hero_accounts,'navbar_data':navbar_data,'subnav_items': subnav_items,'navigation_logo_url':navigation_main.logo.url,'orbit_promo':isl_orbit_data,'acc_features': isl_zigzag_data,"dbg_full_text_2": isl_full_text_2_data,"dbg_full_text": isl_full_text_data,'golden_prem_promo':green_promo,'footer_image':footer_image,'footer':footer})
    elif islamic_misc.title == 'Coverage Limits':
      
        return render(request, 'islamic_coverage_limits.html', {'hero_sections': hero_accounts,'navbar_data':navbar_data,'subnav_items': subnav_items,'navigation_logo_url':navigation_main.logo.url,'table_promo_1':isl_table_1,'table_promo_2':isl_table_2,"dbg_full_text_2": isl_full_text_2_data,"dbg_full_text": isl_full_text_data,'footer_image':footer_image,'footer':footer})

    elif islamic_misc.title == 'FAQs: Free Personal Accident & Household Takaful Coverage':
      
        return render(request, 'islamic_faq_accident.html', {'hero_sections': hero_accounts,'navbar_data':navbar_data,'subnav_items': subnav_items,'navigation_logo_url':navigation_main.logo.url,'faqs': faq_data,'footer_image':footer_image,'footer':footer})

    elif islamic_misc.title == 'Nostro Accounts':
      
        return render(request, 'islamic_nostro.html', {'hero_sections': hero_accounts,'navbar_data':navbar_data,'subnav_items': subnav_items,'navigation_logo_url':navigation_main.logo.url,'table_promo_1':isl_table_1,'footer_image':footer_image,'footer':footer})

    elif islamic_misc.title == 'Takaful Claims':
       
        return render(request, 'islamic_takaful_claims.html', {'hero_sections': hero_accounts,'navbar_data':navbar_data,'subnav_items': subnav_items,'navigation_logo_url':navigation_main.logo.url,"dbg_full_text_4": isl_full_text_4_data,"dbg_full_text_3": isl_full_text_3_data,"dbg_full_text_2": isl_full_text_2_data,"dbg_full_text": isl_full_text_data,'footer_image':footer_image,'footer':footer})

    elif islamic_misc.title == 'Treasury':
       
        return render(request, 'islamic_treasury.html', {'hero_sections': hero_accounts,'navbar_data':navbar_data,'subnav_items': subnav_items,'navigation_logo_url':navigation_main.logo.url,'col_entries_2':entries_2_col,'col_entries':entries,'footer_image':footer_image,'footer':footer})


    
