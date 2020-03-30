import sys

sys.path.append('./classes/import')

from importData import ImportData
from command import Command

i = ImportData('./data/input/testDb.txt')

i.importFromTxt()

#print(i.getDbs())

cmd = Command(i.getDbs())

req = {
    "command" : "find",
    "table" : "sales",
    "condition" : {
        "=" : ['city', 'London']  
    }
}

cmd.doCommand(req)
