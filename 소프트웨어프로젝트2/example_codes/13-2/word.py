import random

class Word:

    def __init__(self, filename):
        self.words = []
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()

        self.count = 0
        for line in lines:
            word = line.rstrip()
            self.words.append(word)
            self.count += 1

        print('%d words in DB' % self.count)


    def test(self):
        return 'default'


    def randFromDB(self, minLength):
        r = random.randrange(self.count)
        selected = False
        max_len = len(max(self.words, key=len))
        if max_len < minLength:
            minLength = max_len

        while not selected:
            if len(self.words[r]) >= minLength:
                selected = True
            else:
                r = random.randrange(self.count)

        return self.words[r]

