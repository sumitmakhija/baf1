from django.shortcuts import render
from .models import *
from itertools import groupby
from django.http import JsonResponse
# Create your views here.

def homepage_view(request):
    # Assuming there is only one Homepage instance
    homepage = Homepage.objects.first()
    hero_slider_sections = homepage.hero_slider_sections.all() if homepage else []
    account_promo = homepage.account_promo if homepage else None
    reports_tab = homepage.reports_promo if homepage else None
    offers_promo = homepage.offers_promo if homepage else None
    financial_solution_promos = homepage.financial_solution_promo.all() if homepage else []
    promo_banner = homepage.promo_banner if homepage else None
    banking_promos = homepage.banking_promo.all() if homepage else []
    footer = homepage.footer_section.links.all() if homepage else None
    footer_image = homepage.footer_section if homepage else None
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



    return render(request, 'premier_home.html', {'hero_slider_sections': hero_slider_sections,'navbar_data':navbar_data,'subnav_items': subnav_items,'navigation_logo_url':navigation_main.logo.url,'account_promo':account_promo,'reports_tab':reports_tab,'offers_promo':offers_promo, 'financial_solution_promos': financial_solution_promos,'promo_banner': promo_banner,'banking_promos': banking_promos,'footer':footer,'footer_image':footer_image})

def cards_promo_premier(request,section):
    
    titles_mapping = {
    "deposit-premier": "Deposit Accounts",
    "consumer-premier": "Consumer Banking",
    "islamic-premier-card":"Bank Alfalah Islamic Premier Cards",
    "sme-banking-prem": "SME/Commercial Banking",
    "prem-bancaktakaful":"Banca Takaful",
    
    }

    if section in titles_mapping:
        accounts_islamic = PremierCardsPromoPages.objects.get(title=titles_mapping[section])
    
    hero_accounts = accounts_islamic.hero_sections if accounts_islamic else None
    promo_banner = accounts_islamic.promo_banner if accounts_islamic else None
    cards_data = accounts_islamic.cards if accounts_islamic else None
    footer_image = accounts_islamic.footer_section if accounts_islamic else None
    footer = accounts_islamic.footer_section.links.all() if accounts_islamic else None
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




    return render(request, 'premier_cards_promo.html', {'hero_sections': hero_accounts,'navbar_data':navbar_data,'subnav_items': subnav_items,'navigation_logo_url':navigation_main.logo.url,'promo_banner':promo_banner,'cards_data':cards_data,'footer_image':footer_image,'footer':footer})

