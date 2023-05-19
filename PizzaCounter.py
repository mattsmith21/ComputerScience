# This application takes an input and shows an output depending on that input

print("")
print("=======================================")
print("         PIZZA COUNTER"          )
print("=======================================")
print("")

def main():

    fltSlice = float(input("Enter number of slices desired: "))     #ASKING FOR, AND STOREING SLICE COUNT AS fltSli

    #DETERMINE PIZZA SIZE
    if fltSlice == 8 :
        print("your pizza size will be a small")
        print()
    elif fltSlice == 12:
        print("your pizza size will be a medium")
        print()
    elif fltSlice == 16:
        print("your pizza size will be a large")
        print()
    elif fltSlice == 24:
        print("your pizza size will be an extra large")
        print()
    else:
        print()
        print("our only choices are 8 slices, 12 slices, 16 slices, or 24 slices. ")
        print("please try again :) ")
        print()
        main()      #restarts application ONLY if user enters a bad number
   
main() 