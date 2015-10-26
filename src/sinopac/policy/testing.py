# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import sinopac.policy


class SinopacPolicyLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=sinopac.policy)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'sinopac.policy:default')


SINOPAC_POLICY_FIXTURE = SinopacPolicyLayer()


SINOPAC_POLICY_INTEGRATION_TESTING = IntegrationTesting(
    bases=(SINOPAC_POLICY_FIXTURE,),
    name='SinopacPolicyLayer:IntegrationTesting'
)


SINOPAC_POLICY_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(SINOPAC_POLICY_FIXTURE,),
    name='SinopacPolicyLayer:FunctionalTesting'
)


SINOPAC_POLICY_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        SINOPAC_POLICY_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='SinopacPolicyLayer:AcceptanceTesting'
)
