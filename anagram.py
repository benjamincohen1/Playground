# Example anagram:   a decimal point = im a dot in place
# Example input: ['a', 'dot', 'im', 'in', 'place', 'blah', 'foo'], 'a decimal point'
# Example result: 'im a dot in place'
#['an','a','not'],nota
import itertools
def anagramFinder(wordList, phrase):
    phraseAsList = [x for x in phrase if x!=" "]
    returnList = []
    wordsToRemove=[]
    for word in wordList:
        if not isSubset(word,phraseAsList):
            wordsToRemove.append(word)
    for x in wordsToRemove:
        wordList.remove(x)    
    combos=[]
    length=len(wordList)
    passed=[]
    for x in range(1,length+1):
        combos+=(list(itertools.combinations(wordList,x)))
    for c in combos:
        if letCount(c) == len(phraseAsList):
            passed.append(c)
    for solution in passed:
        if(isSubset(phraseList(solution),phrase)):
            return solution
def letCount(p):
    total=0
    for x in p:
        total+=len(x)
    return total
def isSubset(s1,s2):
    for x in s1:
        if s1.count(x) > s2.count(x) or s2.count(x) == 0:
            return False
            
    return True
    

def phraseList(phrase):
    phraseList=[]
    for x in phrase:
        for let in x:
            if x !=" ":
                phraseList.append(let)
    return phraseList

def subset(s1,s2):
    for x in s1:
        if x not in s2:
            return False
    return True
