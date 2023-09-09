
def mergeSortRev(list):
    if len(list) > 1:
        a = len(list)//2
        l = list[:a]
        r = list[a:]
        mergeSortRev(l)
        mergeSortRev(r)
        b = c = d = 0
        while b < len(l) and c < len(r):
            if len(l[b]) > len(r[c]):
                list[d] = l[b]
                b += 1
            else:
                list[d] = r[c]
                c += 1
            d += 1
        while c < len(r):
            list[d] = r[c]
            c += 1
            d += 1
        while b < len(l):
            list[d] = l[b]
            b += 1
            d += 1

# def dictionary(file):
#     list=[]
#     with open(file) as f:
#         lines = f.readlines()
#     for word in lines:
#         if len(word) > 3:
#             word = word.replace("\n", "").upper()
#             list.append(word)
#     return list

def newList():
    str, list = 'ABCDEFGHIJLMNOPQRSTUV',[]
    for letter in str:
        list.append(letter)
    return list
def lettersClearer(word, lettersList):
    for letter in word:
        if letter in lettersList:
            lettersList.remove(letter)
        if len(lettersList) == 0:
            return newList()
    return lettersList
def search(dictionary, syllable):
    for word in dictionary:
        if syllable in word:
            return word

def inWord(word, lettersList, syllable, amount):
    copy = lettersList[:]
    for letter in syllable:
        if letter in copy:
            copy.remove(letter)
    if len(copy) == 0:
        return True

    while amount > 0 and len(copy) > 0:
        if copy[-1] in word and syllable in word:
            amount -=1
        copy.pop()
    if amount == 0:
        return True
    return False



def lettersBias(dictionary, lettersList, syllable):
    remaining = len(lettersList)
    if remaining < 3:
        for word in dictionary[::-1]:
            if inWord(word, lettersList, syllable, 2) or inWord(word, lettersList, syllable, 1):
                return word

        return search(dictionary[::-1], syllable)

    elif remaining < 9:
        for word in dictionary:
            if inWord(word, lettersList, syllable, 3) or inWord(word, lettersList, syllable, 2):
                return word

        return search(dictionary, syllable)

    elif remaining < 14:
        for word in dictionary:
            if inWord(word, lettersList, syllable, 4) or inWord(word, lettersList, syllable, 3):
                return word

        return search(dictionary, syllable)
    return search(dictionary, syllable)


letters = newList()

