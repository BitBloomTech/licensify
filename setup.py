# licensify
# Copyright (C) 2018, Simmovation Ltd.
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
from setuptools import setup, Command
import re
from os import path

import versioneer

PACKAGE_NAME = 'licensify'

install_requires = []

tests_require = [
    'tox'
]

extras_require = {
    'test': tests_require,
    'build': ['versioneer']
}

setup(
    name='licensify',
    version=versioneer.get_version(),
    packages=['licensify'],
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require=extras_require,
    cmdclass=versioneer.get_cmdclass()
)
