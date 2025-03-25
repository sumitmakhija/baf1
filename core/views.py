from django.shortcuts import render
from .models import *
from bs4 import BeautifulSoup
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
import pandas as pd
import os

def strip_ul_tags(description):
    soup = BeautifulSoup(description, 'html.parser')
    lis = soup.find_all('li')
    return ''.join(str(li) for li in lis)

def hero_section_view(request, section):
    if section == 'digital':
        hero_section = HeroSection.objects.get(title='Digital Account Hero Section')  # Example query
        
    elif section == 'current':
        hero_section = HeroSection.objects.get(title='Current Account Hero Section')  # Example query
    else:
        hero_section = None  # Handle default or error case

    return render(request, 'hero_section.html', {'hero_section': hero_section})

def homepage_view(request):
    # Assuming there is only one Homepage instance
    homepage = Homepage.objects.first()
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
    return render(request, 'home.html', {'hero_slider_sections': hero_slider_sections,
    'subnav_items': subnav_items,
    'navbar_data':navbar_data,'navigation_logo_url':navigation_main.logo.url,'account_promo':account_promo,'news_updates':updates_slider,'offers_promo':offers_promo, 'financial_solution_promos': financial_solution_promos,'promo_banner': promo_banner,'banking_promos': banking_promos,'footer':footer,'footer_image':footer_image})

def accounts_view(request):
    # Assuming there is only one Homepage instance
    accounts = AccountsPage.objects.first()
    hero_accounts = accounts.hero_sections if accounts else None
    accounts_promo_all = accounts.accounts_promo_all if accounts else None
    faqs = accounts.faq.all() if accounts else []

    # Get the navbar data
    navigation_main = accounts.navbar
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
    subnav = accounts.subnav if accounts else None
    subnav_items = []
    
    if subnav:
     
        subnav_items = subnav.navbar.all()
    footer = accounts.footer_section.links.all() if accounts else None
    footer_image = accounts.footer_section if accounts else None
    return render(request, 'accounts_lp.html', {'hero_sections': hero_accounts,
    'subnav_items': subnav_items,
    'navigation_logo_url':navigation_main.logo.url,'navbar_data':navbar_data,'accounts_promo': accounts_promo_all,'faqs':faqs,'footer':footer,'footer_image':footer_image})

