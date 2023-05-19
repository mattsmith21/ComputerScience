def main():
#========================================================
# Variable      Type        Purpose
#========================================================
# strChoice     String      Store the users choice
# fltFinalTotal      float       Total ticket quanity       
    strChoice = ""
    fltTotal = 0  
    while strChoice != "X":

        print("--------------------------------")
        print("Menu of options")
        print("--------------------------------")
        print("")
        print("C: Caculate ticket costs")
        print("D: Display ticket options")
        print("X: Exit application")
        print("")
        strChoice = input("Enter your menu selection: ").upper()
        print("")

        #evaluate choices
        if strChoice == "C":
            fltTotal = CalcCost()
            print("Your grand total is $" + format(fltTotal, '.2f'))
            #wait for user
            print("")
            input("Press enter to continue...")
            print()
        elif strChoice == "D":
            ticketOptions() #call ticketOptions to display  

    print("Application ending")

def ticketOptions():
    #create blank spaces
    print('\n' *5)
    print("------------------")
    print("TICKET OPTIONS")
    print("------------------") 
    print("")
    #display choices
    print("1. Weekday Ticket")
    print("2. Weekend Ticket")
    print("3. Twilight Ticket")
    #wait for user
    print("")
    input("Press enter to continue...")
    print()

def calcSalesTax(subtotal):
    #=============================================================
    # Variable      Type        Purpose
    #=============================================================
    # subtotal          float       Pramerter passed to float
    # fltSalesTaxAmt    float       Sales tax amount
    # fltSalesTaxPct    float       Sales tax percent

    #define variables
    fltSalesTaxAmt = 0
    fltSalesTaxPct = 0.07 
     
    #calculation
    fltSalesTaxAmt = subtotal * fltSalesTaxPct

    #return sales tax amount to function
    return fltSalesTaxAmt

def CalcCost():
    #=============================================================
    # Variable      Type        Purpose
    #=============================================================
    # fltTicketType          float           What ticket the user wants
    # fltPrice               float           Ticket price during weekday
    # intTicketQuanity       integer         Number of tickets wanted
    # fltSalesTax            float           Sales tax amount during function
    # fltSubTotal            float           Subtotal baced on choice and calculations
    # fltGrandTotal          float           Grandtotal baced on choices and calculations

    #define variables
    fltPrice = 0
    intTicketQuanity = 0
    fltSalesTax = 0
    fltSubTotal = 0
    fltGrandTotal = 0
    
    #get input from user
    print("1: Weekday")
    print("2: Weekend")
    print("3: Twilight")
    fltTicketType = int(input("What kind of ticket do you want? "))
    print()
    if fltTicketType == 1:
        fltPrice = 38.00
    elif fltTicketType == 2:
        fltPrice = 42.00
    elif fltTicketType == 3:
        fltPrice = 24.00
    intTicketQuanity = int(input("How many tickets do you want? "))

    #calculate subtotal
    fltSubTotal = fltPrice * intTicketQuanity

    #get tax amount
    fltSalesTax = calcSalesTax(fltSubTotal)
    #calculate grand total
    fltGrandTotal = fltSalesTax + fltSubTotal
    #return grand total
    return fltGrandTotal    
main()