# -*- coding: utf-8 -*-
"""
This is the template script for the Advent of Code 2023. It should have the
necessary boilerplate, imports, and helpers to get you running solving problems.

Have fun! ~ @kiroussa
"""

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

#######
# Your code goes here!!!! :D
#######
def solve_part_one(input: List[str]) -> str:
    """Solve part one of the problem."""
    return None


def solve_part_two(input: List[str]) -> str:
    """Solve part two of the problem."""
    return None


# Helpers
def read_input() -> List[str]:
    """Read the input file and return the list of lines."""
    with open(INPUT_FILE, 'r') as input_file:
        return input_file.read().splitlines()


# Main
def main():
    """Main entry point for the script."""
    input = read_input()

    start_time = time.time()
    part_one = solve_part_one(input)
    if not part_one:
        logger.info('Part One: Not solved yet :(')
    else:
        logger.info(f'Part One: {part_one}')
        logger.info(f'Part One Execution Time: {time.time() - start_time}')

    if not part_one:
        return

    start_time = time.time()
    part_two = solve_part_two(input)
    if not part_two:
        logger.info('Part Two: Not solved yet :(')
    else:
        logger.info(f'Part Two: {part_two}')
        logger.info(f'Part Two Execution Time: {time.time() - start_time}')


if __name__ == '__main__':
    main()
