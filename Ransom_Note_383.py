### Brute Force Approch ####

def canConstruct(ransomNote, magazine):
   
    magazine= list(magazine)

    for i in ransomNote:
        if i in magazine:
            magazine.remove(i)
        else:
            False
    return True

ransomNote=str(input())
magazine=str(input())
canConstruct(ransomNote, magazine)



### Hash Table ####

def canConstruct(ransomNote, magazine):
    note,mag = Counter(ransomNote), Counter(magazine)

    if mag == note: 
        return True
    return False

# ransomNote="fihjjjjei"
# magazine="hjibagacbhadfaefdjaeaebgi"
ransomNote="preonath"
magazine="preonath"

canConstruct(ransomNote, magazine)


####
