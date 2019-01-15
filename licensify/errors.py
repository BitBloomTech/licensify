# licensify
# Copyright (C) 2019, Simmovation Ltd.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA
"""Defines errors for the :mod:`licensify` module
"""

class LicensesOutOfDateError(Exception):
    """Error raised when licenses are out of date
    """
    def __init__(self, files):
        """Initialises the :class:`LicensesOutOfDateError` class

        :param files: The files that are out of date
        :type files: list
        """
        super(LicensesOutOfDateError, self).__init__()
        self.files = files

    def __repr__(self):
        return '{}({})'.format(type(self).__name__, self.files)
