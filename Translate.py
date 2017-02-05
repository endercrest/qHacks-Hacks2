import re

class translate():
    global restList
    restList = [] #CHANGE
    def getRestList(self):
        return restList
    
    def mapE(lom):
        sentence = []
        i = 0
        while(i<len(lom)):
            if lom[i]['Type'] == 'function':
                sentence.append(translate.functiontoenglish(lom[i]['Value']))
            elif lom[i]['Type'] == 'ass':
                sentence.append(" is assigned to ")
            elif lom[i]['Type'] == 'float':
                if ((i<len(lom)-1) and ((lom[i+1]['Type'] == 'op'))) or ((i>0) and ((lom[i-1]['Type'] == 'op') or (lom[i-1]['Type'] == 'function' or (lom[i-1]['Type'] == 'cmp')))):
                    sentence.append("the number " + lom[i]['Value'])
                else:
                    sentence.append("the string " + lom[i]['Value'])
            elif lom[i]['Type'] == 'string':
                sentence.append("the string " + lom[i]['Value'])
            elif lom[i]['Type'] == 'var':
                if lom[i]['Value'] == "True":
                    sentence("the boolean 'True'")
                elif lom[i]['Value'] == "False":
                    sentence("the boolean 'False'")
                else:
                    sentence.append("the variable " + lom[i]['Value'])   
            elif lom[i]['Type'] == 'comma':
                sentence.append(" and then it")
            elif lom[i]['Type'] == 'op':
                if(lom[i]['Value'] == '+'):
                    sentence.append(" added with ")
                elif(lom[i]['Value'] == '-'):
                    if ((i>0) and (lom[i-1]['Type'] != 'float')):
                        sentence.append(" negative of ")
                    else:
                        sentence.append(" subtracted by ")
                elif(lom[i]['Value'] == '*'):
                    sentence.append(" multiplied with ")
                elif(lom[i]['Value'] == '/'):
                    sentence.append(" divided by ")
                elif(lom[i]['Value'] == ','):
                    sentence.append(" and ")
                elif(lom[i]['Value'] == '>'):
                    sentence.append(" is checked to see if it's greater than ")
                elif(lom[i]['Value'] == '<'):
                    sentence.append(" is checked to see if it's less than ")
                else:
                    print("FUCK")

            elif(lom[i]['Type'] == 'cmp'):
                sentence.append(" compared to ")

            elif(lom[i]['Type'] == 'forfunction'):
                sentence.append(translate.mapE(lom[i]['Value']))

            elif(lom[i]['Type'] == 'forstring'):
                sentence.append(lom[i]['Value'])

            elif(lom[i]['Type'] == 'loop'):
                sentence.append(translate.loops(lom[i]['Value']))

            elif(lom[i]['Type'] == 'decimal'):
                if(lom[i-1]['Type'] == "float"):
                    sentence.append(lom[i-1]['Value'].strip('.0') + "." + lom[i+1]['Value'].strip('.0'))
                    sentence[i-1] = ''
                i = i + 1
            i = i + 1

        x =("".join(sentence))
        return(x[0].upper() + x[1:])
    FUNCTION_DEFS2 = {
        "abs(": "absolute value of ",
        "all(": "the boolean if all of these elements are true: ",
        "any(": "the boolean if any of these elements are true:",
        # "basestring(": "",
        "bin(": "the binary string of ",
        "bool(": "the boolean value of ",
        # "bytearray(": "",
        # "callable(": "",
        "chr(": "the character string of ",
        # "classmethod(": "",
        "cmp(": "compares ",
        # "compile(": "",
        # "complex(": "",
        # "delattr(": "",
        # "dict(": "",
        # "dir(": "",
        "divmod(": "the quotient and remainder of ",
        # "enumerate(": "",
        "eval(": "the evaluated expression of ",
        # "execfile(": "",
        # "file(": "",
        # "filter(": "",
        "float(": "the floating point of ",
        # "format(": "",
        # "frozenset(": "",
        # "getattr(": "",
        # "globals(": "",
        # "hasattr(": "",
        "hash(": "the hash value of ",
        "help(": "starts the interactive help interpreter. ",
        "hex(": "the hexadecimal number of ",
        "id(": "the unique id of ",
        "input(": "prompts for input of ",
        "int(": "The integer of ",
        # "isinstance(": "",
        # "issubclass(": "",
        # "iter(": "",
        "len(": "the length of ",
        "list(": "the list of ",
        # "locals(": "",
        "long(": "the long of ",
        # "map(": "",
        "max(": "the maximum value of ",
        "memoryview(": "memory view of ",
        "min(": "the minimum value of ",
        "next(": "the next value of ",
        # "object(": "",
        "oct(": "the octal string of ",
        # "open(": "",
        "ord(": "the unicode of ",
        "pow(": "the power of ",
        "print(": "prints ",
        # "property(": "",
        "range(": "range of ",
        "raw_input(": "prompts for raw input of ",
        # "reduce(": "",
        "reload(": "reloads ",
        "repr(": "printable version of ",
        "reversed(": "the reverse of ",
        "round(": "rounds ",
        "set(": "a new set of ",
        # "setattr(": "",
        # "slice(": "",
        "sorted(": "the sorted of ",
        # "staticmethod(": "",
        "str(": "printable version of ",
        "sum(": "the sum of ",
        # "super(": "",
        # "tuple(": "",
        "type(": "the type of ",
        "unichr(": "the unicode of ",
        # "vars(": "",
        "xrange(": "the range of ",
        # "zip(": "",
        "__import__(": "imports "
    }


    def functiontoenglish(name):
        """
        Converts the given function to english version of what it does. The string will
        contain a {} of where the rest of the text should go.

        :return: If the function is not found, the function will return -1.
        """
        if name in translate.FUNCTION_DEFS2:
            return translate.FUNCTION_DEFS2[name]
        else:
            return -1


    def allfunctions():
        """
        This function returns a list of all the functions that have an english translation.
        :return: A list of function names.
        """
        return translate.FUNCTION_DEFS.keys()

    FUNCTION_DEFS = {
        'abs(', 'dict(', 'help(', 'min(', 'setattr(', 'all(', 'dir(', 'hex(', 'next(', 'slice(',
        'any(', 'divmod(', 'id(', 'object(', 'sorted(', 'ascii(', 'enumerate(', 'input(', 'oct(',
        'staticmethod(', 'bin(', 'eval(', 'int(', 'open(', 'str(', 'bool(', 'exec(', 'isinstance(',
        'ord(', 'sum(', 'bytearray(', 'filter(', 'issubclass(', 'pow(', 'super(', 'bytes(', 'float(',
        'iter(', 'print(', 'tuple(', 'callable(', 'format(', 'len(', 'property(', 'type(', 'chr(',
        'frozenset(', 'list(', 'range(', 'vars(', 'classmethod(', 'getattr(', 'locals(', 'repr(', 'zip(',
        'compile(', 'globals(', 'map(', 'reversed(', 'complex(', 'hasattr(', 'max(', 'round(', 'delattr(',
        'hash(', 'memoryview(', 'set('
    }

    SPECIAL_CHARS = {
        '+': 'op', '-': 'op', '/': 'op', '*': 'op', ',': 'op', '<': 'op', '>': 'op', '.': 'decimal', ')': 'bracket',
        '=': 'ass'
    }
    

    LOOPNAMES = {"for":" a for loop where ",
                 "in":" in the ",
                 "while": " a while loop where "}

    def loops(loopName):
        if loopName in translate.LOOPNAMES:
            return translate.LOOPNAMES[loopName]
        else:
            return -1


    def split(string):
        linespl = []
        linespl.append('')
        for i in string:
            if i == ' ':
                linespl = (re.split(r'[ ]+', string, 1))
                break
            elif i == '(':
                linespl = re.split(r'[(]+', string, 1)
                break
                
        return linespl[0], linespl[1]


    def parseExpression(rest):
        global restList
        restList = []
        temp = []
        countQ = 0
        digitFlag = 0
        prev = ''
        for i in rest:
            if i == '"':
                countQ += 1
                if countQ == 2:
                    countQ = 0
                    temp.append('"')
                    restList.append(temp)
                    temp = []
                    prev = '"'
                    continue
            if countQ == 1:
                if i == '"' or i =="'":
                    temp.append('"')
                    prev = '"'
                else:
                    temp.append(i)
                    prev = i
                continue
            if countQ == 0 and i == ',':
                temp.append(',')
                restList.append(temp)
                temp = []
                prev = ','
                continue
            elif countQ == 0 and (i.isdigit() or i == '.'):
                temp.append(i)
                restList.append(temp)
                temp = []
                prev = i
                continue
            elif countQ == 0 and ((i == '+' or i == '-' or i == '/' or i == '*') or i == ')' or (i == '<' or i == '>') or i == '='):
                if temp is not [] and prev is not '=':
                    restList.append(temp)
                    temp = []
                if i == '=' and prev == '=':
                    temp.append('==')
                    restList[-1] = temp
                    prev = '=='
                else:
                    temp.append(i)
                    restList.append(temp)
                    prev = i
                temp = []
                continue
            elif i is not ' ':
                temp.append(i)
                prev = i
                if i == '(':
                    restList.append(temp)
                    temp = []
                    continue

        lis = []
        temp = []
        num = ''
        for i in restList:
            funcFound = False
            part = ''.join(i)
            if part in translate.FUNCTION_DEFS:
                funcFound = True
            if i == ' ' or i == '' or i == []:
                continue
            elif i[0].isdigit():
                temp.append(i[0])
                continue
            if i[0] == '+' or i[0] == '-' or i[0] == '/' or i[0] == '*' or i[0] == '<' or i[0] == '>' or i[0] == ',':
                num = ''.join(temp)
                if num is not '':
                    lis.append({'Value': num, 'Type': 'float'})
                lis.append({'Value': part, 'Type': 'op'})
                num = ''
                temp = []
            elif i[0] == '.':
                num = ''.join(temp)
                if num is not '':
                    lis.append({'Value': num, 'Type': 'float'})
                lis.append({'Value': part, 'Type': 'decimal'})
                num = ''
                temp = []
            elif i[0] == '=':
                num = ''.join(temp)
                if num is not '':
                    lis.append({'Value': num, 'Type': 'float'})
                lis.append({'Value': part, 'Type': 'ass'})
                num = ''
                temp = []
            elif i[0] == '==':
                num = ''.join(temp)
                if num is not '':
                    lis.append({'Value': num, 'Type': 'float'})
                lis.append({'Value': part, 'Type': 'cmp'})
                num = ''
                temp = []
            elif i[0] == ')':
                num = ''.join(temp)
                if num is not '':
                    lis.append({'Value': num, 'Type': 'float'})
                lis.append({'Value': part, 'Type': 'bracket'})
                num = ''
                temp = []
            elif funcFound == True and part is not '(':
                lis.append({'Value': part, 'Type': 'function'})
                funcFound = False
            else:
                if part[0] is not '"' and part[0] is not "'":
                    last = part[-1]
                    start = part[:-1]
                    if last not in translate.SPECIAL_CHARS:
                        lis.append({'Value': part, 'Type': 'var'})
                    else:
                        lis.append({'Value': start, 'Type': 'var'})
                        lis.append({'Value': last, 'Type': translate.SPECIAL_CHARS[last]})
                else:
                    lis.append({'Value': part, 'Type': 'string'})
        return lis


    def parseif(raw):
        """
        Parses a string in the format of a while statement.

        :param raw: The raw form of the for loop. IE. "i in range(0,9)"
        :return: Returns a list of maps.
        """
        lom = [{"Value": "if", "Type": "loop"}]

        bracket = False
        for i in raw:
            if i == "(":
                bracket = True
                break
            elif i == " ":
                raw = raw[1:]
            else:
                break
        if raw[-1:] == ":":
            raw = raw[:-1]
        expression = raw
        if bracket:
            expression = raw[1:-1]

        translate.parseExpression(expression)

        lom.append({"Value": translate.parseExpression(expression), "Type": "forfunction"})

        return lom

    def parseelif(raw):
        """
        Parses a string in the format of a while statement.

        :param raw: The raw form of the for loop. IE. "i in range(0,9)"
        :return: Returns a list of maps.
        """
        lom = [{"Value": "elif", "Type": "loop"}]

        bracket = False
        for i in raw:
            if i == "(":
                bracket = True
                break
            elif i == " ":
                raw = raw[1:]
            else:
                break
        if raw[-1:] == ":":
            raw = raw[:-1]
        expression = raw
        if bracket:
            expression = raw[1:-1]

        translate.parseExpression(expression)

        lom.append({"Value": translate.parseExpression(expression), "Type": "forfunction"})

        return lom


    def parsefor(raw):
        """
        Parses a string in the format of a for statement.

        :param raw: The raw form of the for loop. IE. "i in range(0,9)"
        :return: Returns a list of maps.
        """
        lom = [{"Value": "for", "Type": "loop"}]

        parts = []
        for i in raw:
            if i == ' ':
                parts = (re.split(r'[ ]+', raw))

        lom.append({"Value": parts[0], "Type": "var"})
        lom.append({"Value": parts[1], "Type": "loop"})
        # Determine if function
        combined = ""
        for i in range(2, len(parts)):
            combined += " " + parts[i]
        if parts[2].split("(")[0]+"(" in translate.allfunctions():
            lom.append({"Value": translate.parsefunction(combined), "Type": "forfunction"})
        else:
            lom.append({"Value": combined, "Type": "forstring"})
        return lom


    def parsewhile(raw):
        """
        Parses a string in the format of a while statement.

        :param raw: The raw form of the for loop. IE. "i in range(0,9)"
        :return: Returns a list of maps.
        """
        lom = [{"Value": "while", "Type": "loop"}]

        bracket = False
        for i in raw:
            if i == "(":
                bracket = True
                break
            elif i == " ":
                raw = raw[1:]
            else:
                break
        if raw[-1:] == ":":
            raw = raw[:-1]
        expression = raw
        if bracket:
            expression = raw[1:-1]

        translate.parseExpression(expression)

        lom.append({"Value": translate.parseExpression(expression), "Type": "forfunction"})

        return lom


    def parsefunction(string):
        function, rest = translate.split(string)
        
        if function == "while":
            return translate.parsewhile(rest)
        elif function == "if":
            return translate.parseif(rest)
        elif function == "for":
            return translate.parsefor(rest)
        elif function == "elif":
            return translate.parseelif(rest)

        ls = (translate.parseExpression(rest))
        if (function is not 'for' or function is not 'while' or function is not 'if') and function is not '' and function is not ' ':
            ls.insert(0, {'Value': function+'(', 'Type': 'function'})
        return ls

    def pythontoenglish(self, tinput):
        return translate.mapE(translate.parsefunction(tinput))
