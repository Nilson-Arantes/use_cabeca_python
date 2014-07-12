#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os

#pega o caminho do seu diretorio
os.chdir('/home/leonardo/python/use_cabeca_python/hfpy_code/chapter3')

data = open('sketch.txt')

for each_line in data:
  if not each_line.find(':') == -1:
    (role, line_spoken) = each_line.split(':', 1)
    print(role, end='')
    print(' said: ', end='')
    print(line_spoken, end='')

data.close()
