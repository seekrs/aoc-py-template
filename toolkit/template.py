# -*- coding: utf-8 -*-
"""
This is the template script for the Advent of Code 2023. It should have the
necessary boilerplate, imports, and helpers to get you running solving problems.

Have fun! ~ @kiroussa
"""

import argparse
import collections
import itertools
import logging
import math
import os
import sys
import time
from typing import List, Tuple

# Constants
INPUT_FILE = 'input.txt'

# Logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

# Helpers
def read_input() -> List[str]:
    """Read the input file and return the list of lines."""
    with open(INPUT_FILE, 'r') as input_file:
        return input_file.read().splitlines()


def hijack_path():
    """Hijack the path to import modules from the toolkit directory."""
    # Get the path to the current file
    # Should be something like /bla/bla/aoc-toolkit/projects/day1/main.py
    current_file = os.path.abspath(__file__)

    # Get the path to the toolkit directory
    # Should be something like /bla/bla/aoc-toolkit
    toolkit_dir = os.path.dirname(os.path.dirname(current_file))

    # Add the toolkit directory to the python lookup path
    sys.path.insert(0, toolkit_dir)