def accountsdetail_view(request,section):
 
    titles_mapping = {
    "pehchaan": "Bank Alfalah Pehchaan Current Account",
    "kashtkaar": "Bank Alfalah Kashtkaar Current Account",
    "kamyabkarobar": "Bank Alfalah Kamyab Karobar",
    "pkrcurrent": "Bank Alfalah PKR Current Account",
    "basicbanking": "Bank Alfalah Basic Banking Account",
    "asaancurrent": "Bank Alfalah Asaan Current Account",
    "asaanremitt": "Bank Alfalah Asaan Remittance Current Account",
    "fcycurrent": "Bank Alfalah FCY Current Account",
    "fcysaving": "FCY Monthly Savings Account",
    "pehchansaving": "Bank Alfalah Pehchaan Savings Account",
    "saving": "Bank Alfalah Savings Account",
    "kifayat": "Bank Alfalah Kifayat Account",
    "seniorcitizen": "Bank Alfalah Care Senior Citizen Account",
    "royalprofit": "Bank Alfalah Royal Profit Account",
    "asaansaving": "Bank Alfalah Asaan Savings Account",
    "cscamdan": "Bank Alfalah Care Senior Citizen Mahana Amdan Account",
    "floatingdeposit": "Bank Alfalah Floating Term Deposit",
    "termdeposit": "Bank Alfalah Term Deposit",
    "mahanaamdan": "Bank Alfalah Mahana Amdan Term Deposit Account",
    "foreigncurrency": "Bank Alfalah Foreign Currency Fixed Account",
    "asaan_dig_saving": "Bank Alfalah Asaan Digital Savings Account",
    "asaan_remitt_current": "Bank Alfalah Asaan Remittance Digital Account – Current",
    "asaan_digit_current": "Bank Alfalah Asaan Digital Current Account",
    "freelancer_digital": "Bank Alfalah Freelancer Digital Savings Account",
    "asaan_pehchan_digital": "Bank Alfalah Asaan Pehchaan Digital Account",
    "freelancer_digital_saving": "Bank Alfalah Freelancer Digital Account – Savings"
    }

    if section in titles_mapping:
        accounts_detail = AccountDetails.objects.get(title=titles_mapping[section])

    hero_accounts = accounts_detail.hero_sections if accounts_detail else None
    acc_features = accounts_detail.account_features.all() if accounts_detail else []
    promo_banner = accounts_detail.promo_banner if accounts_detail else None
    promo_banner_full = accounts_detail.promo_banner_full if accounts_detail else None
    footer_image = accounts_detail.footer_section if accounts_detail else None
    footer = accounts_detail.footer_section.links.all() if accounts_detail else None
    # Get the related `EligibilityDocsSection` for each `EligibilityDocTile`
    eligible_docs = accounts_detail.eligibility_docs.all() if accounts_detail else []
    # Get the navbar data
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


    for doc in eligible_docs:
        # Access the title and description from the related `EligibilityDocsSection`
        section = doc.section
    eligible_docs_title = section.title
    eligible_docs_desc = section.description
    
    return render(request, 'acc_details_lp.html', {'hero_sections': hero_accounts,'subnav_items': subnav_items,'navigation_logo_url':navigation_main.logo.url,'navbar_data':navbar_data,'acc_features': acc_features,'promo_banner':promo_banner,'eligible_docs':eligible_docs,'eligible_docs_title':eligible_docs_title,'eligible_docs_desc':eligible_docs_desc,'promo_banner_full':promo_banner_full,'footer':footer,'footer_image':footer_image})

def careers_view(request):
    careers = Careers.objects.first()
    hero_careers = careers.hero_sections if careers else None
    careers_features = careers.careers_features.all() if careers else []
    careers_red_box_promo = careers.red_box_promo.entries.all() if careers else None
    maangement_promo = careers.management_promo if careers else None
    footer = careers.footer_section.links.all() if careers else None
    footer_image = careers.footer_section if careers else None

    navigation_main = careers.navbar
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
    subnav = careers.subnav if careers else None
    subnav_items = []
    
    if subnav:
        
        subnav_items = subnav.navbar.all()
    return render(request,'careers.html',{'hero_sections': hero_careers,'navigation_logo_url':navigation_main.logo.url,'navbar_data':navbar_data,'footer':footer,'footer_image':footer_image,'acc_features': careers_features,'promo_box':careers_red_box_promo,'offers_promo':maangement_promo,'subnav_items': subnav_items})

def aboutus_view(request):
    about_us = AboutUs.objects.first()
    hero_aboutus = about_us.hero_sections if about_us else None
    aboutus_features = about_us.aboutus_features.all() if about_us else []
    modal_promo = about_us.modal_promo if about_us else None
    vision_mission = about_us.vision_mission_promo.entries.all() if about_us.vision_mission_promo else []
    footer = about_us.footer_section.links.all() if about_us else None
    footer_image = about_us.footer_section if about_us else None
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
    return render(request,'about_us.html',{'hero_sections': hero_aboutus,'navigation_logo_url':navigation_main.logo.url,'navbar_data':navbar_data,'footer':footer,'footer_image':footer_image,'acc_features': aboutus_features,'modal_promo': modal_promo,'vision_mission_promo':vision_mission,'subnav_items': subnav_items})

