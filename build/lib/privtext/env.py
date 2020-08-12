#-*- coding: utf-8 -*-

import sys

_TEST_MODE = 0
_PY_V = 2 if sys.version_info[0] < 3 else 3

if _PY_V == 2:
  import cookielib
elif _PY_V == 3:
  from http import cookiejar as cookielib
else:
  print('Fatal error: Unknown python version!')
  exit(-1)