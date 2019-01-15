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
"""Entry point to the licensify command
"""
from sys import stdout
from os import linesep, walk, path
import fnmatch
from argparse import ArgumentParser

from licensify import apply_license_header, LicensesOutOfDateError

def _parse_args():
    parser = ArgumentParser()
    parser.add_argument('license', help='A file containing the liense')
    parser.add_argument('--directory', default='.', help='The directory to apply licenses to')
    parser.add_argument('--files', default='*.*', help='Glob to match files')
    parser.add_argument('--exclude', default=None, help='Glob to match files to be excluded')
    parser.add_argument('--comment', default='#', help='Comment string to prepend to header lines')
    parser.add_argument('--dry-run', action='store_true', default=False, help='Perform a dry run')
    parser.add_argument(
        '--check', action='store_true', default=False,
        help='Return an error if any files need updating (implies dry run)'
    )
    return parser.parse_args()

def licensify(command_line_args):
    """licensify with the given command line args
    """
    with open(command_line_args.license) as fp:
        license_header = fp.read()
        files = [
            path.join(dirname, f)
            for dirname, _, filenames in walk(command_line_args.directory)
            for f in fnmatch.filter(filenames, command_line_args.files)
            if not (command_line_args.exclude and fnmatch.fnmatch(f, command_line_args.exclude))
        ]
        try:
            result = apply_license_header(
                license_header, files,
                command_line_args.check, command_line_args.dry_run or command_line_args.check
            )
        except LicensesOutOfDateError as error:
            stdout.write(repr(error))
            exit(1)
        if result:
            message = 'The following files have been changed: {}'.format(', '.join(result))
        else:
            message = 'No files changed'
        stdout.write(message + linesep)

def main():
    """Entrypoint for the application
    """
    licensify(_parse_args())

if __name__ == '__main__':
    main()
