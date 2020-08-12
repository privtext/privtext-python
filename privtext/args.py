#-*- coding: utf-8 -*-

import os, sys
import argparse
import textwrap

from privtext.utils import cross_input

def get_args(args=None):

  if args is None:
    args = sys.argv[1:]

  argv_parser = argparse.ArgumentParser(
    prog='privtext',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent("""\
            Encrypt text and create a one-time link with privtext.com.\n\
            -------------------------\n\
            The text is encrypted with a key generated on client side.\n\
            Encrypted text is stored on privtext.com and destroyed after it's read.\n\
            Strong AES 256-bit encryption is used.\n\
            -------------------------\
            """),
    epilog=textwrap.dedent("""\
            -------------------------\n\
            * NOTE: If you pass text as command line argument, do  not forget
            to encapsulate it into "".

            Check out https://github.com/privtext/privtext-python
            -------------------------"""),
    add_help=True
  )
  argv_parser.add_argument("-f", "--file", action="store", metavar='FILE PATH', dest='file', default=None, help="Get input text from file rather than from argument or piped input.")
  argv_parser.add_argument("-s", "--split-lines", action="store_true", dest='split_lines', default=False, help="Split text line by line and make a separate privtext for each line.")

  argv_parser.add_argument("text", nargs='?', default='', metavar='TEXT TO ENCRYPT')

  argv_parser.add_argument("-o", "--outfile", action="store", metavar='FILE PATH', dest='outfile', default=None, help="Specify an output file rather than priniting result to stdout.")
  argv_parser.add_argument("-k", "--keysize", action="store", metavar='PASSWORD LENGTH', dest="keysize", type=int, default=9, help="Specify key size for random key generator.")
  argv_parser.add_argument("-p", "--password", action="store", metavar='ENCRYPTION KEY', dest='password', default=None, help="Specify encryption key. Otherwise the key will be randomly generated.")
  argv_parser.add_argument("-l", "--lifetime", action="store", dest='lifetime', nargs=1, choices=('afterread','1hour','1day','3days','1week','1month','1year'), type=str, default='afterread', help="Set life time for your private text on privtext.com.")
  argv_parser.add_argument("-e", "--email", action="store", metavar='NOTIFY EMAIL', dest='email', default=None, help="Specify e-mail to send notification to when privtext is read and destroyed.")
  argv_parser.add_argument("-v", "--version", action="store_true", dest='version', default=False, help="Print version and exit")
  args = argv_parser.parse_args(args=args)

  if args.version:
    print("Version 2.1.3. Built Wed Aug 12 12:50")
    sys.exit(0)

  if args.file is None and len(args.text) == 0:
    if not os.isatty(sys.stdin.fileno()):
      args.text = sys.stdin.read()
  if args.file and args.text:
    print("ERROR! Only ONE text source can be specified. Either piped input, command line argument, or file. `privtext --help` for more info.")
    sys.exit(-1)
  elif not args.file and not args.text:
    argv_parser.print_help()
    sys.exit(0)

  if isinstance(args.keysize, list):
    args.keysize = args.keysize[0]

  #if user set lifetime, then ArgumentParser will return list with one element
  if isinstance(args.lifetime, list):
    args.lifetime = args.lifetime[0]

  return args
