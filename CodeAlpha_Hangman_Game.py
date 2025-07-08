import random
def hangman():
    words = ['python', 'java', 'c programming', 'javascript', 'hangman']
    chosen = random.choice(words)
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = 6

    display = ['_'] * len(chosen)

    while wrong_guesses < max_wrong and '_' in display:
        print('\nCurrent word:', ' '.join(display))
        print(f'Wrong guesses left: {max_wrong - wrong_guesses}')
        guess = input('Guess a letter: ').lower()

        if len(guess) != 1 or not guess.isalpha():
            print('Enter a single alphabetical character.')
            continue

        if guess in guessed_letters:
            print('You already guessed that letter.')
            continue

        guessed_letters.add(guess)

        if guess in chosen:
            for idx, ch in enumerate(chosen):
                if ch == guess:
                    display[idx] = guess
            print('Good guess!')
        else:
            wrong_guesses += 1
            print('Wrong guess!')

    if '_' not in display:
        print('\nCongratulations, you won! The word was', chosen)
    else:
        print('\nGame over! The word was', chosen)

if __name__ == '__main__':
    hangman()