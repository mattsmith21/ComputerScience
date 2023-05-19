#This program takes an input and compares to a random number and lets the user know if random number is higher or lower than inputed number.

#get and store the random number
import random
RanNum = random.randint(1,100)
Count = 0
 
#check input agenst the random number
Guess = int(input("Enter a number between 1 and 100: ")) #saves input as an intiger
while Guess != RanNum: #while guess is NOT EQUAL to 'RanNum' then 
    Count += 1      #counter = counter + 1 
    if Guess < RanNum:
        print("Answer is Higher") 
        Guess = int(input("Enter a number between 1 and 100: "))
    elif Guess > RanNum:
        print("Answer is Lower")
        Guess = int(input("Enter a number between 1 and 100: "))
Count += 1 #adds 1 to count one last time to make the count accurate
print("You guessed it!") #when user enter the correct number, it will exit the "while Guess != RanNum:" and go this line
print("It took you " + str(Count) + " guess(es)!") #print Count as a string or else will break the program(not qute sure why)