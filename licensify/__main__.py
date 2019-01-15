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
