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

from ploomcake.theme_collection_accessibility.browser.baseoption import BaseThemeOption

class ThemeOption(BaseThemeOption):

    def title(self):
        """get the title of the option"""
        return "High contrast"

    def description(self):
        """get the description of the option"""
        return "high contrast description"

    def class_name(self):
        """class to attach to the body"""
        return "ploomcake-high-contrast"

    def option_type(self):
        """description of the option_type"""
        return "Color"

    def option_type_name(self):
        """name of the option_type"""
        return "color"

    def preview_src(self):
        """src of an img representing the option"""
        return "++resource++ploomcake.theme.options.highcontrast/preview.png"

