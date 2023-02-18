import game_data
import art
import random
import os

score = 0
all_Particepent_data = game_data.data
print(art.logo)


def random_num():
    return random.randint(0, len(all_Particepent_data)-1)


def choices():
    first_person = all_Particepent_data[random_num()]
    second_person = all_Particepent_data[random_num()+1]
    return first_person, second_person
def print_fun(acoount):
  return f"{acoount['name']} a {acoount['description']}, from {acoount['country']}. Cheat {acoount['follower_count']}"

def userChosen():
    abc = choices()
    print(f"Compare A:{print_fun(abc[0])}")
    print(art.vs)
    print(f"Against B:{print_fun(abc[1])}")
    Choice = input(" Who has more followers? Type 'A' or 'B': ").upper()
    new_lists = {"A": abc[0]["follower_count"], "B": abc[1]["follower_count"]}
    if Choice == "A":
        return new_lists[Choice], new_lists["B"]
    else:
        return new_lists[Choice], new_lists["A"]


firstCall = userChosen()
while firstCall[0] > firstCall[1]:
    os.system('clear')
    print(art.logo)
    score += 1
    print(f"You're right! Current score:{score}")
    firstCall = userChosen()

os.system('clear')
print(art.logo)
print(f"Sorry, that's wrong. Final score: {score}")
