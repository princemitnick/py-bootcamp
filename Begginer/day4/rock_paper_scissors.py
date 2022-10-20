import random
"""
rock wins against scissors.
scissors win against paper.
paper wins agains rock.
"""

# Rock
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

rock_int = 0
paper_int = 1
scissors_int = 2

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
#print (your_choice)

computer_choice = random.randint(0,2)
#print(computer_choice)
'''
if your_choice == 0:
    print(rock)
    if computer_choice == 2:
        print(f"Computer choice: \n{scissors}")
        print("You win.")
    elif computer_choice == 1:
        print(f"Computer choice : \n{paper}")
        print("You lose.")
    else:
        print("It's a draw.")

if your_choice == 1:
    print(paper)
    if computer_choice == 0:
        print(f"Computer choice: \n{rock}")
        print("You win.")
    elif computer_choice == 2:
        print(f"Computer choice: \n{scissors}")
        print("You lose.")
    else:
        print("Its a draw.")

if your_choice == 2:
    print(scissors)
    if computer_choice == 1:
        print(f"Computer choice : \n{paper}")
        print("You win.")
    elif computer_choice == 0:
        print(f"Computer choice : \n{rock}")
        print("You lose.")
    else:
        print("It's a draw.")
'''
####################################################################

if your_choice >= 3 or your_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    game_images = [rock, paper, scissors]
    print(f"Your choice : \n{game_images[your_choice]}")
    print(f"Computer choice : \n{game_images[computer_choice]}")
    if your_choice == 0 and computer_choice == 2:
        print("You win.")
    elif computer_choice == 0 and your_choice == 2:
        print("You lose.")
    elif your_choice > computer_choice:
        print("You win.")
    elif computer_choice > your_choice:
        print("You lose.")
    else:
        print("It is a draw.")



"""
rock (0) wins against scissors(2).
scissors(2) win against paper(1).
paper(1) wins agains rock(0).
"""