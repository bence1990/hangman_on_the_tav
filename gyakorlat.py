import random


def generate_random_word(my_list):
    value = random.randint(0, len(my_list)-1)
    return my_list[value]


def read_file(file_name):
    with open(file_name, "r") as my_list:
        for item in my_list:
            my_list = item.split(' ')
    return my_list


def get_guess():
    guess = ""
    while len(guess) != 1:
        guess = input("Write your guess: ")
    return guess


def print_underscore(random_word):
    underscore = len(random_word) * '*'
    return underscore


def check_guess(random_word, guess):
    index_list = []
    if guess in random_word:
        for random in range(0, len(random_word)):
            if random_word[random] == guess:
                index_list.append(random)
        return index_list
    else:
        return index_list


def fill_underscore(index_list, underscore, guess):
    underscore = list(underscore)
    for index in index_list:
        underscore[index] = guess
    underscore = ''.join(underscore)
    return underscore


def main():
    random_word = generate_random_word(read_file("lista.txt"))
    underscore = print_underscore(random_word)
    counter = 0
    while counter < len(random_word):
        guess = get_guess()
        index_list = check_guess(random_word, guess)
        print(fill_underscore(index_list, underscore, guess))
        counter += 1


if __name__ == '__main__':
    main()
