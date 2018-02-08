#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mechanicalsoup
import codecs
from slugify import slugify




#connect to tpp admin site
browser = mechanicalsoup.StatefulBrowser()
browser.open('https://www.tpp.pt/admin/')

username = 'tpp_add_username'
password = 'tpp_add_password'
#fill from to login
form = browser.select_form()
browser['username'] = username
browser['password'] = password

browser.submit_selected()
browser.follow_link('/admin/companies/company/add/')


with open('companies_list.txt') as f:
    company = f.readlines()

companies = [x.strip() for x in company]

for comp in companies:
    browser.open('https://www.tpp.pt/admin/companies/company/add/')
    comp = unicode(comp.decode('utf8'))
    form = browser.select_form()
    browser['name'] = comp
    browser['slug'] = slugify(comp)
    browser.submit_selected()
