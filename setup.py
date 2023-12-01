# -*- coding: utf-8 -*-
"""
This script is used to setup the projects for the course. It will create a
directory for each project and copy the necessary files.

Author: @kiroussa
URL: https://github.com/27network/aoc-toolkit
"""

import hashlib
import os
import sys

PROJECT_DIR = 'projects'
TEMPLATE_SCRIPT = 'template.py'
HASH_FILE = '.last_setup'

BANNER = """
:::'###::::'########::'##::::'##:'########:'##::: ##:'########:::::'#######::'########:
::'## ##::: ##.... ##: ##:::: ##: ##.....:: ###:: ##:... ##..:::::'##.... ##: ##.....::
:'##:. ##:: ##:::: ##: ##:::: ##: ##::::::: ####: ##:::: ##::::::: ##:::: ##: ##:::::::
'##:::. ##: ##:::: ##: ##:::: ##: ######::: ## ## ##:::: ##::::::: ##:::: ##: ######:::
 #########: ##:::: ##:. ##:: ##:: ##...:::: ##. ####:::: ##::::::: ##:::: ##: ##...::::
 ##.... ##: ##:::: ##::. ## ##::: ##::::::: ##:. ###:::: ##::::::: ##:::: ##: ##:::::::
 ##:::: ##: ########::::. ###:::: ########: ##::. ##:::: ##:::::::. #######:: ##:::::::
:..:::::..::........::::::...:::::........::..::::..:::::..:::::::::.......:::..:::::::
:::'######:::'#######::'########::'########::::'##::::::::'#######::::::::'##:'####::::
::'##... ##:'##.... ##: ##.... ##: ##.....:::::. ##::::::'##.... ##::::::'##:: ####::::
:: ##:::..:: ##:::: ##: ##:::: ##: ##:::::::::::. ##::::: ##:::: ##:::::'##::: ####::::
:: ##::::::: ##:::: ##: ##:::: ##: ######::::::::. ##:::: ##:::: ##::::'##::::: ##:::::
:: ##::::::: ##:::: ##: ##:::: ##: ##...::::::::::. ##::: ##:::: ##:::'##::::::..::::::
:: ##::: ##: ##:::: ##: ##:::: ##: ##::::::::::::::. ##:: ##:::: ##::'##::::::'####::::
::. ######::. #######:: ########:: ########:::::::::. ##:. #######::'##::::::: ####::::
:::......::::.......:::........:::........:::::::::::..:::.......:::..::::::::....:::::
"""

def main() -> None:
    """Main entry point for the script."""
    first_run = not os.path.isfile(HASH_FILE)
    hash_value = None
    if not first_run:
        with open(HASH_FILE, 'r') as hash_file:
            hash_value = hash_file.read()
    else:
        print(BANNER)

    # Create the projects dir and its parent directories
    os.makedirs(PROJECT_DIR, exist_ok=True)

    # Get the list of projects
    projects = ["day%d" % i for i in range(1, 25 + 1)]
    max_len = max([len(p) for p in projects])

    # Create a directory for each project
    for project in projects:
        # Create the project directory
        project_dir = os.path.join(PROJECT_DIR, project)
        print(' ', end='')
        if not first_run:
            print('Re-', end='')
        print(f'Setting up Day #{project[3:]}...', end='')
        print(' ' * (max_len - len(project)), end='')
        os.makedirs(project_dir, exist_ok=True)

        # Ensure template script is copied
        target_main = os.path.join(project_dir, "main.py")
        if hash_value and os.path.isfile(target_main):
            with open(target_main, 'r') as script:
                # Check if the template script has been modified
                if hash_value != hashlib.md5(script.read().encode()).hexdigest():
                    print(' SKIPPING')
                    continue
                # The hash is the same, we can delete it and copy it back
                os.remove(target_main)
        if not os.path.isfile(target_main):
            with open(TEMPLATE_SCRIPT, 'r') as template:
                with open(target_main, 'w') as script:
                    script.write(template.read())
        print(' OK')
    
    # Create the hash file
    with open(HASH_FILE, 'w') as hash_file:
        with open(TEMPLATE_SCRIPT, 'r') as template:
            # Hash the template script
            hash_file.write(hashlib.md5(template.read().encode()).hexdigest())

    print('\nAll Done! Merry Coding! :)')


if __name__ == '__main__':
    main()
