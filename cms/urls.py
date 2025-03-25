"""
URL configuration for cms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import views
from islamic_core import islamic_views
from premier_core import premier_views
from dbg import dbg_views
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from core.views import submit_employment_application
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



admin.site.site_header = 'Bank Alfalah Website CMS'
admin.site.site_title = 'Bank Alfalah Website CMS'
admin.site.index_title = 'Welcome to Bank Alfalah Website CMS'

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', views.homepage_view, name='homepage'),
    path('accounts/', views.accounts_view, name='accounts_lp'),
    path('careers/',views.careers_view,name="careers"),
    path('about-bank-alfalah/',views.aboutus_view,name="about-us"),
    path('awards/',views.awards_view,name="awards"),
    path('careers/career-opportunities',views.career_ops_view,name="career_ops"),
    path('careers/career-opportunities/experienced-professionals/',views.jobs_view,name="jobs"),
    path('financial-reports/',views.financial_reports_view,name="reports"),
    path('election-of-directors/',views.election_dir_views,name="election"),
    path('branch-atm-locator/',views.branch_locator_view,name="branch"),
    path('press-release/',views.article_page_View,name="article_press"),
    path('investors/',views.investors_view,name="investors"),
    path('management/',views.leadership_view,name="leadership"),
    path('media/',views.media_view,name="media"),
    path('profile-of-company/',views.company_profile_view,name="profile"),
    path('governance/',views.governance_view,name="governance"),
    path('notice/',views.links_view,name="notices"),
    path('contact-us/',views.contact_us_view,name="contact_us"),
    path('investor-relations/',views.investor_relation_view,name="investor_relation"),
    path('submit-complaint-form/', views.submit_complaint_form, name='submit_complaint'),
    path('submit-fraud-form/', views.submit_fraud_form, name='submit_fraud'),
    path('personal-banking/current-account/alfalah-kashtkaar-current-account/', views.accountsdetail_view,{'section': 'kashtkaar'}, name='accounts'),
    path('personal-banking/deposit-accounts/alfalah-pehchaan-current-account/', views.accountsdetail_view,{'section': 'pehchaan'}, name='accounts'),
    path('personal-banking/deposit-accounts/current-accounts/alfalah-kamyab-karobar/', views.accountsdetail_view,{'section': 'kamyabkarobar'}, name='accounts'),
    path('personal-banking/deposit-accounts/current-accounts/alfalah-current-account/', views.accountsdetail_view,{'section': 'pkrcurrent'}, name='accounts'),
    path('personal-banking/deposit-accounts/current-accounts/alfalah-basic-banking-account/', views.accountsdetail_view,{'section': 'basicbanking'}, name='accounts'),
    path('personal-banking/deposit-accounts/current-accounts/alfalah-asaan-current-account/', views.accountsdetail_view,{'section': 'asaancurrent'}, name='accounts'),
    path('personal-banking/deposit-accounts/current-accounts/alfalah-asaan-remittance-current-account/', views.accountsdetail_view,{'section': 'asaanremitt'}, name='accounts'),
    path('personal-banking/deposit-accounts/current-accounts/alfalah-fcy-current-account/', views.accountsdetail_view,{'section': 'fcycurrent'}, name='accounts'),
    path('personal-banking/deposit-accounts/savings-account/alfalah-fcy-monthly-savings-account/', views.accountsdetail_view,{'section': 'fcysaving'}, name='accounts'),
    path('personal-banking/deposit-accounts/alfalah-pehchaan-savings-account/', views.accountsdetail_view,{'section': 'pehchansaving'}, name='accounts'),
    path('personal-banking/deposit-accounts/savings-account/alfalah-savings-account/', views.accountsdetail_view,{'section': 'saving'}, name='accounts'),
    path('personal-banking/deposit-accounts/savings-account/alfalah-kifayat-account/', views.accountsdetail_view,{'section': 'kifayat'}, name='accounts'),
    path('personal-banking/deposit-accounts/savings-account/alfalah-care-senior-citizen-account/', views.accountsdetail_view,{'section': 'seniorcitizen'}, name='accounts'),
    path('personal-banking/deposit-accounts/savings-account/alfalah-royal-profit-account/', views.accountsdetail_view,{'section': 'royalprofit'}, name='accounts'),
    path('personal-banking/deposit-accounts/savings-account/alfalah-asaan-savings-account/', views.accountsdetail_view,{'section': 'asaansaving'}, name='accounts'),
    path('personal-banking/deposit-accounts/fixed-accounts/alfalah-senior-citizen-mahana-amdan/', views.accountsdetail_view,{'section': 'cscamdan'}, name='accounts'),
    path('personal-banking/deposit-accounts/fixed-accounts/alfalah-floating-term-deposit/', views.accountsdetail_view,{'section': 'floatingdeposit'}, name='accounts'),
    path('personal-banking/deposit-accounts/fixed-accounts/term-deposit/', views.accountsdetail_view,{'section': 'termdeposit'}, name='accounts'),
    path('personal-banking/deposit-accounts/fixed-accounts/alfalah-mahana-amdani-account/', views.accountsdetail_view,{'section': 'mahanaamdan'}, name='accounts'),
    path('personal-banking/deposit-accounts/fixed-accounts/alfalah-foreign-currency-accounts/', views.accountsdetail_view,{'section': 'foreigncurrency'}, name='accounts'),
    path('digital-banking/bank-alfalah-asaan-remittance-digital-account-current/', views.accountsdetail_view,{'section': 'asaan_remitt_current'}, name='accounts'),
    path('personal-banking/deposit-accounts/digital-accounts/bank-alfalah-asaan-digital-current-account', views.accountsdetail_view,{'section': 'asaan_digit_current'}, name='accounts'),
    path('personal-banking/deposit-accounts/digital-accounts/bank-alfalah-assan-digital-saving-account/', views.accountsdetail_view,{'section': 'asaan_dig_saving'}, name='accounts'),
    path('personal-banking/deposit-accounts/digital-accounts/bank-alfalah-freelancer-digital-saving-account/', views.accountsdetail_view,{'section': 'freelancer_digital'}, name='accounts'),
    path('personal-banking/deposit-accounts/digital-accounts/bank-alfalah-assan-pehchaan-digital-account/', views.accountsdetail_view,{'section': 'asaan_pehchan_digital'}, name='accounts'),
    path('digital-banking/bank-alfalah-freelancer-digital-account-savings/', views.accountsdetail_view,{'section': 'freelancer_digital_saving'}, name='accounts'),
    path('employee-application/', views.employee_application_form),
    path('submit-employment-application/', submit_employment_application, name='submit_employment_application'),

    #Islamic URLS
    path('islamic/home/',islamic_views.homepage_view, name='home_isl'),

    path('islamic/debit-card/alfalah-visa-islamic-classic-debit-card/',islamic_views.accounts_detail_view_islamic,{'section': 'Foreign Currency Debit Card'}, name='accounts'),
    path('islamic/deposit-accounts/alfalah-islamic-asaan-remittance-savings-account/',islamic_views.accounts_detail_view_islamic,{'section': 'Bank Alfalah Islamic Asaan Remittance Savings Account'}, name='accounts'),
    path('islamic/deposit-accounts/alfalah-islamic-asaan-digital-remittance-savings-account/',islamic_views.accounts_detail_view_islamic,{'section': 'Bank Alfalah Islamic Asaan Digital Remittance Savings Account'}, name='accounts'),
    path('islamic/deposit-accounts/alfalah-islamic-asaan-women-digital-savings-account/',islamic_views.accounts_detail_view_islamic,{'section': 'Bank Alfalah Asaan Women Digital Savings Account'}, name='accounts'),
    path('islamic/deposit-accounts/alfalah-islamic-asaan-digital-savings-account/',islamic_views.accounts_detail_view_islamic,{'section': 'Bank Alfalah Islamic Asaan Digital Savings Account'}, name='accounts'),
    path('islamic/deposit-accounts/alfalah-islamic-senior-citizen-savings-account/',islamic_views.accounts_detail_view_islamic,{'section': 'Bank Alfalah Senior Citizens Savings Account'}, name='accounts'),
    path('islamic/deposit-accounts/alfalah-islamic-profex-account/',islamic_views.accounts_detail_view_islamic,{'section': 'Bank Alfalah Islamic Profex Account'}, name='accounts'),
    path('islamic/deposit-accounts/alfalah-islamic-mahana-amdani-account/',islamic_views.accounts_detail_view_islamic,{'section': 'Bank Alfalah Mahana Amdani Account'}, name='accounts'),
    path('islamic/deposit-accounts/alfalah-islamic-saving-account/',islamic_views.accounts_detail_view_islamic,{'section': 'Bank Alfalah Islamic Asaan Savings Account'}, name='accounts'),
    path('islamic/deposit-accounts/alfalah-business-account/',islamic_views.accounts_detail_view_islamic,{'section': 'Bank Alfalah Business Account'}, name='accounts'),
    path('islamic/deposit-accounts/alfalah-musharakah-saving-account/',islamic_views.accounts_detail_view_islamic,{'section': 'Bank Alfalah Musharakah Savings Account'}, name='accounts'),
    path('islamic/deposit-accounts/alfalah-foreign-currency-saving-account/',islamic_views.accounts_detail_view_islamic,{'section': 'Bank Alfalah Islamic Foreign Currency Savings Account'}, name='accounts'),
    path('islamic/deposit-accounts/alfalah-islamic-khayal-account/',islamic_views.accounts_detail_view_islamic,{'section': 'Bank Alfalah Islamic Khayaal Rakhna Account'}, name='accounts'),
    path('islamic/deposit-accounts/alfalah-senior-citizen-term-deposit-account/',islamic_views.accounts_detail_view_islamic,{'section': 'Bank Alfalah Islamic Senior Citizens Term Deposit'}, name='accounts'),
    path('islamic/deposit-accounts/alfalah-foreign-currency-termdeposit-account/',islamic_views.accounts_detail_view_islamic,{'section': 'Bank Alfalah Islamic Premium Term Deposits'}, name='accounts'),
    path('islamic/deposit-accounts/alfalah-3-year-termdeposit-account/',islamic_views.accounts_detail_view_islamic,{'section': 'Bank Alfalah 3 Year Term Deposit'}, name='accounts'),
    path('islamic/deposit-accounts/alfalah-mahana-munafa-termdeposit-account/',islamic_views.accounts_detail_view_islamic,{'section': 'Bank Alfalah Mahana Munafa Term Deposit'}, name='accounts'),
    path('islamic/deposit-accounts/alfalah-termdeposit-account/',islamic_views.accounts_detail_view_islamic,{'section': 'Bank Alfalah Term Deposits'}, name='accounts'),
    path('islamic/deposit-accounts/alfalah-islamic-premium-term-deposit-account/',islamic_views.accounts_detail_view_islamic,{'section': 'Bank Alfalah Islamic Foreign Currency Term Deposits'}, name='accounts'),
    path('islamic/deposit-accounts/alfalah-islamic-targert-saving-deposit-account/',islamic_views.accounts_detail_view_islamic,{'section': 'Target Savings Deposit'}, name='accounts'),
    path('islamic/deposit-accounts/alfalah-islamic-freelancer-digital-saving-account/',islamic_views.accounts_detail_view_islamic,{'section': 'Freelancer Digital Saving'}, name='accounts'),
    path('islamic/deposit-accounts/alfalah-islamic-basic-banking-account/',islamic_views.accounts_detail_view_islamic,{'section': 'Bank Alfalah Basic Banking Account'}, name='accounts'),
    path('islamic/deposit-accounts/alfalah-islamic-foreign-currency-current-account/',islamic_views.accounts_detail_view_islamic,{'section': 'Bank Alfalah Islamic Foreign Currency Current Account'}, name='accounts'),
    path('islamic/deposit-accounts/alfalah-islamic-asaan-digital-current-account/',islamic_views.accounts_detail_view_islamic,{'section': 'Bank Alfalah Islamic Asaan Digital Current Account'}, name='accounts'),
    path('islamic/deposit-accounts/alfalah-islamic-asaan-digital-remittance-current-account/',islamic_views.accounts_detail_view_islamic,{'section': 'Bank Alfalah Islamic Asaan Digital Remittance Current Account'}, name='accounts'),
    path('islamic/deposit-accounts/alfalah-islamic-asaan-digital-freelancer-current-account/',islamic_views.accounts_detail_view_islamic,{'section': 'Bank Alfalah Islamic Freelancer Digital Current Account'}, name='accounts'),
    path('islamic/deposit-accounts/alfalah-islamic-asaan-current-account/',islamic_views.accounts_detail_view_islamic,{'section': 'Bank Alfalah Islamic Asaan Current Account'}, name='accounts'),
    path('islamic/deposit-accounts/alfalah-islamic-asaan-remittance-current-account/',islamic_views.accounts_detail_view_islamic,{'section': 'Bank Alfalah Islamic Asaan Remittance Current Account'}, name='accounts'),
    path('islamic/deposit-accounts/alfalah-islamic-business-payroll-account/',islamic_views.accounts_detail_view_islamic,{'section': 'Bank Alfalah Islamic Business Way and Payroll'}, name='accounts'),
    path('islamic/deposit-accounts/alfalah-islamic-current-account/',islamic_views.accounts_detail_view_islamic,{'section': 'Bank Alfalah Islamic Current Account'}, name='accounts'),
    path('islamic/deposit-accounts/trade-services/',islamic_views.accounts_detail_view_islamic,{'section': 'Trade Services'}, name='accounts'),
    path('islamic/deposit-accounts/employee-banking/',islamic_views.accounts_detail_view_islamic,{'section': 'Employee Banking - Alfalah Islamic Business Way'}, name='accounts'),
    path('islamic/roshan-products/',islamic_views.accounts_detail_view_islamic,{'section': 'Roshan Products'}, name='accounts'),
    path('islamic/power-pack/',islamic_views.accounts_detail_view_islamic,{'section': 'Islamic Power Pack'}, name='accounts'),	
    path('islamic/digital-banking/',islamic_views.accounts_lp_view, name='accounts'),
    path('islamic-banking/smecommercial-banking/',islamic_views.cards_promo_islamic,{'section': 'sme'}, name='cards_promo'),
    path('islamic-banking/other-related-information/',islamic_views.cards_promo_islamic,{'section': 'other'}, name='cards_promo'),
    path('islamic-banking/sbp-schemes/',islamic_views.cards_promo_islamic,{'section': 'sbp'}, name='cards_promo'),
    path('islamic/digitalbanking/',islamic_views.cards_promo_islamic,{'section': 'digital-banking'}, name='cards_promo'),
    path('islamic-banking/banca-takaful/',islamic_views.cards_promo_islamic,{'section': 'takaful'}, name='cards_promo'),
    path('islamic-banking/consumer-banking/',islamic_views.cards_promo_islamic,{'section': 'consumer'}, name='cards_promo'),
    path('islamic-banking/corporate-banking/',islamic_views.cards_promo_islamic,{'section': 'corporate'}, name='cards_promo'),
    path('islamic-banking/treasury-capital-markets/treasury/',islamic_views.cards_promo_islamic,{'section': 'treasury'}, name='cards_promo'),
    path('islamic/debit-card/',islamic_views.debit_cards_promo_islamic,{'section': 'corporate'}, name='cards_promo'),
    path('islamic-banking/list-of-cdms-islamic/',islamic_views.cdm_page_view, name='cdm'),
    path('islamic-banking/gallery/',islamic_views.islamic_gallery,{'section': 'islamic-gallery'}, name='gallery'),
    path('islamic-banking/islamic-recurring-value/',islamic_views.islamic_recurring_deposit_page, name='recurring'),
    path('islamic-banking/supply-finance/',islamic_views.islamic_supply_finance, name='finance'),
    path('islamic-banking/women-service/',islamic_views.women_service_view, name='women_service'),
    path('islamic-banking/alfa_bnpl/',islamic_views.alfa_bnpl_view, name='alfa'),
    path('islamic-banking/about-us/',islamic_views.islamic_about_us, name='aboutus'),
    path('islamic-banking/accidents-takaful/',islamic_views.islamic_misc,{'section': 'islamic_accidents'}, name='islamic_accidents'),
    path('islamic-banking/coverage-limits/',islamic_views.islamic_misc,{'section': 'islamic_coverage'}, name='islamic_coverage'),
    path('islamic-banking/accidents-faq/',islamic_views.islamic_misc,{'section': 'islamic-accident-faq'}, name='islamic-accident-faq'),
    path('islamic-banking/nostro-accounts/',islamic_views.islamic_misc,{'section': 'islamic-nostro'}, name='islamic-nostro'),
    path('islamic-banking/takaful-claims/',islamic_views.islamic_misc,{'section': 'islamic-takaful-claims'}, name='islamic-takaful-claims'),
    path('islamic-banking/treasury/',islamic_views.islamic_misc,{'section': 'islamic-treasury'}, name='islamic-treasury'),



    #Premier URLS
    path('premier-banking/', premier_views.homepage_view, name='prem_homepage'),
    path('premier/deposit-accounts/', premier_views.cards_promo_premier,{'section': 'deposit-premier'}, name='prem_deposit'),
    path('premier/consumer-banking/', premier_views.cards_promo_premier,{'section': 'consumer-premier'}, name='prem_consumer'),
    path('premier/islamic-card/', premier_views.cards_promo_premier,{'section': 'islamic-premier-card'}, name='prem_isl_card'),
    path('premier/sme-commercial-banking/', premier_views.cards_promo_premier,{'section': 'sme-banking-prem'}, name='prem_sme'),
    path('premier/bancatakaful/', premier_views.cards_promo_premier,{'section': 'prem-bancaktakaful'}, name='prem_bancatkaaful'),
    path('premier/current-account/', premier_views.prem_ind_accounts,{'section': 'prem-current'}, name='prem_current'),
    path('premier/saving-account/', premier_views.prem_ind_accounts,{'section': 'prem-saving'}, name='prem_saving'),
    path('premier/fixed-deposit-account/', premier_views.prem_ind_accounts,{'section': 'prem-fixed-deposit'}, name='prem_fixed_deposit'),
    path('premier/fcy-account/', premier_views.prem_ind_accounts,{'section': 'prem-fcy'}, name='prem_fcy'),
    path('premier/short-term-financing/', premier_views.prem_ind_accounts,{'section': 'prem-short-term'}, name='prem_short_term'),
    path('premier/islamic-fleet-finance/', premier_views.prem_ind_accounts,{'section': 'prem-islamic-fleet'}, name='prem_fleet'),
    path('premier/milkiat-finance/', premier_views.prem_ind_accounts,{'section': 'prem-milkiat-finance'}, name='prem_milkiat'),
    path('premier/karobar-finance/', premier_views.prem_ind_accounts,{'section': 'prem-karobar-finance'}, name='prem_karobar'),
    path('premier/tahaffuz-takaful/', premier_views.prem_ind_accounts,{'section': 'prem-tahaffuz-takaful'}, name='prem_tahafuz'),
    path('premier/tadbeer-saving/', premier_views.prem_ind_accounts,{'section': 'prem-tadbeer'}, name='prem_tadbeer'),
    path('premier/uroos-marriage/', premier_views.prem_ind_accounts,{'section': 'prem-uroos'}, name='prem_uroos'),
    path('premier/takaful-saving/', premier_views.prem_ind_accounts,{'section': 'prem-takaful-saving'}, name='prem_takaful'),
    path('premier/zeenat/', premier_views.prem_ind_accounts,{'section': 'prem-zeenat'}, name='prem_zeenat'),
    path('premier/danish-education/', premier_views.prem_ind_accounts,{'section': 'prem-danish'}, name='prem_danish'),
    path('premier/home-mushkarah/', premier_views.prem_ind_accounts,{'section': 'prem-mushkarah'}, name='prem_mushkarah'),
    path('premier/fast-track/', premier_views.prem_ind_accounts,{'section': 'prem-fast-track'}, name='prem_fast'),
    path('premier/other-related/', premier_views.prem_ind_accounts,{'section': 'prem-other-info'}, name='prem_other_info'),
    path('premier/zamin/', premier_views.prem_ind_accounts,{'section': 'prem-zamin'}, name='prem-zamin'),
    path('premier/shifa/', premier_views.prem_ind_accounts,{'section': 'prem-shifa'}, name='prem-shifa'),
    path('premier/auto-finance/', premier_views.prem_ind_accounts,{'section': 'prem-auto-finance'}, name='prem-visa'),
    path('premier/visa-debit-signature/', premier_views.prem_visa_debit,{'section': 'prem-visa'}, name='prem-visa'),
    path('premier/contact-us/', premier_views.prem_contact_us, name='prem-contact-us'),
    path('premier/home-finance/', premier_views.prem_home_finance, name='prem-home-finance'),
    path('premier/financing-options/', premier_views.prem_financing_options,{'section': 'prem-financing-options'}, name='prem-financing-options'),
    path('premier/orbit-rewards/', premier_views.prem_orbit_rewards,{'section': 'prem-orbit-rewards'}, name='prem-orbit-rewards'),
    path('premier/eligibility-criteria/', premier_views.prem_miscellenous,{'section': 'prem-eligibility'}, name='prem-eligibility'),
    path('premier/top-alliance/', premier_views.prem_miscellenous,{'section': 'prem-top-notch'}, name='prem-top-notch'),
    path('premier/fast-track-service/', premier_views.prem_miscellenous,{'section': 'prem-fast-track'}, name='prem-fast-track'),
    path('premier/airport-lounge/', premier_views.prem_miscellenous,{'section': 'premier-airport-lounge'}, name='premier-airport-lounge'),
    path('premier/spending-limits/', premier_views.prem_miscellenous,{'section': 'prem-spending-limits'}, name='prem-spending-limits'),
    path('premier/islamic-debit-card/', premier_views.prem_miscellenous,{'section': 'prem-islamic-debit'}, name='prem-islamic-debit'),
    path('premier/sms-alert/', premier_views.prem_miscellenous,{'section': 'prem-sms'}, name='prem-sms'),
    path('premier/e-statements/', premier_views.prem_miscellenous,{'section': 'prem-e-statements'}, name='prem-e-statements'),
    path('premier/auto-loan/', premier_views.prem_miscellenous,{'section': 'prem-auto-loan'}, name='prem-auto-loan'),
    path('premier/banassurance/', premier_views.prem_miscellenous,{'section': 'prem-bancassurance'}, name='prem-bancassurance'),
    path('premier/visa-signature-card/', premier_views.prem_miscellenous,{'section': 'prem-visa-signature-card'}, name='prem-visa-signature-card'),
    path('premier/investment-services/', premier_views.prem_miscellenous,{'section': 'prem-investment-services'}, name='prem-investment-services'),
    path('premier/investment-goals/', premier_views.prem_miscellenous,{'section': 'prem-invest-goal'}, name='prem-investment-goal'),
    path('premier/self-service-banking/', premier_views.prem_miscellenous,{'section': 'prem-self-service'}, name='prem-self-service'),
    path('premier/orbit-rewards-points/', premier_views.prem_miscellenous,{'section': 'prem-orbit-rewards-points'}, name='prem-orbit-rewards'),
    path('premier/airport-lounges-perks/', premier_views.prem_miscellenous,{'section': 'prem-airport-lounge'}, name='prem-airport-lounge'),
    path('premier/islamic-banking/', premier_views.prem_miscellenous,{'section': 'prem-islamic-banking'}, name='prem-islamic-banking'),
    path('premier/fee-waiver/', premier_views.prem_miscellenous,{'section': 'prem-fee-waiver'}, name='prem-fee-waiver'),
    path('premier/complimentary-takaful/', premier_views.prem_miscellenous,{'section': 'prem-complimentary-takaful'}, name='prem-complimentary-takaful'),
    path('premier/alfa/', premier_views.prem_miscellenous,{'section': 'prem-alfa'}, name='prem-alfa'),
    path('premier/contact-center/', premier_views.prem_miscellenous,{'section': 'prem-contact-center'}, name='prem-contact-center'),
    path('premier/internet-banking/', premier_views.prem_miscellenous,{'section': 'prem-internet-baking'}, name='prem-internet-baking'),
    path('premier/atm-cdm/', premier_views.prem_miscellenous,{'section': 'prem-atm-cdm'}, name='prem-atm-cdm'),
    path('premier/hikmat-insurance/', premier_views.prem_miscellenous,{'section': 'prem-hikmat'}, name='prem-hikmat'),
    path('premier/lounge-access/', premier_views.prem_miscellenous,{'section': 'prem-lounge-access'}, name='prem-lounge-access'),

    #Peekabo URLS
    path('conventional/discounts-privileges/', premier_views.discount_privileges_conventional,{'section': 'discounts'}, name='discounts'),
    path('islamic/discounts-privileges/', premier_views.discount_privileges_islamic,{'section': 'discounts'}, name='discounts'),
    path('premier/discounts-privileges/', premier_views.discount_privileges_premier,{'section': 'discounts'}, name='discounts'),
    
    #DBG URLS
    path('digital-banking/tpl-cash-assist/', dbg_views.dbg_pages_view,{'section': 'dbg-tpl'}, name='dbg-tpl'),
    path('digital-banking/faqs/', dbg_views.dbg_pages_view,{'section': 'dbg-faqs'}, name='dbg-faqs'),
    path('digital-banking/voice-biometric-faqs/', dbg_views.dbg_pages_view,{'section': 'dbg-voice-faqs'}, name='dbg-voice-faqs'),
    path('digital-banking/alfa-term-faqs/', dbg_views.dbg_pages_view,{'section': 'dbg-alfa-faqs'}, name='dbg-alfa-faqs'),
    path('digital-banking/unionpay-faqs/', dbg_views.dbg_pages_view,{'section': 'dbg-unionpay-faqs'}, name='dbg-unionpay-faqs'),
    path('digital-banking/premo-xanders/', dbg_views.dbg_pages_view,{'section': 'dbg-premo'}, name='dbg-premo'),
    path('digital-banking/work-hall/', dbg_views.dbg_pages_view,{'section': 'dbg-workhall'}, name='dbg-workhall'),
    path('digital-banking/key-facts-statements/', dbg_views.dbg_pages_view,{'section': 'dbg-keyfacts'}, name='dbg-keyfacts'),
    path('digital-banking/alfa/', dbg_views.dbg_pages_view,{'section': 'dbg-alfa'}, name='dbg-alfa'),
    path('digital-banking/sms-banking/', dbg_views.dbg_pages_view,{'section': 'dbg-sms'}, name='dbg-sms'),
    path('digital-banking/raast/', dbg_views.dbg_pages_view,{'section': 'dbg-raast'}, name='dbg-raast'),
    path('digital-banking/alfa-chat/', dbg_views.dbg_pages_view,{'section': 'dbg-alfachat'}, name='dbg-alfachat'),
    path('digital-banking/key-facts-statements/alfa-chat/', dbg_views.dbg_pages_view,{'section': 'dbg-keyfacts-alfachat'}, name='dbg-keyfacts-alfachat'),
    path('digital-banking/key-facts-statements/goal-based/', dbg_views.dbg_pages_view,{'section': 'dbg-keyfacts-goalbased'}, name='dbg-keyfacts-goalbased'),
    path('digital-banking/alfa-account/', dbg_views.dbg_pages_view,{'section': 'dbg-alfa-account'}, name='dbg-alfa-account'),
    path('digital-banking/key-facts-statements/alfa-account/', dbg_views.dbg_pages_view,{'section': 'dbg-keyfacts-alfaaccount'}, name='dbg-keyfacts-alfaaccount'),
    path('digital-banking/key-facts-statements/alfa-saving/', dbg_views.dbg_pages_view,{'section': 'dbg-keyfacts-alfasaving'}, name='dbg-keyfacts-alfasaving'),
    path('digital-banking/alfa-saving/', dbg_views.dbg_pages_view,{'section': 'dbg-alfasaving'}, name='dbg-alfasaving'),
    path('digital-banking/atm-cdm-ccdm/', dbg_views.dbg_pages_view,{'section': 'dbg-atm-cdm'}, name='dbg-atm-cdm'),
    path('digital-banking/digital-banking/', dbg_views.dbg_pages_view,{'section': 'dbg-digital-branch'}, name='dbg-digital-branch'),
    path('digital-banking/digital-services/', dbg_views.dbg_pages_view,{'section': 'dbg-digital-services'}, name='dbg-digital-services'),
    path('digital-banking/vsm/', dbg_views.dbg_pages_view,{'section': 'dbg-vsm'}, name='dbg-vsm'),
    path('digital-banking/goal-based/', dbg_views.dbg_pages_view,{'section': 'dbg-goalbased'}, name='dbg-goalbased'),
    path('digital-banking/branch-outlook/', dbg_views.dbg_pages_view,{'section': 'dbg-branchoutlook'}, name='dbg-branchoutlook'),
    path('digital-banking/orbit-rewards/', dbg_views.dbg_pages_view,{'section': 'dbg-orbits'}, name='dbg-orbits'),
    path('digital-banking/earn-orbit-rewards/', dbg_views.dbg_pages_view,{'section': 'dbg-orbit-earn'}, name='dbg-orbit-earn'),
    path('digital-banking/alfamall/', dbg_views.dbg_pages_view,{'section': 'dbg-alfamall'}, name='dbg-alfamall'),
    path('digital-banking/mutual-funds/', dbg_views.dbg_pages_view,{'section': 'dbg-mutual-funds'}, name='dbg-mutual-funds'),
    path('digital-banking/eligibility/', dbg_views.dbg_pages_view,{'section': 'dbg-eligibility'}, name='dbg-eligibility'),
    path('digital-banking/documents/', dbg_views.dbg_pages_view,{'section': 'dbg-docs'}, name='dbg-docs'),
    path('digital-banking/alfa-payment-gateway/', dbg_views.dbg_pages_view,{'section': 'dbg-payment'}, name='dbg-payment'),
    path('digital-banking/schedule-of-charges/', dbg_views.dbg_pages_view,{'section': 'dbg-charges'}, name='dbg-charges'),
    path('digital-banking/onboarding/', dbg_views.dbg_pages_view,{'section': 'dbg-onboarding'}, name='dbg-onboarding'),
    path('digital-banking/alfa-qr/', dbg_views.dbg_pages_view,{'section': 'dbg-alfa-qr'}, name='dbg-alfa-qr'),
    path('digital-banking/personal/', dbg_views.dbg_pages_view,{'section': 'dbg-personal'}, name='dbg-personal'),
    path('digital-banking/business/', dbg_views.dbg_pages_view,{'section': 'dbg-biz'}, name='dbg-biz'),
    path('digital-banking/wallet-debit-card/', dbg_views.dbg_pages_view,{'section': 'dbg-wallet-card'}, name='dbg-wallet-card'),
    path('digital-banking/union-pay/', dbg_views.dbg_pages_view,{'section': 'dbg-unionpay'}, name='dbg-unionpay'),
    path('digital-banking/whatsapp-banking/', dbg_views.dbg_pages_view,{'section': 'dbg-whatsapp'}, name='dbg-whatsapp'),
    path('digital-banking/alfa-biz-app/', dbg_views.dbg_pages_view,{'section': 'dbg-alfa-biz-app'}, name='dbg-alfa-biz-app'),
    path('digital-banking/alfa-agent/', dbg_views.dbg_pages_view,{'section': 'dbg-alfa-agent'}, name='dbg-alfa-agent'),
    path('digital-banking/alfa-overdraft/', dbg_views.dbg_pages_view,{'section': 'dbg-alfa-overdraft'}, name='dbg-alfa-overdraft'),
    path('digital-banking/instant-loan/', dbg_views.dbg_pages_view,{'section': 'dbg-instant-loan'}, name='dbg-instant-loan'),
    path('digital-banking/instant-card/', dbg_views.dbg_pages_view,{'section': 'dbg-instant-card'}, name='dbg-instant-card'),
    path('digital-banking/orbit-redeem/', dbg_views.dbg_pages_view,{'section': 'dbg-redeem-orbit'}, name='dbg-redeem-orbit'),
    path('digital-banking/orbit-tiers/', dbg_views.dbg_pages_view,{'section': 'dbg-orbit-tiers'}, name='dbg-orbit-tiers'),
    path('digital-banking/alfa-efu/', dbg_views.dbg_pages_view,{'section': 'dbg-alfa-efu'}, name='dbg-alfa-efu'),
    path('digital-banking/internet-banking/', dbg_views.dbg_pages_view,{'section': 'dbg-internet-banking'}, name='dbg-internet-banking'),
    path('digital-banking/digital-facilitation/', dbg_views.dbg_pages_view,{'section': 'dbg-dfd'}, name='dbg-dfd'),
    path('digital-banking/alfa-remit/', dbg_views.dbg_pages_view,{'section': 'dbg-alfa-remit'}, name='dbg-alfa-remit'),
    path('digital-banking/tpl-hospital/', dbg_views.dbg_pages_view,{'section': 'dbg-hospital'}, name='dbg-hospital'),
    path('digital-banking/edu-fee/', dbg_views.dbg_pages_view,{'section': 'dbg-education-fee'}, name='dbg-education-fee'),
    path('digital-banking/virtual-debit-card/', dbg_views.dbg_pages_view,{'section': 'dbg-virtual-card'}, name='dbg-virtual-card'),
    path('digital-banking/alfa-customer-gateway/', dbg_views.dbg_pages_view,{'section': 'dbg-gateway-customer'}, name='dbg-gateway-customer'),
    path('digital-banking/voice-bio/', dbg_views.dbg_pages_view,{'section': 'dbg-voice-bio'}, name='dbg-voice-bio'),
    path('digital-banking/transaction-insurance/', dbg_views.dbg_pages_view,{'section': 'dbg-transaction-insurance'}, name='dbg-transaction-insurance'),
    path('digital-banking/alfa-term-deposit/', dbg_views.dbg_pages_view,{'section': 'dbg-alfa-deposit'}, name='dbg-alfa-deposit'),
    path('digital-banking/ecommerce/', dbg_views.dbg_pages_view,{'section': 'dbg-ecommerce'}, name='dbg-ecommerce'),
    path('digital-banking/instant-loan-new/', dbg_views.dbg_pages_view,{'section': 'dbg-instant-loan-v2'}, name='dbg-instant-loan-v2'),
    path('digital-banking/eobi/', dbg_views.dbg_pages_view,{'section': 'dbg-eobi'}, name='dbg-eobi'),
    path('digital-banking/digital-account-opening/', dbg_views.dbg_pages_view,{'section': 'dbg-accounts'}, name='dbg-accounts'),
    path('digital-banking/employee-banking/', dbg_views.dbg_pages_view,{'section': 'dbg-employee'}, name='dbg-employee'),
    path('digital-banking/women-power/', dbg_views.dbg_pages_view,{'section': 'dbg-women-power'}, name='dbg-women-power'),
    path('digital-banking/prize-bond/', dbg_views.dbg_pages_view,{'section': 'dbg-prize-bond'}, name='dbg-prize-bond'),
    path('digital-banking/insta-cash/', dbg_views.dbg_pages_view,{'section': 'dbg-insta-cash'}, name='dbg-insta-cash'),
    path('digital-banking/alfa-biz/', dbg_views.dbg_pages_view,{'section': 'dbg-alfa-biz'}, name='dbg-alfa-biz'),
    path('digital-banking/account-opening/', dbg_views.dbg_pages_view,{'section': 'dbg-account-opening'}, name='dbg-account-opening'),


	
    path('digital-banking/personal-finance-management/', dbg_views.dbg_product_pages_view,{'section': 'dbg-pfm'}, name='dbg-pfm'),
    path('digital-banking/bfilter/', dbg_views.dbg_product_pages_view,{'section': 'dbg-bfilter'}, name='dbg-bfilter'),
    path('digital-banking/ktrade/', dbg_views.dbg_product_pages_view,{'section': 'dbg-ktrade'}, name='dbg-ktrade'),
    path('digital-banking/saylani-alfa/', dbg_views.dbg_product_pages_view,{'section': 'dbg-saylani'}, name='dbg-saylani'),


    #2
    path('deposit-protection/', dbg_views.dbg_pages_view,{'section': 'deposit-protection'}, name='deposit-protection'),
    #3
    path('key-fact-statements/accounts/', dbg_views.dbg_pages_view,{'section': 'key-facts-accounts'}, name='key-facts-accounts'),
    #4
    path('rda/nrp/', dbg_views.dbg_pages_view,{'section': 'rda-nrp'}, name='rda-nrp'),
    #9
    path('rda/pension/', dbg_views.dbg_pages_view,{'section': 'rda-pension'}, name='rda-pension'),
    #5
    path('rda/personal/', dbg_views.dbg_pages_view,{'section': 'rda-personal'}, name='rda-personal'),
    #6
    path('rda/biz/', dbg_views.dbg_pages_view,{'section': 'rda-biz'}, name='rda-biz'),
    #7
    path('rda/samaji-khidmat/', dbg_views.dbg_pages_view,{'section': 'rda-samaji'}, name='rda-samaji'),
    #8
    path('naya-pakistan-certificates/', dbg_views.dbg_pages_view,{'section': 'naya-pakistan'}, name='naya-pakistan'),
    #10
    path('psx-investments/', dbg_views.dbg_pages_view,{'section': 'psx-investments'}, name='psx-investments'),
    #14
    path('islamic-banking/about-islamic-banking/',islamic_views.islamic_gallery,{'section': 'islamic-aboutus'}, name='isl_Aboutus'),
    #15
    path('islamic-banking/key-facts/',dbg_views.dbg_pages_view,{'section': 'key-facts-islamic'}, name='key_facts_isl'),
    #12
    path('roshan-car-calculator/',dbg_views.dbg_pages_view,{'section': 'roshan-car-calculator'}, name='roshan-car-calculator'),
#13
    path('roshan-apna-ghar/',dbg_views.dbg_pages_view,{'section': 'roshan-apna-ghar'}, name='roshan-apna-ghar'),
    #11
    path('roshan-apni-car/',dbg_views.dbg_pages_view,{'section': 'roshan-apni-car'}, name='roshan-apni-car'),

    path('roshan-products/',dbg_views.dbg_pages_view,{'section': 'roshan-products-dbg'}, name='roshan-products-dbg'),
] +  static(settings.STATIC_URL,document_root = settings.STATIC_ROOT) + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT) 




handler404 = 'premier_core.premier_views.custom_404'