def awards_view(request):
    # Assuming there is only one Homepage instance
    awards = AwardsPage.objects.first()
    hero_awards = awards.hero_sections if awards else None
    faqs_awards = awards.awards_promo.all() if awards else []
    footer = awards.footer_section.links.all() if awards else None
    footer_image = awards.footer_section if awards else None

    navigation_main = awards.navbar
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

    subnav = awards.subnav if awards else None
    subnav_items = []
    
    if subnav:
        
        subnav_items = subnav.navbar.all()
    return render(request, 'awards_lp.html', {'hero_sections': hero_awards,'navigation_logo_url':navigation_main.logo.url,'navbar_data':navbar_data,'faqs':faqs_awards,'footer':footer,'footer_image':footer_image,'subnav_items': subnav_items})

def career_ops_view(request):
    # Assuming there is only one Homepage instance
    career_ops = CareersOpportunityPage.objects.first()
    hero_sections = career_ops.hero_sections if career_ops else []
    financial_solution_promos = career_ops.programs.all() if career_ops else []
    hr_promo = career_ops.hr_promo if career_ops else []
    footer = career_ops.footer_section.links.all() if career_ops else None
    footer_image = career_ops.footer_section if career_ops else None
    navigation_main = career_ops.navbar
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
    subnav = career_ops.subnav if career_ops else None
    subnav_items = []
    
    if subnav:
        subnav_items = subnav.navbar.all()
    
    return render(request, 'career_opprtunities.html', {'hero_sections': hero_sections,'navigation_logo_url':navigation_main.logo.url,'navbar_data':navbar_data, 'financial_solution_promos': financial_solution_promos,'hr_promo':hr_promo,'footer':footer,'footer_image':footer_image,'subnav_items': subnav_items})

def jobs_view(request):
    # Assuming there is only one Homepage instance
    # Assuming there is only one Homepage instance
    jobs_obj = JobsLP.objects.first()
    hero_sections = jobs_obj.hero_sections if jobs_obj else []
    jobs_promo = jobs_obj.jobs.jobs.all() if jobs_obj and jobs_obj.jobs else []  # Access jobs from the related JobsPage
    footer = jobs_obj.footer_section.links.all() if jobs_obj else None
    footer_image = jobs_obj.footer_section if jobs_obj else None
    navigation_main = jobs_obj.navbar
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
    subnav = jobs_obj.subnav if jobs_obj else None
    subnav_items = []
    
    if subnav:
        subnav_items = subnav.navbar.all()
  
    return render(request, 'jobs_lp.html', {'hero_sections': hero_sections,'navigation_logo_url':navigation_main.logo.url,'navbar_data':navbar_data,'jobs_promo':jobs_promo,'footer':footer,'footer_image':footer_image,'subnav_items': subnav_items})

def group_reports_by_year(report_type, grouped_reports_dict):
    for card in report_type.cards_reports.all():
        year = card.year if card.year else 'Unknown'
        if year not in grouped_reports_dict:
            grouped_reports_dict[year] = []
        grouped_reports_dict[year].append(card)

def financial_reports_view(request):
    # Assuming there is only one FinancialReportsPage instance
    financial_reports = FinancialReportsPage.objects.first()
    
    # Get hero sections and reports tab if available
    hero_accounts = financial_reports.hero_sections if financial_reports else None
    reports_tab = financial_reports.reports_promo if financial_reports else None
    footer = financial_reports.footer_section.links.all() if financial_reports else None
    footer_image = financial_reports.footer_section if financial_reports else None

    navigation_main = financial_reports.navbar
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
    subnav = financial_reports.subnav if financial_reports else None
    subnav_items = []
    
    if subnav:
        subnav_items = subnav.navbar.all()
    # Initialize dictionaries for grouping reports
    grouped_reports = {}
    grouped_reports_analyst = {}
    grouped_reports_capital = {}
    grouped_reports_corporate = {}
    grouped_reports_credit = {}
    grouped_reports_material = {}
    grouped_reports_unclaimed = {}

    # Dictionary to map report types to their corresponding group
    report_type_mapping = {
        'Annual Reports': grouped_reports,
        'Analyst Briefing': grouped_reports_analyst,
        'Capital Adequacy Ratio': grouped_reports_capital,
        'Best Corporate Report': grouped_reports_corporate,
        'Credit Rating': grouped_reports_credit,
        'Material Information': grouped_reports_material,
        'Unclaimed Deposits': grouped_reports_unclaimed,
    }

    # Group reports by year for each type
    if reports_tab:
        for report_type in reports_tab.report_types.all():
            if report_type.type in report_type_mapping:
                group_reports_by_year(report_type, report_type_mapping[report_type.type])

    # Render the template with context data
    context = {
        'navbar_data': navbar_data,
        'navigation_logo_url':navigation_main.logo.url,
        'hero_sections': hero_accounts,
        'reports_tab': reports_tab,
        'grouped_reports': grouped_reports,
        'grouped_reports_analyst': grouped_reports_analyst,
        'grouped_reports_capital': grouped_reports_capital,
        'grouped_reports_corporate': grouped_reports_corporate,
        'grouped_reports_credit': grouped_reports_credit,
        'grouped_reports_material': grouped_reports_material,
        'grouped_reports_unclaimed': grouped_reports_unclaimed,
        'footer': footer,
        'footer_image': footer_image,
        'subnav_items': subnav_items,
    }

    return render(request, 'financial_report.html', context)

