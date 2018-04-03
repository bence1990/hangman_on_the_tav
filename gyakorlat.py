import random


def random_genearted_word(my_list):
    value = random.randint(0, len(my_list)-1)
    return my_list[value]


def file_reading(file_name):
    with open(file_name, "r") as my_list:
        for item in my_list:
            my_list = item.split(',')
    return my_list

def if_input_in_list(guess_char,get_guess):
    typed_char = []
    while True:
        if get_guess in typed_char:
            print ("Sorry...Try something else")
            get_guess
        
        
        


if __name__ == '__main__':
    main()