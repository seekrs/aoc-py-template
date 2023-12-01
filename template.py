# -*- coding: utf-8 -*-
"""
This is the template script for the Advent of Code 2023. It should have the
necessary boilerplate, imports, and helpers to get you running solving problems.

Have fun! ~ @kiroussa
"""

import collections; import datetime; import itertools; import logging; import math; import os; import sys; import time; from typing import List, Tuple

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
    try:
        with open(file, 'r') as input_file:
            return input_file.read().splitlines()
    except FileNotFoundError as e:
        return [None, e.strerror]

# Main
def main():
    """Main entry point for the script.

    This is the main entry point for the script. It will read the input file,
    solve the problems, and print the results, with the additional timing info.

    To run the script, simply run `python main.py <input_file>` from the command line.
    """
    folder_name = os.path.dirname(os.path.realpath(__file__))
    folder_name = folder_name.split(os.sep)[-1]
    logger = logging.getLogger(folder_name)

    if len(sys.argv) < 2:
        logger.error('No input file specified')
        logger.error(f'Usage: python {sys.argv[0]} <input_file>')
        return
    
    # Logger setup boilerplate
    class CustomFormatter(logging.Formatter):
        def format(self, record):
            timestamp = datetime.datetime.now().strftime('%H:%M:%S')
            space = ''
            if record.levelname == 'INFO':
                space = ' '
            if record.levelname == 'DEBUG':
                log_message = f"[{timestamp}] [{record.levelname}/{record.threadName}] ({record.name}:{record.lineno}): {record.getMessage()}"
            else:
                log_message = f"[{timestamp}] {space}{record.levelname} ({record.name}): {record.getMessage()}"
            return log_message
    sh = logging.StreamHandler()
    sh.setFormatter(CustomFormatter())
    sh.setLevel(logging.DEBUG)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(sh)

    # Read input
    input_to_read = sys.argv[1]
    logger.info(f'Using input file: {input_to_read}')

    input = read_input(input_to_read)
    if not input or not input[0]:
        if input:
            logger.error(f'Error reading input file: {input[1]}')
        else:
            logger.error('No valid input found, aborting...')
        return

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
