import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


random_index = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))

if random_index == 0:
    print(rock)
elif random_index == 1:
    print(paper)
elif random_index == 2:
    print(scissors)
else:
    print("Error. Incorrect input.")


print("The computer chooses:")
computer_index = random.randint(0, 2)
if computer_index == 0:
    print(rock)
elif computer_index == 1:
    print(paper)
elif computer_index == 2:
    print(scissors)
else:
    print("Error. Incorrect input.")


if random_index == computer_index:
    print("Draw")
elif random_index == 0 and computer_index == 2:
    print("You win")
elif random_index == 1 and computer_index == 0:
    print("You win")
elif random_index == 2 and computer_index == 1:
    print("You win")
else:
    print("You lose")