def election_dir_views(request):
    # Assuming there is only one Homepage instance
    election_obj = ElectionDirectorsPage.objects.first()
    hero_sections = election_obj.hero_sections if election_obj else []
    reports_tab = election_obj.election_promo if election_obj else None
    footer = election_obj.footer_section.links.all() if election_obj else None
    footer_image = election_obj.footer_section if election_obj else None
    navigation_main = election_obj.navbar
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
    subnav = election_obj.subnav if election_obj else None
    subnav_items = []
    
    if subnav:
        subnav_items = subnav.navbar.all()
    return render(request, 'election_directors.html', {'hero_sections': hero_sections,'navbar_data':navbar_data,'navigation_logo_url':navigation_main.logo.url,'reports_tab':reports_tab,'footer':footer,'footer_image':footer_image,'subnav_items': subnav_items})

def branch_locator_view(request):
    branch = BranchPage.objects.first()
    navigation_main = branch.navbar
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
    subnav = branch.subnav if branch else None
    subnav_items = []
    
    if subnav:
        subnav_items = subnav.navbar.all()

    hero_sections = branch.hero_sections if branch else []
    footer = branch.footer_section.links.all() if branch else None
    footer_image = branch.footer_section if branch else None
    return render(request, 'branch_locator.html', {'hero_sections': hero_sections,'navbar_data':navbar_data,'navigation_logo_url':navigation_main.logo.url,'footer':footer,'footer_image':footer_image,'subnav_items': subnav_items})

def article_page_View(request):
    article = ArticlePage.objects.first()
    navigation_main = article.navbar
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
    subnav = article.subnav if article else None
    subnav_items = []   
    
    if subnav:
        subnav_items = subnav.navbar.all()
    hero_sections = article.hero_sections if article else []
    article_content = article.article_section if article else []
    footer = article.footer_section.links.all() if article else None
    footer_image = article.footer_section if article else None
    return render(request, 'article.html', {'hero_sections': hero_sections,'navbar_data':navbar_data,'navigation_logo_url':navigation_main.logo.url,'article_content':article_content,'footer':footer,'footer_image':footer_image,'subnav_items': subnav_items})

def investors_view(request):
    investor = Investors.objects.first()
    navigation_main = investor.navbar
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
    subnav = investor.subnav if investor else None
    subnav_items = []   
    
    if subnav:
        subnav_items = subnav.navbar.all()
    hero_sections = investor.hero_sections if investor else []
    investor_promo = investor.investor_promo.all() if investor else []
    footer = investor.footer_section.links.all() if investor else None
    footer_image = investor.footer_section if investor else None
    return render(request, 'investors.html', {'hero_sections': hero_sections,'navbar_data':navbar_data,'navigation_logo_url':navigation_main.logo.url,'investor_promo':investor_promo,'footer':footer,'footer_image':footer_image,'subnav_items': subnav_items})

