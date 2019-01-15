# BSD 3-Clause License
#
# Copyright (c) 2019 Simmovation Ltd
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# * Neither the name of the copyright holder nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
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
