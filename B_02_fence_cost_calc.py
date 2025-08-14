# Ask user for width and loop until they
# enter a number that is more than zero
def num_check(question):

    error = "please enter a number that is more than zero\n"
    while True:

        try:
            # ask the user for a number
            response = float(input(question))

            #check that the number is more than zero
            if response > 0:
               return  response
            else:
                print(error)
        except ValueError:
            print(error)


# Main Routine starts here...

Keep_going = ""
while Keep_going == "":
    # Get width and length
    width = num_check("width: ")
    Length = num_check("Length: ")
    cost = num_check("cost: ")
    

    # Calculate perimeter and price for the fence
    perimerter = 2 * (width + Length)
    price = perimerter * cost


    # Display output
    print()
    print(f"perimeter: {perimerter} units")
    print(f"price: s{price:.2f}")

    # Ask user if they want keep going
    Keep_going = input("please enter to keep going or any key to quit. ")
    print()

print("Thank you for using the area / perimeter calculator")
