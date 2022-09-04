"""
Update all Python packages.

Copyright 2021. Andrew Wang.
"""
from json import loads
from subprocess import run, PIPE
from platform import python_version


def update():
    """Pipe output from pip list and update all."""
    version = python_version()[0]
    proc = run(f'python{version} -m pip list --format json'.split(),
               stdout=PIPE, check=True)
    output = loads(proc.stdout)
    packages = [entry['name'] for entry in output]
    command = f'python{version} -m pip install -U'.split() + packages
    print(f'PYTHON {version} - {len(packages)} PACKAGES')
    run(command, check=True)


if __name__ == '__main__':
    update()