def leadership_view(request):
    leaders = LeadershipPage.objects.first()
    navigation_main = leaders.navbar
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
    subnav = leaders.subnav if leaders else None
    subnav_items = []   

    if subnav:
        subnav_items = subnav.navbar.all()
    hero_sections = leaders.hero_sections if leaders else []
    investor_promo = leaders.team_promo.all() if leaders else []
    footer = leaders.footer_section.links.all() if leaders else None
    footer_image = leaders.footer_section if leaders else None
    return render(request, 'leadership.html', {'hero_sections': hero_sections,'navbar_data':navbar_data,'navigation_logo_url':navigation_main.logo.url,'investor_promo':investor_promo,'footer':footer,'footer_image':footer_image,'subnav_items': subnav_items})

def media_view(request):
    media_view = MediaPage.objects.first()
    navigation_main = media_view.navbar
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
    subnav = media_view.subnav if media_view else None
    subnav_items = []   

    if subnav:
        subnav_items = subnav.navbar.all()
    hero_sections = media_view.hero_sections if media_view else []
    media_tabs = media_view.media_tabs_promo.all() if media_view else []
    footer = media_view.footer_section.links.all() if media_view else None
    footer_image = media_view.footer_section if media_view else None

    return render(request, 'media.html', {'hero_sections': hero_sections,'navbar_data':navbar_data,'navigation_logo_url':navigation_main.logo.url,'media_tabs':media_tabs,'footer':footer,'footer_image':footer_image,'subnav_items': subnav_items})

def wrap_description_in_div(description):
    # Split content at the <span> tags
    sections = description.split('<span')
    wrapped_content_1 = ""
    wrapped_content_2 = ""
    count = 0

    for section in sections:
        if section.strip():  # Only process non-empty sections
            count += 1
            wrapped_section = f'<div class="compnayDetailsInner"><span{section}</div>'

            # Add the first 7 sections to wrapped_content_1, and the rest to wrapped_content_2
            if count <= 7:
                wrapped_content_1 += wrapped_section
            else:
                wrapped_content_2 += wrapped_section

    return wrapped_content_1, wrapped_content_2

def company_profile_view(request):
    company_profile = CompanyProfile.objects.first()
    navigation_main = company_profile.navbar
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
    subnav = company_profile.subnav if company_profile else None
    subnav_items = []
    
    if subnav:
        subnav_items = subnav.navbar.all()
    hero_sections = company_profile.hero_sections if company_profile else []
    vision_mission = company_profile.vision_mission_promo.entries.all() if company_profile.vision_mission_promo else []
    associated_companies = company_profile.companies_promo.entries_comp.all() if company_profile.companies_promo else []
    company_info = company_profile.company_detail if company_profile.company_detail else []
    table_promo = company_profile.company_table_promo if company_profile.company_table_promo else []
    if company_info:
        status_description = company_info.status_description
        processed_description, processed_description_2 = wrap_description_in_div(status_description)
    else:
        processed_description = ''
        processed_description_2 = ''

    footer = company_profile.footer_section.links.all() if company_profile else None
    footer_image = company_profile.footer_section if company_profile else None

    return render(request, 'company_profile.html', {'hero_sections': hero_sections,'navbar_data':navbar_data,'navigation_logo_url':navigation_main.logo.url,'vision_mission_promo':vision_mission,
                                                    'associated_companies':associated_companies,'processed_description':processed_description,
                                                    'table_promo':table_promo,'processed_description_2':processed_description_2,'company_info':company_info,'footer':footer,'footer_image':footer_image,'subnav_items': subnav_items})

