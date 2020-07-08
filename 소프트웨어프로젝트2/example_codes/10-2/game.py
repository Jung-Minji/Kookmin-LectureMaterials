from hangman import Hangman
from guess import Guess
from word import Word

def gameMain():
    word = Word('words.txt')
    guess = Guess(word.randFromDB())
    # 플레이어가 맞춰야 할 단어가 인자로 들어간 객체 생성

    finished = False
    hangman = Hangman()
    maxTries = hangman.getLife()    # 6번

    while guess.numTries < maxTries:

        display = hangman.get(maxTries - guess.numTries)    # 행맨 그림
        print(display)  # 그냥 display하면 개행문자가 보인다!!
        guess.display()

        guessedChar = input('Select a letter: ')
        if len(guessedChar) != 1:
            print('One character at a time!')
            continue
        if guessedChar in guess.guessedChars:
            print('You already guessed \"' + guessedChar + '\"')
            continue

        finished = guess.guess(guessedChar)
        if finished == True:
            break

    if finished == True:
        print('Success')
    else:
        print(hangman.get(0))
        print('word [' + guess.secretWord + ']')
        print('guess [' + guess.currentStatus + ']')
        print('Fail')


if __name__ == '__main__':
    gameMain()
