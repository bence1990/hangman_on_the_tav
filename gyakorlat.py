import random


def random_genearted_word(my_list):
    value=random.randint(0,len(my_list)-1)
    return my_list[value]

         
def file_reading(file_name):
    with open(file_name, "r") as my_list:
        for item in my_list:
            my_list = item.split(',')
    return my_list



def main(): 
    print (random_genearted_word(file_reading("lista.txt")))

if __name__ == '__main__':
    main()