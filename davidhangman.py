def get_guess():
    guess = ""
    while len(guess) != 1:
        guess = input("Write your guess: ")
    return guess


print(get_guess())