def governance_view(request):

    governance_view = GovernancePage.objects.first()
    navigation_main = governance_view.navbar
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
    subnav = governance_view.subnav if governance_view else None
    subnav_items = []
    
    if subnav:
        subnav_items = subnav.navbar.all()
    hero_sections = governance_view.hero_sections if governance_view else []
    directors =  governance_view.team_promo.all() if governance_view else []
    legal_persons = governance_view.legal_promo if governance_view else []
    grev_promo = governance_view.grievance_promo if governance_view else []
    footer = governance_view.footer_section.links.all() if governance_view else None
    footer_image = governance_view.footer_section if governance_view else None

    return render(request, 'governance.html', {'hero_sections': hero_sections,'navbar_data':navbar_data,'navigation_logo_url':navigation_main.logo.url,'grev_promo':grev_promo,'legal_persons':legal_persons,'directors':directors,'footer':footer,'footer_image':footer_image,'subnav_items': subnav_items})

def links_view(request):

    links = QuickLinks.objects.first()
    navigation_main = links.navbar
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
    subnav = links.subnav if links else None
    subnav_items = []
    
    if subnav:
        subnav_items = subnav.navbar.all()

    hero_sections = links.hero_sections if links else []
    shareholding_table = links.shareholding_info if links.shareholding_info else []
    others_table = links.others_info if links.others_info else []
    footer = links.footer_section.links.all() if links else None
    footer_image = links.footer_section if links else None

    return render(request, 'quick_links.html', {'hero_sections': hero_sections,'navbar_data':navbar_data,'shareholding_table':shareholding_table,'navigation_logo_url':navigation_main.logo.url,
                                               'others_table':others_table,'footer':footer,'footer_image':footer_image,'subnav_items': subnav_items})

def contact_us_view(request):
    contact_us = ContactUs.objects.first()
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
    hero_sections = contact_us.hero_sections if contact_us else []
    vision_mission = contact_us.vision_mission_promo.entries.all() if contact_us.vision_mission_promo else []
    contact_info = contact_us.contact_info.all() if contact_us.contact_info else []
    footer = contact_us.footer_section.links.all() if contact_us else None
    footer_image = contact_us.footer_section if contact_us else None

    return render(request, 'contact_us.html',{'hero_sections': hero_sections,'navbar_data':navbar_data,'navigation_logo_url':navigation_main.logo.url,'vision_mission_promo':vision_mission,
                                                    'contact_info':contact_info,'footer':footer,'footer_image':footer_image,'subnav_items': subnav_items})

def investor_relation_view(request):
    investor = InvestorRelation.objects.first()

    navigation_main = investor.navbar
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
    subnav = investor.subnav if investor else None
    subnav_items = []
    
    if subnav:
        subnav_items = subnav.navbar.all()
    hero_sections = investor.hero_sections if investor else []
    article_content = investor.article_section if investor else []
    grev_promo = investor.grievance_promo if investor else []
    footer = investor.footer_section.links.all() if investor else None
    footer_image = investor.footer_section if investor else None

    return render(request, 'investor_relation.html',{'hero_sections': hero_sections,'navbar_data':navbar_data,'navigation_logo_url':navigation_main.logo.url,'grev_promo':grev_promo,'secp_promo':article_content,'footer':footer,'footer_image':footer_image,'subnav_items': subnav_items})

