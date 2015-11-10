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


class ToApp(BrowserView):

    def __call__(self):

        context = self.context
        catalog = context.portal_catalog
        request = self.request
        response = request.RESPONSE
        url = request.get('url', 'facebook')
        if url == 'app':
            response.redirect('http://ppt.cc/C3wMw')
        else:
            response.redirect('https://www.facebook.com/SinoPac?fref=ts')

        user = api.user.get_current()
        user.setMemberProperties(mapping={ 'click_app':True, })

#        import pdb; pdb.set_trace()
        return


class ILotto2(Interface):
    """ """


class Lotto2Form(form.Form):

    fields = field.Fields(ILotto2)
    ignoreContext = True

    def updateWidgets(self):
#        import pdb; pdb.set_trace()
#        default初始值放這裏
        super(Lotto2Form, self).updateWidgets()

    @button.buttonAndHandler(u'加碼抽')
    def handleCancel(self, action):
        users = api.user.get_users()
        # filter users
        lottoList = []
        for user in users:
            try:
                if user.getProperty('click_app') == True:
                    lottoList.append(user)
            except:pass
#        import pdb; pdb.set_trace()
        users = lottoList
        luckyer = random.choice(users)
        fullname = safe_unicode(luckyer.getProperty('fullname'))
        fb_url = safe_unicode('https://www.facebook.com/%s' % luckyer.id.replace('fb', ''))
        email = safe_unicode(luckyer.getProperty('email'))

        IStatusMessage(self.request).addStatusMessage(
            u"加碼抽中獎人： %s || 臉書頁面：%s || Email：%s" % (fullname, fb_url, email),
            'info')
        redirect_url = "%s/@@app_lotto" % self.context.absolute_url()
        self.request.response.redirect(redirect_url)



from plone.z3cform.layout import wrap_form
Lotto2View = wrap_form(Lotto2Form)