def prem_ind_accounts(request,section):
    
    titles_mapping = {
    "prem-current": "Bank Alfalah Islamic Premier Current Account",
    "prem-saving":"Bank Alfalah Islamic Premier Saving Account",
    "prem-fixed-deposit":"Bank Alfalah Islamic Premier Fixed Deposit Account",
    "prem-fcy":"Bank Alfalah Islamic Premier FCY Account",
    "prem-short-term":"Short Term Financing Solutions",
    "prem-long-term":"Long Term Financing Solutions",
    "prem-islamic-fleet":"Alfalah Islamic Fleet Finance",
    "prem-milkiat-finance":"Bank Alfalah Islamic Milkiat Finance",
    "prem-karobar-finance":"Bank Alfalah Islamic Karobar Finance",
    "prem-tahaffuz-takaful":"Tahaffuz Takaful Plan",
    "prem-tadbeer":"Tadbeer Multi-Purpose Savings Plan",
    "prem-uroos":"Uroos Marriage Plan",
    "prem-takaful-saving":"Zindagi Premier Takaful Saving Plan",
    "prem-zeenat":"Zeenat Takaful Plan",
    "prem-danish":"Bank Alfalah Danish Education Plan",
    "prem-mushkarah":"Bank Alfalah Home Musharakah",
    "prem-fast-track":"Fast Track and Customized Solutions",
    "prem-other-info":"Other Related Information",
    "prem-zamin":"Zaamin Takaful Plan",
    "prem-shifa":"Shifa Takaful Plan",
    "prem-auto-finance":"Bank Alfalah Islamic Auto Finance",
    
    
    }

    if section in titles_mapping:
        account_detail = PremierIndividualAccounts.objects.get(title=titles_mapping[section])
    
    hero_accounts = account_detail.hero_sections if account_detail else None
    navigation_main = account_detail.navbar
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
    subnav = account_detail.subnav if account_detail else None
    subnav_items = []
    
    if subnav:
     
        subnav_items = subnav.navbar.all()


    promo_banner = account_detail.promo_banner_full if account_detail else None
    acc_features = account_detail.account_features.all() if account_detail.account_features else []
    multi_col_faq = account_detail.multi_column_faq_section.faq_items.all() if account_detail.multi_column_faq_section else None
    golden_prem_promo = account_detail.golden_promo.faq_items_golden.all() if account_detail.golden_promo else None
    faq_prem_nested = account_detail.prem_faq_nested if account_detail else None
    card_detail_1 = account_detail.table_1_prem if account_detail.table_1_prem else []
    card_detail_2 = account_detail.table_2_prem if account_detail.table_2_prem else []
    text_promo = account_detail.text_promo if account_detail else None
    bullet_data = account_detail.bullet_features if account_detail else None
    financial_program_promo = account_detail.financial_program_promo  if account_detail else None
    footer_image = account_detail.footer_section if account_detail else None
    footer = account_detail.footer_section.links.all() if account_detail else None
   
    
    return render(request, 'premier_ind_acc_details.html', {'hero_sections': hero_accounts,'navbar_data':navbar_data,'subnav_items': subnav_items,'navigation_logo_url':navigation_main.logo.url,'faq_prem_nested':faq_prem_nested,'card_detail_1':card_detail_1,'card_detail_2':card_detail_2,'golden_prem_promo':golden_prem_promo,'multi_col_faq':multi_col_faq,'promo_banner_full':promo_banner,'acc_features':acc_features,'text_promo':text_promo,'bullet_data':bullet_data,'financial_program_promo':financial_program_promo,'footer_image':footer_image,'footer':footer})

def prem_visa_debit(request,section):
    
    titles_mapping = {
    "prem-visa": "Bank Alfalah Islamic Premier VISA Signature Debit Card",
    
    
    }
    if section in titles_mapping:
        account_detail = PremierIndividualAccounts.objects.get(title=titles_mapping[section])
    
    hero_accounts = account_detail.hero_sections if account_detail else None
    navigation_main = account_detail.navbar
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
    subnav = account_detail.subnav if account_detail else None
    subnav_items = []
    
    if subnav:
     
        subnav_items = subnav.navbar.all()



    promo_banner = account_detail.promo_banner_full if account_detail else None
    acc_features = account_detail.account_features.all() if account_detail.account_features else []
    multi_col_faq = account_detail.multi_column_faq_section.faq_items.all() if account_detail.multi_column_faq_section else None
    text_promo = account_detail.text_promo if account_detail else None


    footer_image = account_detail.footer_section if account_detail else None
    footer = account_detail.footer_section.links.all() if account_detail else None
   

    return render(request, 'premier_visa_debit.html', {'hero_sections': hero_accounts,'navbar_data':navbar_data,'subnav_items': subnav_items,'navigation_logo_url':navigation_main.logo.url,'multi_col_faq':multi_col_faq,'promo_banner_full':promo_banner,'acc_features':acc_features,'text_promo':text_promo,'footer_image':footer_image,'footer':footer})

def prem_contact_us(request):
    
    
    contact_us = ContactUsPage.objects.get(title='Contact Us Premier')
    navigation_main = contact_us.navbar
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
    subnav = contact_us.subnav if contact_us else None
    subnav_items = []
    
    if subnav:
     
        subnav_items = subnav.navbar.all()



    hero_accounts = contact_us.hero_sections if contact_us else None
    
    locations = Location.objects.all().order_by('region_name')  # Ensure ordered by region_name

    # Group locations by region
    grouped_locations = []
    for region, items in groupby(locations, key=lambda x: x.region_name):
        grouped_locations.append({
            'region_name': region,
            'contacts': list(items)
        })

    
    footer_image = contact_us.footer_section if contact_us else None
    footer = contact_us.footer_section.links.all() if contact_us else None
   

    return render(request, 'premier_contact_us.html', {
        'navigation_logo_url':navigation_main.logo.url,
        'subnav_items': subnav_items,
        'navbar_data':navbar_data,
        'hero_sections': hero_accounts,
        'footer_image': footer_image,
        'footer': footer,
        'grouped_locations': grouped_locations
    })
    
