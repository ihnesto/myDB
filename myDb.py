import importData from importData

i = importData('./data/input/testDb.txt')

i.importFromTxt()

print(i.getDbs())
