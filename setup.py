# -*- coding: utf-8 -*-
"""
This script is used to setup the projects for the course. It will create a
directory for each project and copy the necessary files from the toolkit directory.

Author: @kiroussa
URL: https://github.com/27network/aoc-toolkit
"""

import os
import sys

TOOLKIT_DIR = 'toolkit'
PROJECT_DIR = 'projects'
TEMPLATE_SCRIPT = 'template.py'


def main() -> None:
    """Main entry point for the script."""
    # First, check that the toolkit directory exists
    if not os.path.isdir(TOOLKIT_DIR):
        print(f'Error: {TOOLKIT_DIR} directory does not exist')
        sys.exit(1)

    # Create the projects dir and its parent directories
    os.makedirs(PROJECT_DIR, exist_ok=True)

    # Get the list of projects
    projects = ["day%d" % i for i in range(1, 25)]

    # Create a directory for each project
    for project in projects:
        # Create the project directory
        project_dir = os.path.join(PROJECT_DIR, project)
        print(f'Creating {project}...', end='')
        os.makedirs(project_dir, exist_ok=True)

        # Ensure template script is copied
        template_script = os.path.join(project_dir, "main.py")
        if not os.path.isfile(template_script):
            with open(os.path.join(TOOLKIT_DIR, TEMPLATE_SCRIPT), 'r') as template:
                with open(template_script, 'w') as script:
                    script.write(template.read())

    print('Done!')


if __name__ == '__main__':
    main()
