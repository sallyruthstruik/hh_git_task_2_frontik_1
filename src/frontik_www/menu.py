# -*- coding: utf-8 -*-

from frontik import http_get
from frontik import etree as et
from frontik import Doc

import frontik_www.config

career_menu = et.fromstring(
'''<careerMenu>
    <item href="/applicant/searchvacancy.xml">Вакансии</item>
    <item href="/web/guest/catalog">Компании</item>
    <item href="http://edu.hh.ru/">Образование</item>
    <item href="/web/guest/events">Календарь</item>
    <item href="/web/guest/library">Статьи</item>
    <item href="http://livehh.ru/soobshmolspetsicaru/">Общение</item>
    <item href="/web/guest/consult">Консультант</item>
    <item href="/web/guest/referat">Рефераты</item>
  </careerMenu>''')
  
def do_menu(response, session):
    menu_doc = Doc('leftMenu')
    
    if session.user_type == 'employer':
        menu_doc.put(http_get(frontik_www.config.searchHost + 
                                  'callevent/exists?userId=' +
                                  session.user_id))
        
    elif session.user_type == 'applicant':
        menu_doc.put(http_get(frontik_www.config.serviceHost + 'applicant/leftMenuBar' + 
                                  '?site=' + session.site_id + 
                                  '&lang=' + session.lang))

    if session.platform == 'JOBLIST':
        menu_doc.put(http_get(frontik_www.config.serviceHost + 'vacancyblocks?' +
                                  'totalCount=4&hotCount=100'))
    
    menu_doc.put(career_menu)
    
    response.doc.put(menu_doc)