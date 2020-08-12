#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys, os, stat

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

with open("README.md", "r") as fh:
  long_description = fh.read()

setup(
    name='privtext',
    version='2.1.3',
    
    description='A tool for creating create your private',
    long_description=long_description,
    long_description_content_type="text/markdown",
    
    author='Privtext Tech.',
    author_email='tech@privtext.com',
    url='https://github.com/privtext/privtext-python',
    
    packages=find_packages("."),
    
    install_requires=[
      "argparse",
      "pycrypto",
      "requests"
    ]
)

def get_umask():
  umask = os.umask(0)
  os.umask(umask)
  return umask

def chmod_plus_x(path):
    os.chmod(
        path,
        os.stat(path).st_mode |
        (
            (
                stat.S_IXUSR |
                stat.S_IXGRP |
                stat.S_IXOTH
            )
            & ~get_umask()
        )
    )

executable_dir = os.path.sep.join(sys.executable.split(os.path.sep)[:-1])
executable_path = executable_dir + os.path.sep + 'privtext'

print('Making executable command to {0}'.format(executable_path))
with open(executable_path, 'w') as executable:
  executable.write("""#!{0}
#-*- coding: utf-8 -*-

import sys
from privtext import __main__ as main

if __name__ == '__main__':
  # sys.argv[0] = 'privtext'
  sys.exit(main.run(sys.argv[1:]))

""".format(sys.executable))
  chmod_plus_x(executable_path)

# print('Done.')