def prem_home_finance(request):
    try:
        # Fetch the HomeFinancePage object with the specified title
        home_finance = HomeFinancePage.objects.get(title='Bank Alfalah Home Finance')
        navigation_main = home_finance.navbar
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
        subnav = home_finance.subnav if home_finance else None
        subnav_items = []
        
        if subnav:
        
            subnav_items = subnav.navbar.all()


        # Retrieve related data if the HomeFinancePage object exists
        hero_accounts = home_finance.hero_sections if home_finance else None
        cards_data = home_finance.cards if home_finance else None
        multi_col_faq = home_finance.multi_column_faq_section.faq_items.all() if home_finance.multi_column_faq_section else None
        promo_banner = home_finance.promo_banner_full if home_finance else None
        footer_image = home_finance.footer_section if home_finance else None
        footer = home_finance.footer_section.links.all() if home_finance else None
        
        # Use the location_data field from HomeFinancePage to get related locations
        if home_finance.location_data:
            locations = home_finance.location_data.locations.all().order_by('region_name')  # Ensure ordered by region_name
            
            # Group locations by region
            grouped_locations = []
            for region, items in groupby(locations, key=lambda x: x.region_name):
                grouped_locations.append({
                    'region_name': region,
                    'contacts': list(items)
                })
        else:
            grouped_locations = []  # No locations available

        return render(request, 'home_finance_main.html', {
            'navigation_logo_url':navigation_main.logo.url,
            'subnav_items': subnav_items,
            'navbar_data':navbar_data,
            'hero_sections': hero_accounts,
            'cards_data': cards_data,
            'multi_col_faq': multi_col_faq,
            'promo_banner_full': promo_banner,
            'footer_image': footer_image,
            'footer': footer,
            'grouped_locations': grouped_locations
        })
    except HomeFinancePage.DoesNotExist:
        # Handle the case where the HomeFinancePage object is not found
        return JsonResponse({'error': 'The specified title was not found.'}, status=404)
    except Exception as e:
        # Catch any other exceptions and return an error message
        return JsonResponse({'error': f'An unexpected error occurred: {str(e)}'}, status=500)

def prem_financing_options(request,section):
    
    titles_mapping = {
    "prem-financing-options": "Financing Options",
    
    
    }
    if section in titles_mapping:
        financing_option = FinancingOptionPages.objects.get(title=titles_mapping[section])
    
    hero_accounts = financing_option.hero_sections if financing_option else None
    promo_banner = financing_option.promo_banner_full if financing_option else None
    acc_features = financing_option.account_features.all() if financing_option.account_features else []
    cards_data = financing_option.cards if financing_option else None
    table_promo = financing_option.table_1_prem if financing_option.table_1_prem else []
    steps_promo = financing_option.steps_promo if financing_option.steps_promo else None
    steps_data = financing_option.steps_promo.step_promo.all() if financing_option.steps_promo else []
    footer_image = financing_option.footer_section if financing_option else None
    footer = financing_option.footer_section.links.all() if financing_option else None
    navigation_main = financing_option.navbar
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
    subnav = financing_option.subnav if financing_option else None
    subnav_items = []
    
    if subnav:
    
        subnav_items = subnav.navbar.all()



    return render(request, 'financing_options.html', {'hero_sections': hero_accounts,'navbar_data':navbar_data,'subnav_items': subnav_items,'navigation_logo_url':navigation_main.logo.url,'steps_promo': steps_promo,'steps_data':steps_data,'table_data':table_promo,'acc_features':acc_features,'cards_data':cards_data,'promo_banner_full':promo_banner,'footer_image':footer_image,'footer':footer})

