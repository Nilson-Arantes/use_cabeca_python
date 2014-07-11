#!/usr/bin/env python3

"""Módulo para visuzalizar listas aninhadas. 
   Módulo nester.py"""

def print_lol(the_list):
  """Função para percorrer a lista e mostrar na tela.
     Tem a função print_lol usando isinstance para 
     verificar ser é uma lista"""

  for lista_item in the_list:
    if isinstance(lista_item, list):
      print_lol(lista_item)
    else:
      print(lista_item)
