# -*- coding: utf-8 -*-

from sinopac.policy import _
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.interface import Interface
from plone.z3cform.layout import wrap_form
from Products.statusmessages.interfaces import IStatusMessage
from z3c.form import button
from z3c.form import form, field
from zope import schema
from plone import api
import random
from Products.CMFPlone.utils import safe_unicode


class ILotto(Interface):
    """ """

class LottoForm(form.Form):

    fields = field.Fields(ILotto)
    ignoreContext = True

    def updateWidgets(self):
#        import pdb; pdb.set_trace()
#        default初始值放這裏
        super(LottoForm, self).updateWidgets()

    @button.buttonAndHandler(u'分享抽')
    def handleSave(self, action):
        users = api.user.get_users()
        luckyer = random.choice(users)
        fullname = safe_unicode(luckyer.getProperty('fullname'))
        fb_url = safe_unicode('https://www.facebook.com/%s' % luckyer.id.replace('fb', ''))
        email = safe_unicode(luckyer.getProperty('email'))

        IStatusMessage(self.request).addStatusMessage(
            u"分享抽中獎人： %s || 臉書頁面：%s || Email：%s" % (fullname, fb_url, email),            
            'info')
        redirect_url = "%s/@@lotto" % self.context.absolute_url()
        self.request.response.redirect(redirect_url)


    @button.buttonAndHandler(u'加碼抽')
    def handleCancel(self, action):
        users = api.user.get_users()
        luckyer = random.choice(users)
        fullname = safe_unicode(luckyer.getProperty('fullname'))
        fb_url = safe_unicode('https://www.facebook.com/%s' % luckyer.id.replace('fb', ''))
        email = safe_unicode(luckyer.getProperty('email'))

        IStatusMessage(self.request).addStatusMessage(
            u"加碼抽中獎人： %s || 臉書頁面：%s || Email：%s" % (fullname, fb_url, email),
            'info')
        redirect_url = "%s/@@lotto" % self.context.absolute_url()
        self.request.response.redirect(redirect_url)




from plone.z3cform.layout import wrap_form
LottoView = wrap_form(LottoForm)
