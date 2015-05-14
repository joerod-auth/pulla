#!/usr/bin/env python3

from __future__ import print_function

import sys
import os
import argparse

from .pulla import Pulla
from .utils import is_this_a_git_dir

def parse_known_args():
    """ Parse command line arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--folder', type=str, dest='folder',
                        help='Update the repos in this folder')
    mutually_exclusive_group = parser.add_mutually_exclusive_group()

    mutually_exclusive_group.add_argument('-v', '--verbose',    
                         action='store_true', help='Show verbose information.'
                        ' Higher verbosity can be selected by --verbosity '
                        'flag')
    mutually_exclusive_group.add_argument('-l', '--verbosity', type=int,
                        help='Set higher verbosity level for more detailed '
                        'information: 1. Critical, 2. Error, 3. Warning, '
                        '4. Info, 5. Debug', choices=range(1, 6))


    args, otherthings = parser.parse_known_args()
    return args, otherthings


def main():
    """ Main
    """
    args, otherthings = parse_known_args()
    argc = len(otherthings)

    directory = os.path.abspath(os.curdir)
    if args.folder:
        directory = args.folder

    verbosity = 0
    if args.verbose:
        verbosity = 1
    elif args.verbosity:
        verbosity = args.verbosity

    pulla = Pulla(verbosity=verbosity, recursive=False)

    if is_this_a_git_dir(directory):
        pulla.do_pull_in(directory)
    else:
        pulla.pull_all(directory)

if __name__ == '__main__':
    sys.exit(main())
