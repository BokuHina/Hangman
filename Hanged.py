import random
from wordfreq import top_n_list
def body_of_game(count, str, sicret_word):
    use_let = list()
    while count > 0:
        print(str)
        letter = input("write a letter: ").lower()
        if letter in use_let:
            print("This letter already exists")
        elif letter not in sicret_word:
            use_let.append(letter)
            count -= 1
            print("There is no such letter")
        else:
            for j in range(n):
                if sicret_word[j] == letter:
                    str = str[:j] + letter + str[j + 1:]
            use_let.append(letter)
            print("There is such a letter")
            if str == sicret_word:
                print("You guessed the word!\n")
                return True
    if count == 0:
        print("You've run out of lives(\n")
        return False
print("WELCOME TO HUNGMEN!\n")

word_list = top_n_list("en", 500)
win_count, lose_count = 0, 0
while True:
    user = input("Enter play to start, \nresults to look at your account, \nexit to end the game ").lower()
    count = 8
    if user == "play":
        sicret_word = random.choice(word_list)
        n = len(sicret_word)
        str = "-" * n
        flag = body_of_game(count, str, sicret_word)
        if flag:
         win_count += 1
        else:
            lose_count += 1
    elif user == "results":
        print(f"Win {win_count} \nLose {lose_count}" )
    elif user == "exit":
        print("You have left the game")
        break
    else:
        print("unknown command")
