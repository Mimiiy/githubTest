import random
from datetime import datetime







def main():
    #Day dd Mon yyyy hh:mm:ss +xxxx
    # Sun 10 May 2015 13:54:36 -0700
    # Sun 10 May 2015 13:54:36 -0000
    #convert days to seconds
    timestamp = int(datetime.now().timestamp())
    print(timestamp)
    pass

def guess():
    value = int(input("Please enter a value: ")) #user enters values

    random_list = []

    #
    random_odd = [*range(1,21,2)]
    random_even = [*range(0,21,2)]


    pass
#challenge 1: Print the list of integers as a string, without spaces.
def return_sequence(value):
    for i in range(1,value+1):
        print(f"{i}", end="")

#challenge 2: create a function that takes in a list and prints in the square of the list
def return_square(x):
    nums = [*range(x)]
    [print(i**2) for i in nums]

#challenge 3: if/else
def return_status(n):
    if n%2 != 0:
        print("Weird")
    if n%2 == 0 and 2 <=n <=5:
        print("Not Weird")
    if n%2 == 0 and 6 <=n <= 20:
        print("Weird")
    if n%2 == 0 and n > 20:
        print("Not Weird")


#challenge 4: find the runner-up score from a list of participants. 

def return_second_highest():
    num = random.randint(2,10)
    participant_scores = [random.randint(-100,100) for _ in range(num)]
    print(participant_scores)
    maximum_score = max(participant_scores)
    runner_up_score = 0

    for score in participant_scores:
        if  runner_up_score < score < maximum_score:
            runner_up_score = score 
    return(runner_up_score)

#print out the absolute difference between timestamps. 

#converts days to seconds 
def days_second():
    pass

def timestamp():
    pass



if __name__ == "__main__":
    main()

