import random 

#Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

#Number of attempts
attempts= 0

print("Welcome to the Number Guessing Game! ")
print("I'm thinking of a number between 1 and 100")

while True:
    try:    
        guess = int(input("Take a guess: "))
        attempts +=1

        if guesss < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
              print("Too high! Try Again!")
        else:
              print(f"Congratulations! You guessed the number in{attempts} attempts.")      
              break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

