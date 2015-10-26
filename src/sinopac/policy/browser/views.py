# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class TestFunction(BrowserView):

    index = ViewPageTemplateFile("template/test_function.pt")

    def __call__(self):

        context = self.context
        request = self.request
        catalog = context.portal_catalog
        return self.index()
