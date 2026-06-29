import random

user_score = 0
computer_score = 0

while True:

    print("\n1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

    user_choice = int(input("Enter choice: "))

    if user_choice == 4:
        break

    computer_choice = random.randint(1, 3)

    if user_choice == computer_choice:
        print("Draw")

    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):

        print("You Win")
        user_score += 1

    else:
        print("Computer Wins")
        computer_score += 1

    print("Computer Choice:", computer_choice)

print("\nFinal Score")
print("User Score:", user_score)
print("Computer Score:", computer_score)