# -*- coding: utf-8 -*-
"""
This is the template script for the Advent of Code 2023. It should have the
necessary boilerplate, imports, and helpers to get you running solving problems.

Have fun! ~ @kiroussa
"""

import collections; import itertools; import math; import os; import sys; import time; from typing import List, Tuple

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
def read_input(file: str) -> List[str]:
    """Read the input file and return the list of lines."""
    with open(file, 'r') as input_file:
        return input_file.read().splitlines()


# Main
def main():
    """Main entry point for the script.

    This is the main entry point for the script. It will read the input file,
    solve the problems, and print the results, with the additional timing info.

    To run the script, simply run `python main.py <input_file>` from the command line.
    """
    logger = logging.getLogger(__name__)

    if len(sys.argv) < 2:
        logger.error('No input file specified')
        logger.error(f'Usage: python {sys.argv[0]} <input_file>')
        return
    
    input_to_read = sys.argv[1]
    logger.info(f'Using input file: {input_to_read}')

    input = read_input(input_to_read)

    start_time = time.time()
    part_one = solve_part_one(input)
    if not part_one:
        logger.info('Part One: Not solved yet :(')
    else:
        logger.info(f'Part One: "{part_one}"')
        logger.info(f'  took {time.time() - start_time}s')

    if not part_one:
        return

    start_time = time.time()
    part_two = solve_part_two(input)
    if not part_two:
        logger.info('Part Two: Not solved yet :(')
    else:
        logger.info(f'Part Two: "{part_two}"')
        logger.info(f'  took {time.time() - start_time}s')


if __name__ == '__main__':
    main()
