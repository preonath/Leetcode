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


