<<<<<<< HEAD




def palTest(string):
    """
    A function that takes a string and tests if that string
    is a palindrome. Returns True or False.
    """
    stringA = string
    stringB = string
    stringBIndex = len(stringB) - 1

    for i in range(len(stringA)):
        if stringA[i] == stringB[stringBIndex]:
            result = True
        else:
            result = False
            pass # TODO is this the same as a break statement?
        stringBIndex -= 1

    return(result)



=======
#!/usr/bin/python3



def palTest(pal):
    pal1 = pal
    pal2 = pal
    pal2Index = len(pal) - 1
    for i in range(pal1.length):
        if pal1[i] == pal2[pal2Index]:
            result = True
        else: 
            result = False
        pal2Index -= 1
    return(result) # boolean


def listMaker(bigString, i):
    """
    Function takes a string and an integer index and returns nested lists of strings
    """
    lists = []
    if i <= len(a) - 1:
        start = 0
        end   = i * 2   # i is being treated as the midpoint here
    else:
        start = len(a) - (i * 2)
        end   = len(a) - 1
    while start < (end/2):
        if start == end:
            lists.append(bigString[start])
        else:
            if palTest(bigString[start:end]):
                lists.append(bigString[start:end])
        start += 1
        end   -= 1
    return(lists)


def main():
    text = input('Please enter a possible palindrome')
    
    finalResult = []
    finalResult = [listMaker(text, i) for i in range(len(a)-1)]

if __name__ == '__main__':
    main()
        
            
>>>>>>> 9c6d8b484d6504bddb1368adfaaf584cdbe88497
