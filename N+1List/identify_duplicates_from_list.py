import random


#just a random list generator
#takes an integer and randomly chooses numbers from 1 up to that integer
#creates a list of length n+1 eg: 10 would return a list of length 11
def create_list_from_int(num):
    choicesList = []
    for i in range(num+1):
        choicesList.append(random.randint(1, num))
    return choicesList

#function takes in a list and prints out only numbers that appear more than once
def print_duplicates_in_list(list):
    for i in range(1, len(list)):
        if list.count(i) > 1:
            print(i)


#call the print duplicate process passing in the raandom list creator function
#I like the single line but slightly unhappy with the readability.
print_duplicates_in_list(create_list_from_int(3))
