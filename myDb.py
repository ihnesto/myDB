import sys
# добавлем пути поиска для классов
sys.path.append('./classes/import')
sys.path.append('./classes/commands')

# подключаем классы
from importData import ImportData
from command import Command

# Импортируем данные из файла
i = ImportData('./data/input/testDb.txt')
i.importFromTxt()

# создаем объект для обработки команд
cmd = Command(i.getDbs())

# команда
req = {
    "command" : "find",
    "table" : "sales"
    
}
# выполняем команду
cmd.doCommand(req)

req = {
    "command" : "remove",
    "table" : "sales",
    "condition" : {
        "=" : ['city', 'London']  
    }
    
}
cmd.doCommand(req)

print()
req = {
    "command" : "find",
    "table" : "sales"
    
}
# выполняем команду
cmd.doCommand(req)

req = {
     "command" : "insert",
     "table" : "sales",
     "values" : { 'snum' : 1008,
                   'city' : 'Kiyv',
                'sname' : "John"
                 }
}

cmd.doCommand(req)
print()
req = {
    "command" : "find",
    "table" : "sales"
    
}
# выполняем команду
cmd.doCommand(req)

