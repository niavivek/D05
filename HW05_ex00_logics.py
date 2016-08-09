#!/usr/local/bin/python3
# HW05_ex00_logics.py


##############################################################################
def even_odd():
    """ Print even or odd:
        Takes one integer from user
            accepts only non-word numerals
            must validate
        Determines if even or odd
        Prints determination
        returns None
    """
    #get an input from user
    try:
        user_input = int(input("Enter an integer: "))
    #is not an integer, print error 
    except:
        print("Not a number")
    #if the input is int, determine if odd or even
    else:
        if (user_input % 2) == 0 or (user_input == 0):
            print("%d is even" % user_input)
        else:
            print("%d is odd" % user_input)
    #return none
    return


def ten_by_ten():
    """ Prints integers 1 through 100 sequentially in a ten by ten grid."""
   # counter for line
    for line_counter in range(0,10):
        # values 1 to 10
        for int_to_print in range(1,11):
            # each number is line number times 10 + integer from 1 to 10
            print("%-3d" % ((line_counter * 10) + int_to_print), end = " ") #formats to 3 digit integer
        print() # goes to next line


def find_average():
    """ Takes numeric input (non-word numerals) from the user, one number
    at a time. Once the user types 'done', returns the average.
    """
    #initialize user input
    user_input = ""
    total_of_numbers = 0 # variable for total
    count_numbers = 0 # variable to count the numbers
    while True:
        user_input = input("Enter a number: ")
        if(user_input == "done"): # continue till done is typed
            return total_of_numbers/count_numbers # if done is typed return average
        try:
            user_input = float(user_input) # try converting value to a float - error if string is input
        except:
            print("Enter a valid number")
        else:
            total_of_numbers = total_of_numbers + user_input # add the number - ignores string input
            count_numbers += 1 # increase count - ignores string input





##############################################################################
def main():
    """ Calls the following functions:
        - even_odd()
        - ten_by_ten()
    Prints the following function:
        - find_average()
    """
    even_odd()
    ten_by_ten()
    print("Average is ",find_average())

if __name__ == '__main__':
    main()
