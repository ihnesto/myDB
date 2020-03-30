import sys

sys.path.append('./classes/import')

from importData import ImportData

i = ImportData('./data/input/testDb.txt')

i.importFromTxt()

print(i.getDbs())
