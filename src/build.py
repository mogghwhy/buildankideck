import os
import configparser
from pathlib import Path

x = [f.name for f in os.scandir("../../../") if f.is_file()]

print(x)

"""
config = configparser.ConfigParser()
config.optionxform = str
config.read('../../../config.ini')


bases = config['BASES']
keys = bases.keys()

baseFolders = []

for b in keys:
    baseFolders.append(bases.get(b))

columns = config['COLUMNS'].keys()

print(type(columns))

for k in columns:
    print(k)
"""
