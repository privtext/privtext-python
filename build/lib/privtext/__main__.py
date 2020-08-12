#-*- coding: utf-8 -*-

import sys, os

from privtext.env import _TEST_MODE

from privtext.args import get_args
from privtext.utils import cross_input
from privtext import PrivateText

def run(args=None):

  if args is None:
    args = sys.argv[1:]

  args = get_args(args=args)

  if os.isatty(sys.stdout.fileno()):

    private = PrivateText(keysize=args.keysize, password=args.password, timelive=args.lifetime, email=args.email, debug_mode=_TEST_MODE)
    private.set('split_lines', args.split_lines)

    if len(args.text) > 0:
      private.set('text', args.text)
    elif not args.file is None:
      private.set('inputfile', args.file)

    if not args.outfile is None:
      private.set('outfile', args.outfile)

    private.send()
    private.printout()
    
    # print("Please, press [Enter] for exit...")
    # cross_input()

  else:
    print('Only for console/terminal')


if __name__ == '__main__':
  run()