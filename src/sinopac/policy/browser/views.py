# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api
import logging
import os

class OidReport(BrowserView):

    index = ViewPageTemplateFile("template/oid_report.pt")

    def __call__(self):

        context = self.context
        request = self.request
        catalog = context.portal_catalog
        with open('/home/andyfang51/event/zeocluster/var/client1/event.log') as file:
            self.docs = file.read()
        return self.index()


class Members(BrowserView):

    index = ViewPageTemplateFile("template/memebers.pt")

    def __call__(self):

        context = self.context
        request = self.request
        catalog = context.portal_catalog
        self.users = api.user.get_users()
        return self.index()


class Oid(BrowserView):

#    index = ViewPageTemplateFile("template/oid.pt")

    def __call__(self):

        logger = logging.getLogger("OID_Record")
        context = self.context
        request = self.request
        catalog = context.portal_catalog
        oid = getattr(request, 'oid', None)
        if oid:
            logger.info(oid)
        else:
            return
        return


class TestFunction(BrowserView):

    index = ViewPageTemplateFile("template/test_function.pt")

    def __call__(self):

        context = self.context
        request = self.request
        catalog = context.portal_catalog
        import pdb; pdb.set_trace()
        return self.index()
