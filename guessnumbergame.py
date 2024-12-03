import random
secret_number=random.randint(1,100)
print("Welcome to Guess Number Game")
guess_count=0
while True:
    guess_number=int(input("Guess the number between 1 and 100:"))
    guess_count+=1
    if guess_number>secret_number:
        print("Too high")
    elif guess_number<secret_number:
        print("Too low")
    else:
        print(f"congratulations !!!🥳You have guessed the number in count {guess_count}")
        break


