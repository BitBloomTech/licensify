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

_here = path.abspath(path.dirname(__file__))

with open(path.join(_here, 'README.md')) as fp:
    README_CONTENTS = fp.read()

install_requires = []

tests_require = [
    'pytest',
    'pytest-cov',
    'pylint',
    'tox'
]

extras_require = {
    'test': tests_require,
    'build': ['versioneer'],
    'publish': ['twine']
}

setup(
    name=PACKAGE_NAME,
    license='GPLv3',
    description='Utility to apply license headers to source code files',
    long_description=README_CONTENTS,
    long_description_content_type='text/markdown',
    author='Simmovation Ltd',
    author_email='info@simmovation.tech',
    url='https://github.com/Simmovation/licensify',
    platforms='any',
    version=versioneer.get_version(),
    packages=[PACKAGE_NAME],
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require=extras_require,
    cmdclass=versioneer.get_cmdclass(),
    entry_points={
        'console_scripts': ['licensify=licensify.__main__:main'],
    },
    python_requires='>=2.7,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*,<4'
)
