class Command :
    def __init__(self, dbs) :
        self.database = dbs
        
# анализ, какая команда   
    def doCommand(self, cmd) :
        c = cmd.get('command')
        if c is None :
            return
        if c == 'find' :
            self.doFind(cmd)
        if c == 'remove' :
            self.doRemove(cmd)
        if c == 'insert' :
            self.doInsert(cmd)

    def doRemove(self, cmd) :
        table = cmd['table']
        if table == None :
            return
        p = False
        for t in self.database :
            #print(t)
            if t['table-name'] == table :
                p = True
                db = t
                break
        if p == False :
            return
        cond = cmd['condition']
        if cond == None or cond == '' :
            #self.showAllData(db)
            return
        for op, val in cond.items() :
            #print(op, val)
            args = cond[op]
            #print(args)
            #f = args[0]
            #val = args[1]
            #print(f, val)
            if op == '=' :    
                f = args[0]
                val = args[1]
                #print(f, val)
                #flds = db['fields']
                data = db['data']
                #idx = flds.index(f)
                #print(flds)
                for line in data :
                    if line[f] == val :
                        #print(line)
                        data.remove(line)
            if op == '>' :
                self.showGtData(db, args)
            if op == '<' :
                self.showLtData(db, args)

    def doInsert(self, cmd) :
        table = cmd.get('table')
        if table is None :
            return
        p = False
        for t in self.database :
            #print(t)
            if t['table-name'] == table :
                p = True
                db = t
                break
        if p == False :
            return
        val = cmd.get('values')
        if val is None :
            return
        data = db['data']
        data.append(val)

# обработка команды find
    def doFind(self, cmd) :
        table = cmd['table']
        if table == None :
            return
        p = False
        for t in self.database :
            #print(t)
            if t['table-name'] == table :
                p = True
                db = t
                break
        if p == False :
            return
        # try:
        #     cond = cmd['condition']
        # except KeyError :
        cond = cmd.get('condition')
        if cond is None :
            self.showAllData(db)
            return
        for op, val in cond.items() :
            #print(op, val)
            args = cond[op]
            #print(args)
            #f = args[0]
            #val = args[1]
            #print(f, val)
            if op == '=' :    
                self.showEqData(db, args)
            if op == '>' :
                self.showGtData(db, args)
            if op == '<' :
                self.showLtData(db, args)

# обработка условия(condition) = 
    def showEqData(self, db, args) :
            f = args[0]
            val = args[1]
            #print(f, val)
            #flds = db['fields']
            data = db['data']
            #idx = flds.index(f)
            #print(flds)
            for line in data :
                if line[f] == val :
                    print(line)

# обработка условия(condition) >
    def showGtData(self, db, args) :
            f = args[0]
            val = args[1]
            print(f, val)
            flds = db['fields']
            data = db['data']
            idx = flds.index(f)
            #print(flds)
            for line in data :
                print(line)
                if line[idx] > val :
                    return line

# обработка условия(condition) <
    def showLtData(self, db, args) :
            f = args[0]
            val = args[1]
            print(f, val)
            flds = db['fields']
            data = db['data']
            idx = flds.index(f)
            #print(flds)
            for line in data :
                #print(line)
                if line[idx] < val :
                    print(line)

# вывод всех данных таблицы
    def showAllData(self, db) :
        data = db['data']
        for i in data :
            print(i)
