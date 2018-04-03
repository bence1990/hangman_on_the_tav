def get_guess():
    guess_list = []
    while len(guess_list) != 1:
        guess = input("Write your guess: ")
        guess_list.append(guess)
    return guess_list
