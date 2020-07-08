import random

class Word:

    def __init__(self, filename):
        self.words = []
        f = open(filename, 'r')
        lines = f.readlines()   #lines : 리스트 타입. 파일에 있는 내용을 한 줄씩 계속 읽어들여 리스트에 저장한다.
        f.close()

        self.count = 0
        for line in lines:
            word = line.rstrip()    # 제일 오른쪽에 있는 문자 '\n'을 뺀다.(제어문자를 하나의 문자로 인식)
            self.words.append(word)
            self.count += 1

        print('%d words in DB' % self.count)


    def test(self):
        return 'default'


    def randFromDB(self):
        r = random.randrange(self.count)
        return self.words[r]

