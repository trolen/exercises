#!/usr/bin/python

import os
import re
import sys
import time

class StoryParser:
  def __init__(self, filename):
    self._debugEnabled = True
    self._read_wordlist(filename)
    self._read_story()
    self._words_found = []

  def _debug(self, s):
    if self._debugEnabled:
      print s

  def _strip_newline(self, line):
    return line.rstrip('\n')

  def _read_wordlist(self, filename):
    self._wordlist = []
    regex = re.compile('[^a-z]')
    with open(filename, 'r') as f:
      for line in f:
        word = self._strip_newline(line.lower())
        match = regex.sub('', word)
        self._wordlist.append((len(match),word,match))
    self._wordlist.sort(reverse=True)

  def _read_story(self):
    self._story = ''
    for line in sys.stdin:
      self._story += self._strip_newline(line.lower())

  def parse_story(self, start_position):
    story_length = len(self._story[start_position:])
    if story_length <= 0:
      return True
    for (length, word, match) in self._wordlist:
      if length > story_length:
        continue
      if self._story[start_position:].startswith(match):
	self._words_found.append(word)
        if self.parse_story(start_position + length):
          return True
        self._words_found.pop()
    return False

  def print_story(self):
    for word in self._words_found:
      print word,
    print

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print '\nUSAGE: ' + os.path.basename(sys.argv[0]) + ' wordlist'
    print '    wordlist - a text file with a list of English words, one per line\n'
    print '    The program takes a stream of characters with no whitespace on stdin.'
    print '    The program tries to parse words from the text, given the word list,'
    print '    and inserts spaces in the stream to separate words that it finds.'
    sys.exit(1)
  parser = StoryParser(sys.argv[1])
  t0 = time.time()
  parser.parse_story(0)
  t1 = time.time()
  parser.print_story()
  print "Parsed in %0.2f seconds" % (t1 - t0)
