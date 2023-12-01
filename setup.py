# -*- coding: utf-8 -*-
"""
This script is used to setup the projects for the course. It will create a
directory for each project and copy the necessary files.

Author: @kiroussa
URL: https://github.com/27network/aoc-toolkit
"""

import os
import sys

PROJECT_DIR = 'projects'
TEMPLATE_SCRIPT = 'template.py'
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
    print(BANNER)
    print('\n' * 2)

    # Create the projects dir and its parent directories
    os.makedirs(PROJECT_DIR, exist_ok=True)

    # Get the list of projects
    projects = ["day%d" % i for i in range(1, 25 + 1)]
    max_len = max([len(p) for p in projects])

    # Create a directory for each project
    for project in projects:
        # Create the project directory
        project_dir = os.path.join(PROJECT_DIR, project)
        print(f'\tSetting up Day #{project[3:]}...', end='')
        print(' ' * (max_len - len(project)), end='')
        os.makedirs(project_dir, exist_ok=True)

        # Ensure template script is copied
        template_script = os.path.join(project_dir, "main.py")
        if not os.path.isfile(template_script):
            with open(TEMPLATE_SCRIPT, 'r') as template:
                with open(template_script, 'w') as script:
                    script.write(template.read())
        print(' OK')

    print('All Done! Merry Coding! :)')


if __name__ == '__main__':
    main()
