#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup


#rodoviary transporst url
wiki_transports_url = 'https://pt.wikipedia.org/wiki/Lista_de_empresas_de_transporte_rodoviário_em_Portugal'

page = urllib2.urlopen(wiki_transports_url)

soup = BeautifulSoup(page,'html.parser')

companies = soup.find_all('a',attrs={'title': True})


file = open('companies_list.txt','w')
for company in companies:
    if 'editar' not in company.text:
        file.write(company.text.encode('utf-8').strip())
        file.write('\n')
    if company.text == 'vtbus':
        break
