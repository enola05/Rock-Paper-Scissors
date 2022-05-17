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
options=[rock, paper, scissors]
user_choice=input("0 - Rock\t 1 - Paper\t 2 - Scissors\nEnter your choice ")
print(options[int(user_choice)])
comp_choice=random.choice(options)
print("Computer chose")
print(comp_choice)
if user_choice == "0" :
  if comp_choice == rock:
    print("It's a draw")
  elif comp_choice == paper:
    print("You lose")
  elif comp_choice == scissors:
    print("You win")

elif user_choice == "1" :
  if comp_choice == rock:
    print("You win")
  elif comp_choice == paper:
    print("It's a draw")
  else:
    print("You lose")

elif user_choice == "2" :
  if comp_choice == rock:
    print("You lose")
  elif comp_choice == paper:
    print("You win")
  else:
    print("It's a draw")
#Write your code below this line 👇

