import time
import random
from words import word_list


def username(name):
    print("Welcome ",name)


def solution():
    word = random.choice(word_list)
    return word.upper()


def hangman():
    word = solution()
    secretword = "_ " * len(word)
    life = 6
    used_letters = []
    right_letters = []
    used_words = []
    print("Let the games start")
    print(life_state(life))
    print(secretword)
    solv = False

    while life >0 and not solv:
        user_input = input("Enter a word or letter: ").upper()
        if len(user_input) == 1 and user_input.isalpha():
            if user_input in used_letters:
                print("Already used")
                life = life-1
            elif user_input not in word:
                print(user_input, "Not in the word")
                life = life-1
                used_letters.append(user_input)
            else:
                print("Right!!!", user_input, "will reaveal itself")
                used_letters.append(user_input)
                right_letters.append(user_input)
                print(right_letters)


        elif len(user_input) > 1 and len(user_input)<=len(word) and user_input.isalpha():
            if user_input == word:
                solv==True

            elif user_input != word:
                used_words.append(user_input)
                print("Wrong")
                life = life-1

            elif user_input in used_words:
                print("Already used")
                life = life-1                  
        else:
            print("Not a valid answer")

        if(life>0):
            print(life_state(life))

        else:
            print(life_state(1))
            solv=False

        print(secretword + "\n" )

    if solv:
        print("You Won!!!")
    else:
        print("You Lost")

    
def life_state(life):
    stages = [
        """...... :)"""
        ,
        """.>.... :/"""
        ,
        """..>... :("""
        ,
        """...>.. :- """
        ,
        """....>. :o"""
        ,
        """.....> :-O"""
        ,
        """...... -.-"""
    ]
    return stages[7-life]      
    

if __name__ == "__main__":
    name = input('Enter user name:')
    username(name)
    hangman()
    if input("Again? (Y/N) ").upper() == "Y":
        x = True
    else:
        x = False

    while x:
        name = input('Enter user name:')
        username(name)
        hangman()
        if input("Again? (Y/N) ").upper() == "Y":
            x = True
        else:
            x = False
            break
     
    
