"""
Update all Python packages.

Copyright 2024. Andrew Wang.
"""
# pylint: disable=not-an-iterable, no-value-for-parameter
from concurrent.futures import ThreadPoolExecutor
from subprocess import run
from click import command, option
from pkg_resources import working_set


@command()
@option('--individual', '-i', is_flag=True, show_default=True,
        default=False, help='Update packages together / individually')
def update(individual: bool):
    """Run pip update command."""
    pkgs = [dist.project_name for dist in working_set]
    if individual:
        with ThreadPoolExecutor() as pool:
            pool.map(lambda pkg: run(
                ['pip', 'install', '-U', pkg], check=True), pkgs)
    else:
        run(['pip', 'install', '-U'] + pkgs, check=True)


if __name__ == '__main__':
    update()
