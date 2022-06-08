from asyncio.windows_events import NULL
import random

with open("MyFile.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))


def display(lives):
    if (lives == 4):
        print('    O')
        print('   /|\\')
        print('    /\\')
    elif (lives == 3):
        print('    O')
        print('   /|\\')
    elif (lives == 2):
        print('    O')
        print('    |')
    elif (lives == 1):
        print('    O')


def playAgain():
    print('play again?')
    playAgain = input('y/n: ')
    if (playAgain == 'y'):
        return True
    return False


def main():
    lives = 4
    guessedLetters = []
    playGame = True
    score = 0
    word = random.choice(words)
    word = list(word)
    print(word)

    print('Welcome!')
    while (playGame):
        correctGuess = False
        display(lives)
        guess = input('make a guess of a character! ')
        if (guess in guessedLetters):
            print(str(guess) + ' already guessed!')
        else:
            for letter in range(0, len(word)):

                if (guess == word[letter]):
                    print('correct!')
                    guessedLetters.append(guess)
                    score = score + 1
                    word[letter] = NULL
                    correctGuess = True
                    break
            if (correctGuess == False):
                guessedLetters.append(guess)
                print('wrong!')
                lives = lives - 1
        print('score is: ' + str(score) + '\n')

        # Check game conditions
        if (lives <= 0):
            print('you lost!')
            playGame = playAgain()
        if (score >= len(word)):
            print('you win!')
            playGame = playAgain()


main()
