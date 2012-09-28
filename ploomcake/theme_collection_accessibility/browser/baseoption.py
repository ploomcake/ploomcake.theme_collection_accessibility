#!/usr/bin/env python
# Authors: Maurizio Lupo <maurizio.lupo@redomino.com> and contributors (see docs/CONTRIBUTORS.txt)
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as published
# by the Free Software Foundation.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA
# 02111-1307, USA.

from Products.CMFCore.utils import getToolByName

try:
    from ploomcake.themeoptions.browser.interfaces import IThemeOption
except ImportError:
    from zope.interface import Interface

class IThemeOption(Interface):
    """mock interface"""

from zope.interface import implements
from zope.site.hooks import getSite

class BaseThemeOption(object):
    implements(IThemeOption)

    def is_available(self):
        site = getSite()
        portal_quickinstaller = getToolByName(site, 'portal_quickinstaller')
        if portal_quickinstaller.isProductInstalled('ploomcake.theme_collection_accessibility'):
            return True

