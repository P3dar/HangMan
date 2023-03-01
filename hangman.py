from ast import Continue
import random
import os


def hangman(x):
    if x == 7:
        print('''
        
        
        
        
        
        ''')
    if x == 6:
        print('''
            ______
            |     
            |    
            |    
           _|_
        ''')
    elif x == 5:
        print('''
            ______
            |     O
            |    
            |    
           _|_
        ''')
    elif x == 4:
        print('''
            ______
            |     O
            |     |
            |    
           _|_
        ''')
    elif x == 3:
        print('''
            ______
            |     O
            |    /|
            |   
           _|_
        ''')
    elif x == 2:
        print('''
            ______
            |     O
            |    /|\\
            |    
           _|_
        ''')
    elif x == 1:
        print('''
            ______
            |     O
            |    /|\\
            |    / 
           _|_
        ''')
    elif x == 0:
        print('''
            ______
            |     O
            |    /|\\       GAME OVER
            |    / \\
           _|_
        ''')


def createList(word1, word2):
    global word
    for letter in word:
        word1.append(letter)
    for letter in word:
        word2.append("*")


rePlay = True
while rePlay == True:
    lines = open("wordlist.txt").read().splitlines()
    word = random.choice(lines)
    endGame = False
    wordToGuess = []
    userWord = []
    lives = 7
    index = 0
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"]
    createList(wordToGuess, userWord)
    print("\nBenvenuto al gioco dell'impiccato!")
    print("ecco la tua parola nascosta da scoprire!")
    print("Avrai 7 tentativi, metticela tutta!")
    print("\n", *userWord, sep="")
    hangman(lives)
    while endGame == False:
        ans = input(
            "\ninserisci una lettera oppure cerca di indovinare la parola: ")
        os.system('cls')
        if len(ans) == 1 and ans in alphabet:
            alphabet.remove(ans)
            for s, letter in enumerate(wordToGuess):
                if ans == letter:
                    index = s
                    userWord[index] = ans
                    print("\nHai trovato una nuova lettera!")
                    print("Lettere disponibili rimaste: ")
                    print(*alphabet, sep="-")
                    print("\n", *userWord, sep="")

            if ans not in wordToGuess:
                lives -= 1
                print("\nSbagliato!")
                print("Lettere disponibili rimaste: ")
                print(*alphabet, sep="-")
                print("\n", *userWord, sep="")
        elif len(ans) == 1 and ans not in alphabet:
            print("\nHai già usato questa lettera, scegline un'altra!")
            print("Lettere disponibili rimaste: ")
            print(*alphabet, sep="-")
            print("\n", *userWord, sep="")
        elif len(ans) > 1:
            if ans == word:
                print("\nLa risposta è esatta!!! Hai vinto!")
                endGame = True
                print("\nLa parola è: ", *wordToGuess, sep="")
            else:
                lives -= 1
                print("\nSbagliato!")
                print("Lettere disponibili rimaste: ")
                print(*alphabet, sep="-")
                print("\n", *userWord, sep="")

        if wordToGuess == userWord and lives > 0:
            print("\nCongratulazioni! sei riuscito a scoprire la parola!")
            endGame = True
        elif lives == 0:
            print("\nMi spiace, non hai più vite, hai perso :(")
            print("La parola era: ", *wordToGuess, sep="")
            endGame = True
        hangman(lives)

    print("Vuoi  giocare ancora?")
    playAgain = input("y/n: ")
    if playAgain == "y":
        endGame = False
        os.system('cls')
    else:
        rePlay = False

print("Alla proissima partita!!!")
