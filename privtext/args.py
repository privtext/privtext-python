#-*- coding: utf-8 -*-

import os, sys
import argparse
import textwrap

from privtext.utils import cross_input

def get_args(args=None):

  if args is None:
    args = sys.argv[1:]

  argv_parser = argparse.ArgumentParser(prog='privtext', formatter_class=argparse.RawDescriptionHelpFormatter, description=textwrap.dedent("""\
            Create your private note.\n\
            -------------------------\n\
            We do not have an access to your data, since a decryption key is not stored.\n\
            We only generate a key, crypt your data, and return you the key.\n\
            We use 256-bit symmetric AES encryption.\n\
            -------------------------\
            """),
            epilog=textwrap.dedent("""\
            -------------------------\n\
            * NOTE: key's value `--text`, `--file`, `--outfile`, what have one or more space -\n\
            It must be incapsulate by \" or \'\n\
            -------------------------"""),
            add_help=True)
  argv_parser.add_argument("-t", "--text", action="store", metavar='SOME TEXT', dest='text', default='', help="Run script with your text.")
  argv_parser.add_argument("-f", "--file", action="store", metavar='FILE PATH', dest='file', default=None, help="Run script which enters your file")
  argv_parser.add_argument("-r", "--rows", action="store_true", dest='file_by_rows', default=False, help="Split file by rows and make link for each within (max 30 rows)")

  argv_parser.add_argument("-o", "--outfile", action="store", metavar='FILE PATH', dest='outfile', default=None, help="Saves the info to the specified file")
  argv_parser.add_argument("-k", "--keysize", action="store", metavar='PASSWORD LENGTH', dest="keysize", type=int, default=9, help="Set secret password length for password generator.")
  argv_parser.add_argument("-p", "--password", action="store", metavar='ENCRYPT PASSWORD', dest='password', default=None, help="Set custom user's password")
  argv_parser.add_argument("-l", "--lifetime", action="store", dest='lifetime', nargs=1, choices=('afterread','1hour','1day','3days','1week','1month','1year'), type=str, default='afterread', help="Set time live for your Note.")
  argv_parser.add_argument("-e", "--email", action="store", metavar='NOTIFY EMAIL', dest='email', default=None, help="E-mail to notify when Note is destroyed.")
  argv_parser.add_argument("-v", "--verbose", action="store_true", dest='verbose', default=False, help="Print the Python version number and exit")
  args = argv_parser.parse_args(args=args)

  if args.verbose:
    print("Version 2.0. Built by Jul 20 2020 13:50 GMT")
    # print("Please, press [Enter] for exit...")
    # cross_input()
    sys.exit(0)

  if ((not args.file is None) and os.path.exists(args.file)) and len(args.text) > 0:
    print("* WARNING: You must use one from specified types: only by `text` or only by `file`. Look to help (--help, -h) for more info.")
    print("Please, press [Enter] for exit...")
    cross_input()
    sys.exit(-1)
  elif not ((not args.file is None) and os.path.exists(args.file)) and len(args.text) == 0:
    print("You run programm like double click or pressed `Enter`.\nFor more detaile run from terminal (command line) `privtext -h` or `privtext --help`\n")
    print("For now, you must enter needed string: ")
    args.text = cross_input()

  #if user set key size, than ArgumentParser will return list with one element
  if isinstance(args.keysize, list):
    args.keysize = args.keysize[0]

  #if user set lifetime, than ArgumentParser will return list with one element
  if isinstance(args.lifetime, list):
    args.lifetime = args.lifetime[0]

  return args