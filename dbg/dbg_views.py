from django.shortcuts import render
from dbg.models import *
from django.db.models import Prefetch
# Create your views here.

def dbg_pages_view(request,section):

    titles_mapping = {
    "dbg-tpl": "FAQ’s – Hospital Cash Assist by TPL Life",
    "dbg-faqs":"DBQ Faqs",
    "dbg-voice-faqs":"DBG Voice-Bio FAQ",
    "dbg-alfa-faqs":"FAQ Alfa Term Deposit",
    "dbg-unionpay-faqs":"Bank Alfalah Wallet Unionpay Debit Card",
    "dbg-workhall":"Work Hall",
    "dbg-premo":"Premo By Xander’s",
    "dbg-keyfacts":"Key Facts Statements",
    "dbg-alfa":"Alfa",
    "dbg-sms":"SMS Banking",
    "dbg-raast":"RAAST Pakistan’s First Instant Payment System",
    "dbg-alfachat":"AlfaChat",
    "dbg-keyfacts-alfachat":"Key Facts Statements Alfa Chat",   
    "dbg-keyfacts-goalbased":"Key Facts Statements Goal Based Saving", 
    "dbg-alfa-account":"Alfa Account",
    "dbg-keyfacts-alfaaccount":"Key Facts Statements Alfa Account",
    "dbg-keyfacts-alfasaving":"Key Facts Statements Alfa Saving Account",
    "dbg-alfasaving":"Alfa Saving Account",
    "dbg-atm-cdm":"ATM-CDM-CCDM",
    "dbg-digital-branch":"Digital Branch",
    "dbg-digital-services":"Digital Services",
    "dbg-vsm":"VSM – Virtual Services Machine",
    "dbg-goalbased":"Goal-Based Saving",
    "dbg-branchoutlook":"Branch Outlook",
    "dbg-orbits":"Bank Alfalah Orbit Rewards",
    "dbg-orbit-earn":"How to Earn Orbits",
    "dbg-alfamall":"Alfamall",
    "dbg-mutual-funds":"Mutual Funds",
    "dbg-eligibility":"Eligibility Criteria",
    "dbg-docs":"About Documents Requirement",
    "dbg-payment":"Alfa Payment Gateway",
    "dbg-charges":"Schedule of Charges",
    "dbg-onboarding":"On Boarding DBG",
    "dbg-alfa-qr":"Alfa QR",
    "dbg-personal":"Personal",
    "dbg-biz":"Business",
    "dbg-wallet-card":"Bank Alfalah Wallet Debit Cards",
    "dbg-unionpay":"Bank Alfalah Wallet UnionPay Debit Card",
    "dbg-whatsapp":"WhatsApp Banking",
    "dbg-alfa-biz-app":"Alfa Business App",
    "dbg-alfa-agent":"Bank Alfalah Agent Financing",
    "dbg-alfa-overdraft":"Alfa Overdraft",
    "dbg-instant-loan":"Bank Alfalah Instant Loan",
    "dbg-instant-card":"Instant Credit Card",
    "dbg-redeem-orbit":"How to redeem Orbits",
    "dbg-orbit-tiers":"Orbit Tiers",
    "dbg-alfa-efu":"Alfa Zindagi – Alfa Zindagi by EFU Life",
    "dbg-internet-banking":"Internet Banking",
    "dbg-dfd":"DFD – Digital Facilitation Desk",
    "dbg-alfa-remit":"Alfa Remittance Account",
    "dbg-hospital":"Hospital Cash Assist by TPL Life",
    "dbg-education-fee":"Alfa Education Fee Payments",
    "dbg-virtual-card":"Virtual Debit Card",
    "dbg-gateway-customer":"Alfa Payment Gateway – Customer",
    "dbg-voice-bio":"Voice Biometrics",
    "dbg-transaction-insurance":"Alfa Transaction Insurance",
    "dbg-alfa-deposit":"Alfa Term Deposit",
    "dbg-ecommerce":"Alfa Payment Gateway – Your Business partner for Ecommerce Payments",
    "dbg-instant-loan-v2":"Bank Alfalah Instant Loan v2",
    "dbg-eobi":"EOBI",
    "dbg-accounts":"Digital Account Opening",
    "dbg-employee":"Employee Banking – The Bank Alfalah Way",
    "dbg-women-power":"Women Empowerment",
    "dbg-prize-bond":"Premium Prize Bond (Registered)",
    "dbg-insta-cash":"Bank Alfalah Insta Cash",
    "dbg-alfa-biz":"Alfa Business",
    "dbg-account-opening":"Account Opening Guideline and Checklist",
    "deposit-protection":"Deposit Protection Corporation – Public Awareness",
    "key-facts-accounts":"Key Facts Statements Accounts",
    "rda-nrp":"Roshan Digital Account (for NRPs)",
    "rda-pension":"Roshan Pension Plan",
    "rda-personal":"RDA Personal Account",
    "rda-biz":"RDA Business Accounts – Legal Entities",
    "rda-samaji":"Roshan Samaaji Khidmat",
    "naya-pakistan":"Naya Pakistan Certificates (for Roshan Digital Account Customers)",
    "psx-investments":"Investments in PSX",
    "key-facts-islamic":"Key Fact Statements Islamic",
    "roshan-car-calculator":"Roshan Apni Car Calculator",
    "roshan-apna-ghar":"RDA – Roshan Apna Ghar",
    "roshan-apni-car":"Bank Alfalah Roshan Apni Car for Roshan Digital Account Holders",
    "roshan-products-dbg":"Roshan Products",
    }




    if section in titles_mapping:
        dbg_page = DBGPages.objects.get(title=titles_mapping[section])
    
    hero_accounts = dbg_page.hero_sections if dbg_page else None
    text_section_data = dbg_page.dbg_text_section if dbg_page else None
    dbg_zigzag_data = dbg_page.dbg_zigzag.all() if dbg_page else []
    dbg_reports_tab = dbg_page.dbg_reports_promo if dbg_page else None
    dbg_table_1 = dbg_page.dbg_table_1 if dbg_page.dbg_table_1 else []
    dbg_table_2 = dbg_page.dbg_table_2 if dbg_page.dbg_table_2 else []
    dbg_table_3 = dbg_page.dbg_table_3 if dbg_page.dbg_table_3 else []
    dbg_table_4 = dbg_page.dbg_table_4 if dbg_page.dbg_table_4 else []
    dbg_table_5 = dbg_page.dbg_table_5 if dbg_page.dbg_table_5 else []
    key_facts = dbg_page.key_facts if dbg_page else None

    red_promo = dbg_page.red_promo.faq_items_golden.all() if dbg_page.red_promo else None
    red_promo_2 = dbg_page.red_promo_2.faq_items_golden.all() if dbg_page.red_promo_2 else None
    red_promo_3 = dbg_page.red_promo_3.faq_items_golden.all() if dbg_page.red_promo_3 else None


    cards_data = dbg_page.dbg_cards if dbg_page else None
    promo_banner = dbg_page.promo_banner if dbg_page else None
    promo_banner_full = dbg_page.promo_banner_full if dbg_page else None

    accounts_promo_all = dbg_page.dbg_accounts if dbg_page else None
    dbg_video_section = dbg_page.dbg_video if dbg_page.dbg_video else None
    faq_dbg_nested = dbg_page.dbg_faq_nested if dbg_page.dbg_faq_nested else None
    dbg_orbit_data = dbg_page.dbg_promo_orbit.orbit_promo.all() if dbg_page.dbg_promo_orbit else []
    
    dbg_accounts_promo = dbg_page.dbg_accounts_promo_all if dbg_page.dbg_accounts_promo_all else None

    footer_image = dbg_page.footer_section if dbg_page else None
    footer = dbg_page.footer_section.links.all() if dbg_page else None

    navigation_main = dbg_page.navbar
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
    subnav = dbg_page.subnav if dbg_page else None
    subnav_items = []
    
    if subnav:
        subnav_items = subnav.navbar.all()
    def get_feature_data(feature_promo):
        return {
            "title": feature_promo.title if feature_promo else None,
            "entries": [
                {"title": entry.title, "description": entry.description}
                for entry in feature_promo.features_box_entries.all()
            ]
        } if feature_promo else None


    # Fetch all services promos and their related entries
    def get_service_data(service_promo):
        return {
            "heading": service_promo.heading if service_promo else None,
            "entries": [
                {"name": entry.name, "logo": entry.logo.url if entry.logo else None}
                for entry in service_promo.service_entries.all()
            ]
        } if service_promo else None

    def get_box_data(box_promo):
        return {
            "heading": box_promo.heading if box_promo else None,
            "description": box_promo.description if box_promo else None,
            "entries": [
                {"name": entry.name, "logo": entry.logo.url if entry.logo else None}
                for entry in box_promo.service_entries.all()
            ]
        } if box_promo else None

    services_promo_1 = get_service_data(dbg_page.services_promo_1)
    services_promo_2 = get_service_data(dbg_page.services_promo_2)
    services_promo_3 = get_service_data(dbg_page.services_promo_3)
    services_promo_4 = get_service_data(dbg_page.services_promo_4)
    services_promo_5 = get_service_data(dbg_page.services_promo_5)
    services_promo_6 = get_service_data(dbg_page.services_promo_6)

    box_data = get_box_data(dbg_page.dbg_box_promo)
    box_data_2 = get_box_data(dbg_page.dbg_box_promo_2)
    box_data_3 = get_box_data(dbg_page.dbg_box_promo_3)

    tips_promo = get_service_data(dbg_page.dbg_tips)
    
    box_feature = get_feature_data(dbg_page.dbg_features)



    faq_data = []
    if dbg_page.dbg_faq:
        faq_data = [
            {
                'faq_section': {'title': dbg_page.dbg_faq.title},
                'question': item.question,
                'answer': item.answer,
            }
            for item in dbg_page.dbg_faq.faq_items.all()
        ]
    faq_data_2 = []
    if dbg_page.dbg_faq_2:
        faq_data_2 = [
            {
                'faq_section': {'title': dbg_page.dbg_faq_2.title},
                'question': item.question,
                'answer': item.answer,
            }
            for item in dbg_page.dbg_faq_2.faq_items.all()
        ]


    dbg_page = DBGPages.objects.prefetch_related(
        'dbg_file_faq_section__file_faq_categories__file_faq_question_answers'
    ).filter(title=titles_mapping[section]).first()

   
    if dbg_page.dbg_file_faq_section:
    
    
    # Build `files_faq` structure
        files_faq = [
        {
            'title': dbg_page.dbg_file_faq_section.title,
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
                for category in dbg_page.dbg_file_faq_section.file_faq_categories.all()
            ],
        }
    ]

    else:
        files_faq = []
    # Fetch DBGPages instance and related data in a single query
    dbg_page = DBGPages.objects.select_related('dbg_full_text').prefetch_related(
        'dbg_full_text__dbg_full_entries'
    ).filter(title=titles_mapping.get(section)).first()
    # Prepare data for the template
    dbg_full_text_data = []

    if dbg_page.dbg_full_text:
        dbg_full_text_data = [
            {
                "heading": entry.main_heading,
                "description": entry.main_description,
            }
            for entry in dbg_page.dbg_full_text.dbg_full_entries.all()
        ]

    dbg_page_full_text_2 = DBGPages.objects.select_related('dbg_full_text_2').prefetch_related(
        'dbg_full_text_2__dbg_full_entries'
    ).filter(title=titles_mapping.get(section)).first()
    # Prepare data for the template
    dbg_full_text_2_data = []

    if dbg_page.dbg_full_text_2:
        dbg_full_text_2_data = [
            {
                "heading": entry.main_heading,
                "description": entry.main_description,
            }
            for entry in dbg_page.dbg_full_text_2.dbg_full_entries.all()
        ]


    # If dbg_page exists, build the entries
    entries = []
    
    if dbg_page.dbg_col_text and dbg_page.dbg_col_text.dbg_col_entries.exists():  # Ensure related entries exist
        entries = [
            {   "title": dbg_page.dbg_col_text.heading,
                "column1": {
                    "heading": entry.main_heading_column1,
                    "description": entry.main_description_column1,
                },
                "column2": {
                    "heading": entry.main_heading_column2,
                    "description": entry.main_description_column2,
                },
            }
            for entry in dbg_page.dbg_col_text.dbg_col_entries.all()
        ]

    entries_2_col = []
    if dbg_page.dbg_col_text_2 and dbg_page.dbg_col_text_2.dbg_col_entries.exists():  # Ensure related entries exist
        entries_2_col = [
            {   "title": dbg_page.dbg_col_text_2.heading,
                "column1": {
                    "heading": entry.main_heading_column1,
                    "description": entry.main_description_column1,
                },
                "column2": {
                    "heading": entry.main_heading_column2,
                    "description": entry.main_description_column2,
                },
            }
            for entry in dbg_page.dbg_col_text_2.dbg_col_entries.all()
        ]
    entries_3_col = []
    if dbg_page.dbg_col_text_3 and dbg_page.dbg_col_text_3.dbg_col_entries.exists():  # Ensure related entries exist
        entries_3_col = [
            {   "title": dbg_page.dbg_col_text_3.heading,
                "column1": {
                    "heading": entry.main_heading_column1,
                    "description": entry.main_description_column1,
                },
                "column2": {
                    "heading": entry.main_heading_column2,
                    "description": entry.main_description_column2,
                },
            }
            for entry in dbg_page.dbg_col_text_3.dbg_col_entries.all()
        ]
    if dbg_page.dbg_full_text and dbg_page.dbg_full_text.heading in ["Alfa QR Text", "Personal","Business"]:
      
        return render(request, 'dbg_alfa_qr.html', {'hero_sections': hero_accounts,'key_facts':key_facts,'navbar_data':navbar_data,'subnav_items': subnav_items,'navigation_logo_url':navigation_main.logo.url,'col_entries_2':entries_2_col,'col_entries':entries,"dbg_full_text": dbg_full_text_data,'orbit_promo':dbg_orbit_data,'faq_prem_nested':faq_dbg_nested,'video_section': dbg_video_section,'accounts_promo': accounts_promo_all,'promo_banner':promo_banner,'cards_data':cards_data,'files_faq':files_faq,'golden_prem_promo_dup':red_promo_2,'golden_prem_promo':red_promo,'table_promo_1':dbg_table_1,'table_promo_2':dbg_table_2,'table_promo_3':dbg_table_3,'table_promo_4':dbg_table_4,'table_promo_5':dbg_table_5,'reports_tab':dbg_reports_tab,'acc_features': dbg_zigzag_data,'text_data':text_section_data,'faqs': faq_data,'footer':footer,'footer_image':footer_image})

    elif dbg_page.title == "Key Fact Statements Islamic":
        return render(request, 'islamic_key_facts.html', {'hero_sections': hero_accounts,'key_facts':key_facts,'navbar_data':navbar_data,'subnav_items': subnav_items,'navigation_logo_url':navigation_main.logo.url,'reports_tab':dbg_reports_tab,'footer':footer,'footer_image':footer_image})
    elif  dbg_page.title == "Alfa Education Fee Payments":
    
        return render(request, 'dbg_education_fee.html', {'hero_sections': hero_accounts,'key_facts':key_facts,'navbar_data':navbar_data,'subnav_items': subnav_items,'navigation_logo_url':navigation_main.logo.url,"dbg_full_text": dbg_full_text_data,'promo_banner':promo_banner,'footer':footer,'footer_image':footer_image})
    elif dbg_page.title == "Bank Alfalah Instant Loan v2":
 
        return render(request, 'dbg_instant_loan.html', {'hero_sections': hero_accounts,'navbar_data':navbar_data,'key_facts':key_facts,'subnav_items': subnav_items,'acc_features': dbg_zigzag_data,'faqs': faq_data,"dbg_full_text": dbg_full_text_data,'navigation_logo_url':navigation_main.logo.url,'col_entries':entries,'promo_banner':promo_banner,'footer':footer,'footer_image':footer_image})
    elif dbg_page.title == "Digital Account Opening":
        return render(request, 'dbg_accounts.html', {'hero_sections': hero_accounts,'key_facts':key_facts,'navbar_data':navbar_data,'subnav_items': subnav_items,'navigation_logo_url':navigation_main.logo.url,'accounts_promo': dbg_accounts_promo,'footer':footer,'footer_image':footer_image})
    elif dbg_page.title == "EOBI":
  
        return render(request, 'dbg_eobi.html', {'hero_sections': hero_accounts,'key_facts':key_facts,'navbar_data':navbar_data,'subnav_items': subnav_items,'navigation_logo_url':navigation_main.logo.url,'col_entries_2':entries_2_col,'col_entries':entries,"dbg_full_text": dbg_full_text_data,"dbg_full_text_2": dbg_full_text_2_data,'files_faq':files_faq,'footer':footer,'footer_image':footer_image})

    elif dbg_page.title == "Alfa Payment Gateway – Your Business partner for Ecommerce Payments":
        return render(request, 'dbg_alfa_payment_gateway.html', {'hero_sections': hero_accounts,'key_facts':key_facts,'subnav_items': subnav_items,'navbar_data':navbar_data,'navigation_logo_url':navigation_main.logo.url,'box_data_3':box_data_3,'box_data':box_data,'box_data_2':box_data_2,'col_entries_2':entries_2_col,'col_entries':entries,"dbg_full_text_2": dbg_full_text_2_data,"dbg_full_text": dbg_full_text_data,'table_promo_1':dbg_table_1,'text_data':text_section_data,'footer':footer,'footer_image':footer_image})

    elif dbg_page.title == "Account Opening Guideline and Checklist":
        return render(request, 'dbg_account_opening.html', {'hero_sections': hero_accounts,'key_facts':key_facts,'subnav_items': subnav_items,'navbar_data':navbar_data,'navigation_logo_url':navigation_main.logo.url,'col_entries_3':entries_3_col,'col_entries_2':entries_2_col,'col_entries':entries,"dbg_full_text": dbg_full_text_data,'footer':footer,'footer_image':footer_image})

    elif dbg_page.title == "Roshan Apni Car Calculator":
        return render(request, 'roshan_car_calculator.html', {'hero_sections': hero_accounts,"dbg_full_text": dbg_full_text_data,'subnav_items': subnav_items,'navbar_data':navbar_data,'navigation_logo_url':navigation_main.logo.url,'footer':footer,'footer_image':footer_image})
        
    

    else:
        print(dbg_full_text_2_data)
        return render(request, 'dbg_base.html', {'hero_sections': hero_accounts,'key_facts':key_facts,'subnav_items': subnav_items,'navigation_logo_url':navigation_main.logo.url,'navbar_data':navbar_data,'box_feature_data':box_feature,'tips_data':tips_promo,'box_data':box_data,'box_data_2':box_data_2,'col_entries_3':entries_3_col,'col_entries_2':entries_2_col,'col_entries':entries,"dbg_full_text_2": dbg_full_text_2_data,"dbg_full_text": dbg_full_text_data,'orbit_promo':dbg_orbit_data,'faq_prem_nested':faq_dbg_nested,'video_section': dbg_video_section,'accounts_promo': accounts_promo_all,'promo_banner_full':promo_banner_full,'promo_banner':promo_banner,'cards_data':cards_data,'files_faq':files_faq,'red_promo_3':red_promo_3,'golden_prem_promo_dup':red_promo_2,'golden_prem_promo':red_promo,'table_promo_1':dbg_table_1,'table_promo_2':dbg_table_2,'table_promo_3':dbg_table_3,'table_promo_4':dbg_table_4,'table_promo_5':dbg_table_5,'reports_tab':dbg_reports_tab,'acc_features': dbg_zigzag_data,'text_data':text_section_data,'faqs_2':faq_data_2,'faqs': faq_data, "services_promo_1": services_promo_1,
        "services_promo_2": services_promo_2,
        "services_promo_3": services_promo_3,
        "services_promo_4": services_promo_4,
        "services_promo_5": services_promo_5,
        "services_promo_6": services_promo_6,'footer':footer,'footer_image':footer_image})


