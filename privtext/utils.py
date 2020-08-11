#-*- coding: utf-8 -*-

from privtext.env import _PY_V
from random import randint

def cross_input():
  if _PY_V == 2:
    return raw_input()
  return input()

def cross_encode(s):
  if _PY_V == 2:
    return s
  return s.encode('utf-8')

def cross_decode(s):
  if _PY_V == 2:
    return s
  return s.decode('utf-8')

# Function for create random string
def makeRandomString(length):
  makefrom, key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890', []
  for i in range(0, length): key.append(makefrom[randint(0,len(makefrom) - 1)])
  return ''.join(key)