@csrf_exempt
def submit_complaint_form(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)
        customer_name = data.get('customer_name')
        customer_email = data.get('customer_email')
        customer_contact_no = data.get('customer_contact_no')
        customer_contact_no_landline = data.get('customer_contact_no_landline')
        customer_contact_acc_no = data.get('customer_contact_acc_no')
        customer_city = data.get('customer_city')
        product_detail = data.get('product_detail')
        complaint_detail = data.get('complaint_detail')
        # Save data in the model
        complaint = ComplaintFormData(
            customer_name=customer_name,
            customer_email=customer_email,
            customer_contact_no=customer_contact_no,
            customer_contact_no_landline=customer_contact_no_landline,
            customer_contact_acc_no=customer_contact_acc_no,
            customer_city=customer_city,
            product_detail=product_detail,
            complaint_detail=complaint_detail
        )
        complaint.save()

        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def submit_fraud_form(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        customer_name = data.get('customer_name')
        customer_email = data.get('customer_email')
        customer_cnic = data.get('customer_cnic')
        customer_transaction_date = data.get('customer_transaction_date')
        customer_transaction_amt = data.get('customer_transaction_amt')
        customer_acct_amt = data.get('customer_acct_amt')
        customer_contact = data.get('customer_contact')
        customer_remarks = data.get('customer_remarks')
        complaint_detail = data.get('complaint_detail')
        # Save data in the model
        fraud = FraudulentFundTransferComplaint(
            customer_name=customer_name,
            email=customer_email,
            cnic_no=customer_cnic,
            transaction_date = customer_transaction_date,
            transaction_amount=customer_transaction_amt,
            account_amount=customer_acct_amt,
            contact_no=customer_contact,
            customer_remarks=customer_remarks,
            other_information=complaint_detail
        )
        fraud.save()

        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def employee_application_form(request):
    try:
        # Get the employment application page configuration
        employment_page = EmploymentApplicationPage.objects.first()
        navigation_main = employment_page.navbar
        footer = employment_page.footer_section.links.all() if employment_page else None
        footer_image = employment_page.footer_section if employment_page else None
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
        subnav = employment_page.subnav if employment_page else None
        subnav_items = []
        
        if subnav:
            subnav_items = subnav.navbar.all()
        # If no configuration exists, create a default context
        if not employment_page:
            return render(request, 'employment_application.html')
        
        # Create context with navbar and footer
        context = {
            'title': employment_page.title,
            'navigation_logo_url': employment_page.navbar.logo.url if employment_page.navbar and employment_page.navbar.logo else None,
            'navbar_data': navbar_data,
            'footer':footer,'footer_image':footer_image,'subnav_items': subnav_items
        }
        
        # Add hero section if available
     
        
        return render(request, 'employment_application.html', context)
    except Exception as e:
        # Fallback to basic rendering if any error occurs

        return render(request, 'employment_application.html')

@csrf_exempt
def submit_employment_application(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.POST.get('data'))
            cv_file = request.FILES.get('cv_file')
            
            # Extract education and experience data
            additional_education = {}
            additional_experience = {}
            
            # Process the first education entry (default fields in the model)
            education_data = {
                'qualification': data.get('qualification[1]', ''),
                'institution': data.get('institution[1]', ''),
                'additional_certification': data.get('additional_certification[1]', ''),
                'education_start_date': data.get('education_start_date[1]', ''),
                'education_end_date': data.get('education_end_date[1]', ''),
                'education_in_process': data.get('education_in_process[1]', False)
            }
            
            # Process the first experience entry (default fields in the model)
            experience_data = {
                'industry_type': data.get('industry_type[1]', ''),
                'designation': data.get('designation[1]', ''),
                'organization': data.get('organization[1]', ''),
                'job_tenure_from': data.get('job_tenure_from[1]', ''),
                'job_tenure_to': data.get('job_tenure_to[1]', ''),
                'job_tenure_in_process': data.get('job_tenure_in_process[1]', False)
            }
            
            # Extract additional education entries (index > 1)
            for key in data.keys():
                # Process education entries
                if key.startswith('qualification[') and not key.endswith('[1]'):
                    index = key.split('[')[1].split(']')[0]
                    if index != '1':  # Skip the first entry as it's stored in the main fields
                        if index not in additional_education:
                            additional_education[index] = {}
                        additional_education[index]['qualification'] = data[key]
                
                if key.startswith('institution[') and not key.endswith('[1]'):
                    index = key.split('[')[1].split(']')[0]
                    if index != '1':
                        if index not in additional_education:
                            additional_education[index] = {}
                        additional_education[index]['institution'] = data[key]
                
                if key.startswith('additional_certification[') and not key.endswith('[1]'):
                    index = key.split('[')[1].split(']')[0]
                    if index != '1':
                        if index not in additional_education:
                            additional_education[index] = {}
                        additional_education[index]['additional_certification'] = data[key]
                
                if key.startswith('education_start_date[') and not key.endswith('[1]'):
                    index = key.split('[')[1].split(']')[0]
                    if index != '1':
                        if index not in additional_education:
                            additional_education[index] = {}
                        additional_education[index]['education_start_date'] = data[key]
                
                if key.startswith('education_end_date[') and not key.endswith('[1]'):
                    index = key.split('[')[1].split(']')[0]
                    if index != '1':
                        if index not in additional_education:
                            additional_education[index] = {}
                        additional_education[index]['education_end_date'] = data[key]
                
                if key.startswith('education_in_process[') and not key.endswith('[1]'):
                    index = key.split('[')[1].split(']')[0]
                    if index != '1':
                        if index not in additional_education:
                            additional_education[index] = {}
                        additional_education[index]['education_in_process'] = data[key] == 'on'
                
                # Process experience entries
                if key.startswith('industry_type[') and not key.endswith('[1]'):
                    index = key.split('[')[1].split(']')[0]
                    if index != '1':  # Skip the first entry as it's stored in the main fields
                        if index not in additional_experience:
                            additional_experience[index] = {}
                        additional_experience[index]['industry_type'] = data[key]
                
                if key.startswith('designation[') and not key.endswith('[1]'):
                    index = key.split('[')[1].split(']')[0]
                    if index != '1':
                        if index not in additional_experience:
                            additional_experience[index] = {}
                        additional_experience[index]['designation'] = data[key]
                
                if key.startswith('organization[') and not key.endswith('[1]'):
                    index = key.split('[')[1].split(']')[0]
                    if index != '1':
                        if index not in additional_experience:
                            additional_experience[index] = {}
                        additional_experience[index]['organization'] = data[key]
                
                if key.startswith('job_tenure_from[') and not key.endswith('[1]'):
                    index = key.split('[')[1].split(']')[0]
                    if index != '1':
                        if index not in additional_experience:
                            additional_experience[index] = {}
                        additional_experience[index]['job_tenure_from'] = data[key]
                
                if key.startswith('job_tenure_to[') and not key.endswith('[1]'):
                    index = key.split('[')[1].split(']')[0]
                    if index != '1':
                        if index not in additional_experience:
                            additional_experience[index] = {}
                        additional_experience[index]['job_tenure_to'] = data[key]
                
                if key.startswith('job_tenure_in_process[') and not key.endswith('[1]'):
                    index = key.split('[')[1].split(']')[0]
                    if index != '1':
                        if index not in additional_experience:
                            additional_experience[index] = {}
                        additional_experience[index]['job_tenure_in_process'] = data[key] == 'on'
            
            # Convert additional_education and additional_experience to lists for better storage
            additional_education_list = list(additional_education.values()) if additional_education else None
            additional_experience_list = list(additional_experience.values()) if additional_experience else None
            
            application = EmploymentApplication(
                full_name=data['full_name'],
                email=data['email'],
                mobile_number=data['mobile_number'],
                cnic=data['cnic'],
                date_of_birth=data['date_of_birth'],
                emergency_number=data['emergency_number'],
                address=data['address'],
                city=data['city'],
                
                # First education entry
                qualification=education_data['qualification'],
                institution=education_data['institution'],
                additional_certification=education_data['additional_certification'],
                education_start_date=education_data['education_start_date'],
                education_end_date=education_data['education_end_date'],
                education_in_process=education_data['education_in_process'],
                
                # First experience entry
                industry_type=experience_data['industry_type'],
                designation=experience_data['designation'],
                organization=experience_data['organization'],
                job_tenure_from=experience_data['job_tenure_from'],
                job_tenure_to=experience_data['job_tenure_to'],
                job_tenure_in_process=experience_data['job_tenure_in_process'],
                
                # Additional entries
                additional_education=additional_education_list,
                additional_experience=additional_experience_list,
                
                cv_file=cv_file
            )
            application.save()
            
            return JsonResponse({
                'status': 'success',
                'message': 'Application submitted successfully'
            })
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)