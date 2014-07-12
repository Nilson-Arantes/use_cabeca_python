#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os

os.chdir('/home/leonardo/python/use_cabeca_python/hfpy_code/chapter3')

data = open('sketch.txt')

for each_line in data:
  (role, line_spoken) = each_line.split(':')
  print(role, end='')
  print(' said: ', end='')
  print(line_spoken, end='')

