import pandas as pd
import json

def clo():
    new_dict = dict()
with open('/content/mature.fa','r') as f:
  for line in f:
    m = line.strip()
    if len(m) != 0 and m[0] == '>':
      m = m.split()
      key = m[0][1:]
      new_dict[key] = ""
    else:
        new_dict[key] += m
for key, value in new_dict.items():
#  print(key, '*', value)):