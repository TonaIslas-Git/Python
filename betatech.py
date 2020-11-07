#!/usr/bin/python3
lst = []
SBL = 0
SBR = 0
PL = 0
PR = 0
CBL = 0
CBR = 0
SBF = False
PF = False
CBF = False

class Stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items==[]
    def push(self, data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
s= Stack()

entry = input("Enter a valid string of characters. e.g [],(),{}, or a combination of them : ")
#regex here
if len(entry) > 0:
    lst = entry
    if lst[0] == ")" or lst[0] == "}" or lst[0] == "]":
        print ("First Character is " + lst[0] + " that means an error since the begining")
        exit
    else:
        for char in lst:
            if char == "[":
                SBL = SBL + 1
            elif char == "]":
                SBR = SBR + 1
            elif char == "(":
                PL = PL + 1
            elif char == ")":
                PR = PR + 1
            elif char == "{":
                CBL = CBL + 1
            elif char == "}":
                CBR = CBR + 1
            s.push(char)
    sum_chars = [SBL,SBR,PL,PR,CBL,CBR]
    total = sum(sum_chars)
    if (total % 2) == 0:
        print("The total number is correct " + str(total))
        if SBL == SBR:
            SBF = True
        if PL == PR:
            PF = True
        if CBL == CBR:
            CBF = True
        if (SBF and PF and CBF):
            print("The chars match")
        else:
            print("The chars are not matching")
    else:
        print("The total is NOT correct")
else:
    print("Must enter a string, bye")
