import configparser
from pathlib import Path

print(Path("../../../../config.ini").exists())
print(Path("../../../config.ini").exists())
print(Path("../../config.ini").exists())
print(Path("../config.ini").exists())

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