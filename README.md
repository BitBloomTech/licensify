# licensify

Licensify is a tool for applying license headers to source code files.

[![CircleCI](https://circleci.com/gh/Simmovation/licensify.svg?style=svg)](https://circleci.com/gh/Simmovation/licensify)

## Usage


```
> python licensify --help

usage: licensify [-h] [--directory DIRECTORY] [--files FILES]
                 [--comment COMMENT] [--dry-run] [--check]
                 license

positional arguments:
  license               A file containing the liense

optional arguments:
  -h, --help            show this help message and exit
  --directory DIRECTORY
                        The directory to apply licenses to
  --files FILES         Glob to match files
  --comment COMMENT     Comment string to prepend to header lines
  --dry-run             Perform a dry run
  --check               Return an error if any files need updating (implies
                        dry run)
```