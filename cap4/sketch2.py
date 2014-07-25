#!/usr/bin/python3
# -*- coding:UTF-8 -*-

import os
os.chdir('/home/leonardo/python/use_cabeca_python/hfpy_code/chapter3')
man =[]
other= []

try:
  data = open('sketch.txt')
  
  for each_line in data:
    try:
      (role, line_spoken) = each_line.split(':', 1)
      line_spoken = line_spoken.strip()
      if role == 'Man':
        man.append(line_spoken)
      elif role == 'Other Man':
        other.append(line_spoken)
    except ValueError:
      pass
  data.close()
except IOError:
  print('The data file is missing!')

print(man)
print(other)

