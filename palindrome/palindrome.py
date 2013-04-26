



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



