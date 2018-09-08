def euler98():
    # import urllib2
    # text = urllib2.urlopen("https://projecteuler.net/project/resources/p098_words.txt").readlines()
    # words = [i.strip("\"") for i in text[0].split(',')]

    # anagrams = []
    # for i in range(len(words)):
    #     print i
    #     for j in range(i+1,len(words)):
    #         if len(words[i])==len(words[j]) and sorted(words[i])==sorted(words[j]):
    #             anagrams.append((words[i],words[j]))
    anagrams = [('ACT', 'CAT'), ('ARISE', 'RAISE'), ('BOARD', 'BROAD'), ('CARE', 'RACE'), ('CENTRE', 'RECENT'), ('COURSE', 'SOURCE'), ('CREATION', 'REACTION'), ('CREDIT', 'DIRECT'), ('DANGER', 'GARDEN'), ('DEAL', 'LEAD'), ('DOG', 'GOD'), ('EARN', 'NEAR'), ('EARTH', 'HEART'), ('EAST', 'SEAT'), ('EAT', 'TEA'), ('EXCEPT', 'EXPECT'), ('FILE', 'LIFE'), ('FORM', 'FROM'), ('FORMER', 'REFORM'), ('HATE', 'HEAT'), ('HOW', 'WHO'), ('IGNORE',
                                                                                                                                                                                                                                                                                                                                                                                                                                         'REGION'), ('INTRODUCE', 'REDUCTION'), ('ITEM', 'TIME'), ('ITS', 'SIT'), ('LEAST', 'STEAL'), ('MALE', 'MEAL'), ('MEAN', 'NAME'), ('NIGHT', 'THING'), ('NO', 'ON'), ('NOTE', 'TONE'), ('NOW', 'OWN'), ('PHASE', 'SHAPE'), ('POST', 'SPOT'), ('POST', 'STOP'), ('QUIET', 'QUITE'), ('RATE', 'TEAR'), ('SHEET', 'THESE'), ('SHOUT', 'SOUTH'), ('SHUT', 'THUS'), ('SIGN', 'SING'), ('SPOT', 'STOP'), ('SURE', 'USER'), ('THROW', 'WORTH')]

    def word_to_square(square, word1, word2):
        if len(str(square))!=len(word1):
            return 2
        letters = {}
        for i in range(len(word1)):
            letters[word1[i]] = str(square)[i]
        out = ""
        for i in word2:
            out += letters[i]
        return int(out)

    def is_square(x):
        return (x**0.5) % 1. == 0
    out = []
    for word_pair in anagrams:
        word1 = word_pair[0]
        word2 = word_pair[1]
        lo = int((10**(len(word1)-1))**0.5)
        hi = int((10**(len(word1)))**0.5)
        potential_squares = [i*i for i in range(lo-1, hi+1)]
        for square1 in potential_squares:
            square2 = word_to_square(square1, word1, word2)
            if is_square(square2) and square1 == word_to_square(square2, word1, word2) and square1 != square2:
                print word1, word2, square1, square2
    return out


print euler98()
