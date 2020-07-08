class Guess:

    def __init__(self, word):
        self.secretWord = word
        self.guessedChars = set()
        self.numTries = 0
        self.currentStatus = '-' * len(word)
        self.reSeceretWord = word    # seceretWord에서 guessedChars를 뺀 값 - 중복 처리를 위해

    def display(self):
        print('Current: ' + self.currentStatus)
        print('Tries: ' + str(self.numTries))


    def guess(self, character):
        self.guessedChars.add(character)
        # 사용자가 입력한 문자가 secretWord 에 중복된 문자일 때 처리
        if character in self.reSeceretWord:
            while character in self.reSeceretWord:
                self.idx = self.reSeceretWord.find(character)
                self.currentStatus = self.currentStatus[:self.idx] + character + self.currentStatus[self.idx+1:]
                self.reSeceretWord = self.reSeceretWord[:self.idx] + '-' + self.reSeceretWord[self.idx+1:]

        else:
            self.numTries += 1
            return False


        if self.currentStatus == self.secretWord:
            return True




