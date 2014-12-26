import doctest
from unittest import TestSuite

from doctest import DocFileSuite

from plone.testing import layered

from plone.app.controlpanel.tests.cptc import CP_FUNCTIONAL_LAYER
from plone.app.controlpanel.tests.cptc import CP_SECURITY_LAYER
from plone.app.controlpanel.tests.cptc import simplify_white_space
from plone.app.controlpanel.tests.cptc import generate_user_and_groups


OPTIONFLAGS = (doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE)


def loginAsManager(browser, user='root', pwd='secret', control='Login Name'):
    """points the browser to the login screen and logs in as user root
       with Manager role."""
    browser.open('http://nohost/plone/')
    browser.getLink('Log in').click()
    browser.getControl(control).value = user
    browser.getControl('Password').value = pwd
    browser.getControl('Log in').click()


def test_suite():
    tests = [
#            'editing.txt',
             'filter.txt',
#             'mail.txt',
#             'maintenance.txt',
#             'security_enable_user_folder.txt',
#             'search.txt',
#             'site.txt',
#             'skins.txt',
#             'markup.txt',
#             'navigation.txt',
             'types.txt',
             'syndication.txt'
             ]
    suite = TestSuite()

    for test in tests:
        suite.addTest(layered(
            DocFileSuite(test, optionflags=OPTIONFLAGS,
                         package="plone.app.controlpanel.tests",
                         globs={'loginAsManager': loginAsManager,
                                'simplify_white_space': simplify_white_space}),
            layer=CP_FUNCTIONAL_LAYER))

#    suite.addTest(layered(
#        DocFileSuite('usergroups.txt', optionflags=OPTIONFLAGS,
#                     package="plone.app.controlpanel.tests",
#                     globs={'loginAsManager': loginAsManager,
#                            'generate_user_and_groups': generate_user_and_groups}),
#        layer=CP_FUNCTIONAL_LAYER))

#    suite.addTest(layered(
#        DocFileSuite('security.txt', optionflags=OPTIONFLAGS,
#                     package="plone.app.controlpanel.tests",
#                     globs={'loginAsManager': loginAsManager}),
#        layer=CP_SECURITY_LAYER))

    return suite
