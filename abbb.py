def char_freq(inputString):
    dictionary = {}
    print(inputString)

    for i in range(len(inputString)):

        if inputString[i] in dictionary:
            dictionary[inputString[i]] = int(dictionary.get(inputString[i])) + 1
        else:
            dictionary[inputString[i]] = 1

    return dictionary


print(str(char_freq("abbabcbdbabdbdbabababcbcbab")))