
def main():
    #==================================================================================
    # Var           Type        Its use case
    #-----------------------------------------
    # price_list    list        creates empty list for future use. 
    # intNewPrice   intiger     takes price input
    #==================================================================================
    selection = "Root > "
    print("\n"*3 ,"=" *20, "\n Home Cost Calculator ", "\n", "=" *20, "\n")
    print("E. Enter list editor")
    print("X. Exit Application", "\n")
    #creats empty list
    selection = input("Root > ")
    if selection == "E":
        price_list = [] #create empty list
        intNewPrice = 0
        print('Type -1 when done entering prices')
        while intNewPrice != -1:
            intNewPrice = int(input("House Price: "))
            if intNewPrice != -1: #if not -1, add to list
                price_list.append (intNewPrice)
        print("\n Scores\n" , "-" *20 , "\n") #print scores
        for i in range(len(price_list)): 
            print(str(i+1) + ": " + format(price_list[i], '.2f'))
            print("")
        print("Highest Score: $" + format(max(price_list), '.2f')) #print highest score
        print("Lowest Score: $" + format(min(price_list), '.2f')) #print lowest score
        print("Average Score: $" +  format(sum(price_list)/len(price_list), '.2f')) #print avrage score
        print("")
    elif selection == "X":
        print()
        print('Application ending')
    else:
        input('Not an option, press enter to try again...')
        main()
main()