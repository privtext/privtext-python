#-*- coding: utf-8 -*-

import sys, os

from privtext.env import _TEST_MODE

from privtext.args import get_args
from privtext.utils import cross_input
from privtext import PrivateText

import re

def run(args=None):

  if args is None:
    args = sys.argv[1:]

  args = get_args(args=args)

  if os.isatty(sys.stdout.fileno()):

    private = PrivateText(keysize=args.keysize, password=args.password, timelive=args.lifetime, email=args.email, debug_mode=_TEST_MODE)
    private.set('split_lines', args.split_lines)

    l = len(args.text)
    r = re.compile('^https://privtext\\.com/([^/#]+)(#(.+))?$', flags=re.I)
    m = r.search(args.text)
    
    if not m is None:
      noteid = m.group(1)
      password = m.group(3)
      if password is None or len(password) == 0:
        password = private.get('password')
      if not password:
        print('You must add  password for note `%s` to link (#password) or with flag -p --password. For more info call --help, please.' % noteid)
        sys.exit(-1)

      private.set('password', password)
      private.set('noteid', noteid)

    else:
      if l > 0:
        private.set('text', args.text)
      elif not args.file is None:
        private.set('inputfile', args.file)

    if not args.outfile is None:
      private.set('outfile', args.outfile)

    if not m is None:
      private.read()
    else:
      private.send()

    private.printout()
    
    # print("Please, press [Enter] for exit...")
    # cross_input()

  else:
    print('Only for console/terminal')


if __name__ == '__main__':
  run()