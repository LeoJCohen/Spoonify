vowels = ['a', 'e', 'i', 'o', 'u']


def vowel(word):
    w = [*word]
    c = w[0]
    for j in range(len(vowels)):
        if vowels[j] == c:
            boolean = True
            break
        else:
            boolean = False
    return boolean



def getFirstCons(word):
    w = [*word]
    new = ''
    for int in range(len(w)):
        if vowel(w[int]):
            break
        else:
            new += w[int]
    return new


def spoonify(words):
    word = words.split(" ")
    word1 = word[0]
    word2 = word[1]
    fir1 = getFirstCons(word1)
    fir2 = getFirstCons(word2)
    w1 = word1.replace(fir1, fir2, 1)
    w2 = word2.replace(fir2, fir1, 1)
    return w1 + " " + w2


# i = input("Input two words: ")
# split = i.split(' ')
# word1 = i[0]
# word2 = i[1]


i = input("\nInput two words: ")
print(spoonify(i))
