import random
import time

name=input("What is your name? ")
print("Good luck! ", name)
gameWords=['python', 'java','PHP','javaScript', 'computer', 'geeks', 'keyboard','laptop', 'headphone', 'hardware','software','Pasta','Football','Basketball' ]
# use the choice method of my random fucntion to pick a gameWords
answer=input('do you want to guess a word ')

while answer == 'yes':
    word= random.choice(gameWords)
    guesses =''
    final = ''
    turns=10
    while turns>0:
        for char in word:
            if char in guesses:
                print(char,end = '')
                final = final + char
            else:
                print('_', end = '')
        print(' ')
        if word in final: 
            print('you win')
            print("the word is: "+ word)
            break 
        guess= input("give me a letter: ") #Controls the guessing part of the game 
        guesses += guess
        if guess not in word:
            turns-=1
            print("you have ",end = '')
            print(turns, end = '')
            print()
        if turns == 0: #Ends the game once you run out of turns
            print('Game Over')
            break
    answer=input('do you want to play again')
time.sleep(5)
