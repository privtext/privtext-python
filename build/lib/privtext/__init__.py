#-*- coding: utf-8 -*-

import sys, os

from .args import get_args
from .env import _TEST_MODE, _PY_V
from .env import cookielib
from privtext.utils import cross_encode, cross_decode, makeRandomString

from random import random
import base64

from Crypto.Hash import SHA256
from Crypto.Cipher import AES
import hashlib

import requests
import json


# main functional
class PrivateText:
  
  # name of system
  _name = 'PrivateTextService'

  # constructor
  def __init__(self, outfile=None, inputfile=None, text='', password=None, timelive='afterread', email=None, keysize=9, debug_mode=0):

    # http(s) address, where service is locate
    self._net_domain = "https://privtext.com"
    #max lines, what can process by one run
    self._max_process_lines = 30
    #length for string, what use as private client key
    self._publick_key_size = keysize
    #max size in Mb, what service server can get from request
    self._max_post_note_mb = 5
    #path for ckoockies file for temporary save on local machine
    self._cookies_file_path = os.path.sep + 'tmp' + os.path.sep + PrivateText._name.lower() + '.cookie'

    #flag for debug mode
    self.debug_mode = debug_mode

    #output lines for answer to client
    self.outtext = []
    #output file, where `outtext` will saved, if it property seted
    self.outfile = outfile
    #path for imported file, what can client set
    self.inputfile = inputfile
    #split file by rows and make link for each within
    self.split_lines = False
    #just text, what can client set
    self.text = text
    
    #customer pasword for encrypt note
    self.password = password
    
    #condition flag for out password with url note
    self.__private_password = False
    
    #customer time live for your note.
    timelive_switcher = { 'afterread': 0, '1hour': 3600, '1day':  86400, '3days': 259200, '1week': 604800, '1month': 2592000, '1year': 31104000 }
    self.timelive = timelive_switcher[timelive]
    
    
    #e-mail to notify when note is destroyed.
    self.email = email

  #get secure temporary identifier for user / recursive if has some problems
  def _miner(self, prefix, target, counter=0, randpath=0):
    if counter == 0: randpath = random()
    started_counter = counter
    while(True):
      counter += 1
      strToHash = str(prefix) + str(randpath) + str(counter)
      
      if self.debug_mode == 2:
        print("* _miner: ")
        print("\t prefix: " + str(prefix))
        print("\t randpath: " + str(randpath))
        print("\t counter: " + str(counter))

      shash_o = SHA256.new()
      shash_o.update(cross_encode(strToHash))
      shash = shash_o.hexdigest()

      if self.debug_mode == 2:
        print("\t target: " + str(target))
        print("\t shash: " + str(shash))

      if int(shash,16) <= int(target,16):
        return strToHash
      elif counter - started_counter > 10e2:
        return self._miner(prefix, target, counter, randpath)


  #send data to service and get private url
  def _makeprivate(self, text):
    note, secure_key = self._encryptNote(text)

    if self.debug_mode:
      print("Input text: " + text)
      print("Secure key: " + secure_key)
      print("Encrypted: " + note)

    length = len(note)

    if length > 1048576 * self._max_post_note_mb:
      print("Your encrypted note is the bigger (" + str(int(length/1024)) + ") than accept length (" + str(int(self._max_post_note_mb*1024)) + ") for post")
    else:
      if os.path.exists(self._cookies_file_path):
        os.remove(self._cookies_file_path)

      cj = cookielib.LWPCookieJar(self._cookies_file_path)
      url = self._net_domain + "/api/proof"

      if self.debug_mode:
        print("Request url: " + url)
      
      try:
        response = requests.post(url, data={'action':'get_proof_password', 'ajax':1}, cookies=cj)
        response_answ = response.text
      except urllib2.URLError as e:
        # print("* WARNING: Request to server error: {0}\nPlease, try later.\nExit.".format("SSL certificate verify failed"))
        print("* WARNING: Request error {0} ({1})\n".format(url, str(e)))
        sys.exit(-2)

      if self.debug_mode:
        print("Response: " + response_answ)

      content = json.loads(response_answ)

      if content['algorithm'] == 'sha256':
        proof = self._miner(content['prefix'], content['target'])

        if self.debug_mode:
          print("Maked proof: " + proof)

        sdata = {'action':'save_note', 'note':note, 'proof':proof, 'ajax':1, 'timelive':self.timelive, 'noticemail':self.email}

        url = self._net_domain + "/api/note"
        
        if self.debug_mode:
          print("Request url: ", url)
          print("Send data: ", sdata)

        try:
          response = requests.post(url, data=sdata, cookies=cj)
          response_answ = response.text
        except urllib2.URLError as e:
          # print("* WARNING: Request to server error: {0}\nPlease, try later.\nExit.".format("SSL certificate verify failed"))
          print("* WARNING: Request error {0} ({1})\n".format(url, str(e)))
          sys.exit(-2)

        if self.debug_mode:
          print("Response: " + response_answ)

        content = json.loads(response_answ)
        if 'id' in content.keys():
          url = self._net_domain + content['url']
          if(not self.__private_password):
            url += '#' + secure_key
          self.outtext.append(url)
          
          if self.debug_mode:
            print("Result url: " + url + "\n")
        else:
          print("* WARNING: Some error on create-raw action: '" + response_answ + "'")
      else:
        print("* WARNING: Unknown algorithm '" + content['algorithm'] + "'")

  #encrypt input text from argv or from file row
  def _encryptNote(self, plaintext):
    passwd = None
    if not self.password is None:
      if len(self.password) > 0:
        passwd = self.password
        self.__private_password = True
      else:
        passwd = makeRandomString(self._publick_key_size)
    else:
        passwd = makeRandomString(self._publick_key_size)
        
    passwd_size = self._publick_key_size

    salt = os.urandom(8)
    salted, dx = cross_encode(''), cross_encode('')

    block_length = AES.block_size # = 16

    # GibberishAES generate self public (for url) key, prom private user's pass
    # 256 / 8 is length for publickey - hard code for Gibberish AES CBC
    
    key_length = int(256 / 8)
    
    salted_length = key_length + block_length
    while len(salted) < salted_length:
      m = hashlib.new('md5')
      m.update(dx + cross_encode(passwd) + salt)
      dx = m.digest()
      salted += dx
    key = salted[0: key_length]
    iv = salted[key_length: key_length + block_length]

    if self.debug_mode == 3:
      print ({
        'key_length': key_length,
        'block_length': block_length,
        'salted_length': salted_length,
        'salted': str(len(salted)),
        'key': str(len(key)),
        'iv': str(len(iv))
      })

    if _PY_V == 2:
      pad = lambda s: s + (block_length - len(s) % block_length) * chr(block_length - len(s) % block_length)
      plaintext = bytes(pad(plaintext))

      crpt = AES.new(key, AES.MODE_CBC, iv)
      encrypted = crpt.encrypt(bytes(plaintext))
    elif _PY_V == 3:
      pad = lambda s: s + (block_length - len(s) % block_length) * bytes([block_length - len(s) % block_length])
      plaintext = pad(cross_encode(plaintext))

      crpt = AES.new(key, AES.MODE_CBC, iv)
      encrypted = crpt.encrypt(plaintext)

    note = cross_decode(base64.b64encode(cross_encode('Salted__') + salt + encrypted))
    return (note, passwd)

  #public function, what run process for use service
  def send(self):
    if len(self.text):
      if self.split_lines:
        lines = self.text.split('\n')
        if len(lines) > self._max_process_lines:
          print("* WARNING: Input file has more than max limit lines for file")
        else:
          for line in lines:
            self._makeprivate(line)
      else:
        self._makeprivate(self.text)

    if not self.inputfile is None:
      if os.path.exists(self.inputfile):

        if self.split_lines:
          lines = []
          try:
            lines = [line for line in open(self.inputfile, 'r')]
          except IOError as e:
            print("* WARNING: I/O error({0})\n".format(str(e)))
          
          if len(lines) > self._max_process_lines:
            print("* WARNING: Input file has more than max limit lines for file")
          else:
            for line in lines:
              self._makeprivate(line)
        else:
          with open(self.inputfile, 'r') as fir:
            self._makeprivate(fir.read())
      else:
        print("* WARNING: input file '" + self.inputfile + "' doesn't exists or not readable")

  #dinamic save needed properties
  def set(self, name, value):
    self.__dict__[name] = value

  #start output results to client / in print to console or save in file
  def printout(self):
    if self.outfile is None:
      self._print_results()
    else:
      if os.path.exists(os.path.dirname(self.outfile)):
        try:
          f = open(self.outfile, 'w')
          f.write("\n".join(self.outtext))
          f.close()
        except IOError as e:
          print("* WARNING: I/O error ({0})\n".format(str(e)))
          self._print_results()
      else:
        self._print_results()

  #print results to client
  def _print_results(self):
    print("\n".join(self.outtext))