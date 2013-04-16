def closeBracket(openbracket):
    if openbracket == '{':
        return '}'
    elif openbracket == '(':
        return ')'
    elif openbracket == '[':
        return ']'
 
if __name__ == "__main__":
    testcase = "{{[{{{{}}{{}}}[]}[][{}][({[(({{[][()()]}}{[{{{}}}]}))][()]{[[{((()))({}(())[][])}][]()]}{()[()]}]})][]]}{{}[]}}"
    teststack = []
    position = 0
 
    for c in testcase:
        if c == '{' or c == '(' or c == '[':
            #push the open character on the stack
            teststack.append(c)
        
        if c == '}' or c == ')' or c == ']':
            #check first to see if the stack is empty and
            #if it is report the position
            if not teststack:
                print "Failed at position %d" % position
                break
            #it's not empty, so pop the last appended character off
            f = teststack.pop()
            #if this character is the respective close character
            #of the character that got popped off, we're good
            if closeBracket(f) == c:
                print "All good at position %d" %  position
            #if the popped character isn't the respective close
            #character, then fail and report position
            elif closeBracket(f) != c:
                print "Failed at position %d" % position
        position = position + 1