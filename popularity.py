def popularity(text):
    if not(isinstance(text, str)):
        return 'Argument of function is not string'
    text = text.strip()
    if (len(text) == 0):
        return 'Argument of function is empty'
    listWords = text.lower().split()
    dictWords = dict()
    sortedList = list()
    for word in listWords:
        if word in dictWords:
            dictWords[word] = dictWords[word] + 1
        else:
            dictWords[word] = 1
    sortedDictWords = dict(sorted(dictWords.items(), key=lambda x: x[0]))
    sortedListWords = sorted(sortedDictWords.items(), key=lambda x: x[1], reverse=True)
    for word in sortedListWords:
        sortedList.append(word[0])
    return sortedList

print(popularity('apple kiwi pineapple kiwi apple kiwi'))
print(popularity('aPPle pine Apple kiwi Apple kiwi'))
print(popularity('aPPle pine Apple kiwi Apple kiwi'))
print(popularity('aab aaa aac aab aac aaa x'))
print(popularity('cat funt dog BIg dog  cAt mouse  cat'))