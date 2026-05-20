import random

secret_number = random.randint(1, 10)
guess = 0

print("Maine 1 se 10 ke beech number socha hai")
print("Guess kar bhai!")

while guess != secret_number:
    guess = int(input("Tera guess: "))
    
    if guess < secret_number:
        print("Chota hai. Bada soch")
    elif guess > secret_number:
        print("Bada hai. Chota soch")
    else:
        print("BOOM! Sahi pakda bhai 🔥")
        print("Number tha:", secret_number)

print("Game khatam. Tu jeet gaya 💯")     
   