def prem_orbit_rewards(request,section):
    
    titles_mapping = {
    "prem-orbit-rewards": "Bank Alfalah Orbit Rewards",
    
    
    }
    if section in titles_mapping:
        orbit_reward = OrbitRewardPages.objects.get(title=titles_mapping[section])
    
    hero_accounts = orbit_reward.hero_sections if orbit_reward else None
    acc_features = orbit_reward.account_features.all() if orbit_reward.account_features else []
    faq_prem_nested = orbit_reward.prem_faq_nested if orbit_reward else None
    orbit_data = orbit_reward.orbit_promo.orbit_promo.all() if orbit_reward.orbit_promo else []
    footer_image = orbit_reward.footer_section if orbit_reward else None
    footer = orbit_reward.footer_section.links.all() if orbit_reward else None
    navigation_main = orbit_reward.navbar
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
   
    subnav = orbit_reward.subnav if orbit_reward else None
    subnav_items = []
    
    if subnav:
     
        subnav_items = subnav.navbar.all()

    return render(request, 'orbit_rewards.html', {'hero_sections': hero_accounts,'navbar_data':navbar_data,'subnav_items': subnav_items,'navigation_logo_url':navigation_main.logo.url,'orbit_promo':orbit_data,'faq_prem_nested':faq_prem_nested,'acc_features':acc_features,'footer_image':footer_image,'footer':footer})

def prem_miscellenous(request,section):
    
    titles_mapping = {
    "prem-eligibility": "Eligibility Criteria",
    "prem-top-notch":"Top Notch Alliance",
    "prem-fast-track":"Fast Track Services",
    "premier-airport-lounge":"Airport Lounges",
    "prem-spending-limits":"Higher Spending Limits",
    "prem-islamic-debit":"Islamic Premier Debit Card",
    "prem-sms":"Premier SMS Alerts",
    "prem-e-statements":"Premier e-statements",
    "prem-auto-loan":"Bank Alfalah Auto Loan",
    "prem-bancassurance":"Bancassurance",
    "prem-visa-signature-card":"Bank Alfalah Premier VISA Signature Debit Card",
    "prem-investment-services":"Investment Services",
    "prem-invest-goal":"Invest for Your Goals with Investment Services",
    "prem-self-service":"Self Service Banking",
    "prem-orbit-rewards-points":"Accelerated Orbit Reward Points",
    "prem-airport-lounge":"Premier Airport Lounges",
    "prem-islamic-banking":"Islamic Premier Banking",
    "prem-fee-waiver":"Fee Waivers and Benefits",
    "prem-complimentary-takaful":"Complimentary Takaful Coverage",
    "prem-alfa":"Alfa Premier",
    "prem-contact-center":"Contact Centre",
    "prem-internet-baking":"Internet Banking",
    "prem-atm-cdm":"Premier ATM / Cash & Cheque Deposit Machine",
    "prem-hikmat":"Hikmat Insurance Plan",
    "prem-lounge-access":"Premier Lounge Access and Benefits",
    }
    if section in titles_mapping:
        misc_page = MiscellenousPages.objects.get(title=titles_mapping[section])
    order_selection = misc_page.text_top if misc_page else None
    calculator = misc_page.show_calculator if misc_page else None
    hero_accounts = misc_page.hero_sections if misc_page else None
    table_promo = misc_page.table_1 if misc_page.table_1 else []
    table_promo_2 = misc_page.table_2 if misc_page.table_2 else []
    table_promo_3 = misc_page.table_3 if misc_page.table_3 else []

    text_promo = misc_page.all_text_data if misc_page else None
    text_promo_bottom = misc_page.all_text_data_bottom if misc_page else None

    acc_features = misc_page.account_features.all() if misc_page.account_features else []
    golden_prem_promo = misc_page.golden_promo.faq_items_golden.all() if misc_page.golden_promo else None
    multi_col_faq = misc_page.multi_column_faq_section.faq_items.all() if misc_page.multi_column_faq_section else None
    cards_data = misc_page.cards if misc_page else None
    promo_banner = misc_page.promo_banner if misc_page else None
    promo_banner_full = misc_page.promo_banner_full if misc_page else None
    logos_promo = misc_page.logos_promo if misc_page.logos_promo else None
    bullet_data = misc_page.bullet_features if misc_page else None
    branch_logo_promo = misc_page.branch_logo_promo if misc_page.branch_logo_promo else None

    footer_image = misc_page.footer_section if misc_page else None
    footer = misc_page.footer_section.links.all() if misc_page else None
    navigation_main = misc_page.navbar
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
    subnav = misc_page.subnav if misc_page else None
    subnav_items = []
    
    if subnav:
     
        subnav_items = subnav.navbar.all()



    misc_page = MiscellenousPages.objects.prefetch_related(
        'file_faq_section__file_faq_categories__file_faq_question_answers'
    ).filter(title=titles_mapping[section]).first()

   
    if misc_page.file_faq_section:
    
    
    # Build `files_faq` structure
        files_faq = [
        {
            'title': misc_page.file_faq_section.title,
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
                for category in misc_page.file_faq_section.file_faq_categories.all()
            ],
        }
    ]

    else:
        files_faq = []

    if misc_page.location_data:
        locations = misc_page.location_data.locations.all().order_by('region_name')  # Ensure ordered by region_name
        
        # Group locations by region
        grouped_locations = []
        for region, items in groupby(locations, key=lambda x: x.region_name):
            grouped_locations.append({
                'region_name': region,
                'contacts': list(items)
            })
    else:
        grouped_locations = []  # No locations available

    return render(request, 'misc_pages.html', {'hero_sections': hero_accounts,'navbar_data':navbar_data,'subnav_items': subnav_items,'navigation_logo_url':navigation_main.logo.url,'branch_logo_promo':branch_logo_promo,'grouped_locations': grouped_locations,'text_promo_bottom':text_promo_bottom,'bullet_data':bullet_data,'table_promo_3':table_promo_3,'table_promo_2':table_promo_2,'files_faq':files_faq,'lounge_promo_data':logos_promo,'cards_data':cards_data,'promo_banner_full':promo_banner_full,'promo_banner':promo_banner,'calculator':calculator,'golden_prem_promo':golden_prem_promo,'multi_col_faq':multi_col_faq,'order':order_selection,'acc_features':acc_features,'text_promo':text_promo,'table_promo':table_promo,'footer_image':footer_image,'footer':footer})

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def discount_privileges_conventional(request,section):
    
    titles_mapping = {
    "discounts": "Discounts and Privileges Conventional",
    
    
    }
    if section in titles_mapping:
        discounts = MiscellenousPages.objects.get(title=titles_mapping[section])
    
    hero_accounts = discounts.hero_sections if discounts else None
   
    footer_image = discounts.footer_section if discounts else None
    footer = discounts.footer_section.links.all() if discounts else None
    navigation_main = discounts.navbar
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
    subnav = discounts.subnav if discounts else None
    subnav_items = []
    
    if subnav:
     
        subnav_items = subnav.navbar.all()



    return render(request, 'discounts_privileges_con.html', {'hero_sections': hero_accounts,'navbar_data':navbar_data,'subnav_items': subnav_items,'navigation_logo_url':navigation_main.logo.url,'footer_image':footer_image,'footer':footer})

