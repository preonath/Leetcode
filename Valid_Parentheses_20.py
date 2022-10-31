from pip._vendor.progress.counter import Stack
from pip._vendor.pyparsing import empty
def pair(e1,e2):
    if e1=="(" and e2==")":
        return True
    elif e1=="[" and e2=="]":
        return True
    elif e1=="{" and e2=="}":
        return True
    else:
        return False

def is_balanced(given_string):
    s = Stack()
    balance=True
    index=0
    while (index<len(given_string) and balance):
        element=given_string[index]
        if element in "[({":
            s.push(element)
        else:
            if s is empty():
                balance=False
            else:
                top=s.pop()
                if not pair(top,element):
                    balance=False
        index=index+1
    if s is empty and balance:
        return True
    else:
        return False
s=input()
print(s)
print(is_balanced(s))


### LAst time Solution ###

def isValid(s):
        if len(s) % 2 != 0:
            return False
        dict = {'(' : ')', '[' : ']', '{' : '}'}
        print(f"Dictionary key {dict.keys()}")
        stack = []
        for i in s:
            print(f"String: {i}")
            
            if i in dict.keys():
                print(f"Keying {i}")
                stack.append(i)
            else:
                if stack == []:
                    return False
                a = stack.pop()
                print(f"Poping {a}")
                print(f"Dictionary Poping {dict[a]}")
                # if i!= dict[a]:
                    
#                     return False
#         return True
s='(){}'
isValid(s)
            
dict = {'(' : ')', '[' : ']', '{' : '}'}
