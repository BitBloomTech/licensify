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
"""Defines the :func:`apply_license_header` function
"""
from .errors import LicensesOutOfDateError

def apply_license_header(license_header, files, check=False, dry_run=False, comment='#'):
    """Apply the license header provided to the files specified

    :param license_header: The license header
    :type license_header: str
    :param files: The files to apply the license header to
    :type files: Sequence
    :param check: `True` if an exception should be raised when some files need updating;
    `False` otherwise
    :type check: bool
    :param dry_run: `True` if header should be added to these files; `False` otherwise
    :type dry_run: bool
    :param comment: The string to prefix header lines with to turn them into a coment
    :type comment: str

    :returns: The list of files updated
    :rtype: list
    """
    files_requiring_update = []

    license_header_lines = _license_header_lines(license_header, comment)

    for file_name in files:
        with open(file_name) as fp:
            lines = fp.readlines()

        old_header, lines = _split_header(lines)
        if old_header != license_header_lines:
            if not dry_run:
                with open(file_name, 'w') as fp:
                    fp.writelines(license_header_lines + lines)
            files_requiring_update.append(file_name)

    if check and files_requiring_update:
        raise LicensesOutOfDateError(files_requiring_update)

    return files_requiring_update

def _split_header(lines):
    for line_number, line in enumerate(lines):
        if not line or line[0] != '#':
            return lines[:line_number], lines[line_number:]
    # Every line is commented
    return lines, []

def _license_header_lines(text, comment):
    return [
        (comment + ' ' + line.strip() if line.strip() else comment) + '\n'
        for line in text.splitlines()
    ]