def discount_privileges_islamic(request,section):
    
    titles_mapping = {
    "discounts": "Discounts and Privileges Islamic",
    
    
    }
    if section in titles_mapping:
        discounts = MiscellenousPages.objects.get(title=titles_mapping[section])
    
    hero_accounts = discounts.hero_sections if discounts else None
   
    footer_image = discounts.footer_section if discounts else None
    footer = discounts.footer_section.links.all() if discounts else None
    navigation_main = discounts.navbar
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
    subnav = discounts.subnav if discounts else None
    subnav_items = []
    
    if subnav:
    
        subnav_items = subnav.navbar.all()

    return render(request, 'discounts_privileges_islamic.html', {'hero_sections': hero_accounts,'navbar_data':navbar_data,'subnav_items': subnav_items,'navigation_logo_url':navigation_main.logo.url,'footer_image':footer_image,'footer':footer})

def discount_privileges_premier(request,section):
    
    titles_mapping = {
    "discounts": "Discounts and Privileges Premier",
    
    
    }
    if section in titles_mapping:
        discounts = MiscellenousPages.objects.get(title=titles_mapping[section])
    
    hero_accounts = discounts.hero_sections if discounts else None
   
    footer_image = discounts.footer_section if discounts else None
    footer = discounts.footer_section.links.all() if discounts else None
    navigation_main = discounts.navbar
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
    subnav = discounts.subnav if discounts else None
    subnav_items = []
    
    if subnav:
    
        subnav_items = subnav.navbar.all()
    return render(request, 'discounts_privileges_premier.html', {'hero_sections': hero_accounts,'navbar_data':navbar_data,'subnav_items': subnav_items,'navigation_logo_url':navigation_main.logo.url,'footer_image':footer_image,'footer':footer})

	