def dbg_product_pages_view(request,section):

    titles_mapping = {
    "dbg-pfm": "Personal Finance Management",
    "dbg-bfilter":"B Filter",
    "dbg-ktrade":"K - Trade",
    "dbg-saylani":"Saylani Welfare via Alfa",
    }




    if section in titles_mapping:
        dbg_page = DBGPages.objects.get(title=titles_mapping[section])
    
    hero_accounts = dbg_page.hero_sections if dbg_page else None
    product_data = dbg_page.dbg_product_text if dbg_page else None
    dbg_zigzag_data = dbg_page.dbg_zigzag.all() if dbg_page else []

    footer_image = dbg_page.footer_section if dbg_page else None
    footer = dbg_page.footer_section.links.all() if dbg_page else None
    navigation_main = dbg_page.navbar
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
    subnav = dbg_page.subnav if dbg_page else None
    subnav_items = []
    
    if subnav:
     
        subnav_items = subnav.navbar.all()
       
    if dbg_page.title == "Personal Finance Management":
        return render(request, 'dbg_pfm.html', {'hero_sections': hero_accounts,'acc_features': dbg_zigzag_data,'subnav_items': subnav_items,'navigation_logo_url':navigation_main.logo.url,'navbar_data':navbar_data,'product_data':product_data,'footer':footer,'footer_image':footer_image,'navigation_logo_url':navigation_main.logo.url})
    
    elif dbg_page.title == "B Filter":
        return render(request, 'dbg_bfiler.html', {'hero_sections': hero_accounts,'acc_features': dbg_zigzag_data,'subnav_items': subnav_items,'navbar_data':navbar_data,'product_data':product_data,'footer':footer,'footer_image':footer_image,'navigation_logo_url':navigation_main.logo.url})
    
    elif dbg_page.title == "K - Trade":
        return render(request, 'dbg_ktrade.html', {'hero_sections': hero_accounts,'acc_features': dbg_zigzag_data,'subnav_items': subnav_items,'navbar_data':navbar_data,'product_data':product_data,'footer':footer,'footer_image':footer_image,'navigation_logo_url':navigation_main.logo.url})
    
    elif dbg_page.title == "Saylani Welfare via Alfa":

        return render(request, 'dbg_saylani.html', {'hero_sections': hero_accounts,'acc_features': dbg_zigzag_data,'subnav_items': subnav_items,'navbar_data':navbar_data,'product_data':product_data,'footer':footer,'footer_image':footer_image,'navigation_logo_url':navigation_main.logo.url})
                                                          
                                                        
