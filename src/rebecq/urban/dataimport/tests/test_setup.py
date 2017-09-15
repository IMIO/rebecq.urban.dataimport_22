# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from rebecq.urban.dataimport.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of rebecq.urban.dataimport into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if rebecq.urban.dataimport is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('rebecq.urban.dataimport'))

    def test_uninstall(self):
        """Test if rebecq.urban.dataimport is cleanly uninstalled."""
        self.installer.uninstallProducts(['rebecq.urban.dataimport'])
        self.assertFalse(self.installer.isProductInstalled('rebecq.urban.dataimport'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IRebecqUrbanDataimportLayer is registered."""
        from rebecq.urban.dataimport.interfaces import IRebecqUrbanDataimportLayer
        from plone.browserlayer import utils
        self.failUnless(IRebecqUrbanDataimportLayer in utils.registered_layers())
