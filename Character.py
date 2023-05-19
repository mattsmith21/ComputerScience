def main():   #start of statment
    strCharName = ""
    print()
    print()
    print("Options are:")
    strCharName = input(str("Enter character name and we will return there TV Show: "))
    if strCharName == "Sandy": 
        print("SpongeBob SquarePants")
    elif strCharName == "Cricket": 
        print("Big City Greens") 
    elif strCharName == "Snoopy": 
        print("Peanuts") 
    elif strCharName == "Tilly": 
        print("Big City Greens") 
    elif strCharName == "Patrick": 
        print("SpongeBob SquarePants") 
    elif strCharName == "Lisa": 
        print("The Simpsons") 
    else:
        print("Not a valid input, try again")
    main()  #allous you to loop
main()    #ends the statment

