import random
print("Welcome to guess the number game")
def choice_difficulty():
    print("Choose diffculty level")
    print("1.Easy(1-50")
    print("2.Medium(1-100)")
    print("3.Hard(1-200)")
    while True:
        try:
            choice=int(input("Choose difficulty level: "))
            if choice==1:
                return random.randint(1,50)
            elif choice==2:
                return random.randint(1,100)
            elif choice==3:
                return random.randint(1,200)
            else:
                print("Invalid choice! Choose 1, 2, or 3.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def play_game():
    guess_number = choice_difficulty()
    guess_count = 0
    while True:
        try:
            a=int(input("Guess a number"))
            guess_count=guess_count+1
            if a>guess_number:
                print("You guessed too high!")
            elif a<guess_number:
                print("You guessed too low!")
            else:
                print(f"CONGRATS!! YOUR Guess is correct! at {guess_count} attempts")
                break
        except ValueError:
            print("INVALID NUMBER!")
def replay():
    while True:
        choice = input("Do you want to play again? (yes/no): ")
        if choice == 'yes':
            play_game()
        elif choice == 'no':
            print("Thank you for playing!")
            break
        else:
            print("Please enter 'yes' or 'no'.")

play_game()
def replay():
    while True:
        choice = input("Do you want to play again? (yes/no): ")
        if choice == 'yes':
            play_game()
        elif choice == 'no':
            print("Thank you for playing!")
            break
        else:
            print("Please enter 'yes' or 'no'.")




