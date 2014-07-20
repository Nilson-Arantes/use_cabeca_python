#!/usr/bin/python3
# -*- coding: uTF-8 -*-

import os

os.chdir('/home/leonardo/python/use_cabeca_python/aprendendo3')
try:
  arquivo = open('einstein.txt')
  
  for linha in arquivo:
    print(linha, end='')

except IOError:
  print("Não foi possível abrir o arquivo")


