# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from sinopac.policy.testing import SINOPAC_POLICY_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that sinopac.policy is properly installed."""

    layer = SINOPAC_POLICY_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if sinopac.policy is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('sinopac.policy'))

    def test_browserlayer(self):
        """Test that ISinopacPolicyLayer is registered."""
        from sinopac.policy.interfaces import ISinopacPolicyLayer
        from plone.browserlayer import utils
        self.assertIn(ISinopacPolicyLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = SINOPAC_POLICY_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['sinopac.policy'])

    def test_product_uninstalled(self):
        """Test if sinopac.policy is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled('sinopac.policy'))

    def test_browserlayer_removed(self):
        """Test that ISinopacPolicyLayer is removed."""
        from sinopac.policy.interfaces import ISinopacPolicyLayer
        from plone.browserlayer import utils
        self.assertNotIn(ISinopacPolicyLayer, utils.registered_layers())
