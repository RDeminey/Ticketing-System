TICKET_PRICE = 10

tickets_remaining = 100 

SERVICE_CHARGE = 2

def calculate_price(amount_of_tickets):
    return (amount_of_tickets * TICKET_PRICE) + SERVICE_CHARGE
    
    
while tickets_remaining >= 1:
    print("There are {} tickets remaining.".format(tickets_remaining))
    name = input("What is your name:    ")
    amount_of_tickets = input("How many tickets would you like, {}?    ".format(name))
    try:
        amount_of_tickets = int(amount_of_tickets)
        if amount_of_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
            
    except ValueError as err:
        
        print ("Oh No, we ran into an issue. {}.  Please try again".format(err))
    else:
        order_price = calculate_price(amount_of_tickets)
        
        print("The total for your order will be ${}".format(order_price))
        
        user_election = input("Do you want to proceed? Y/N     ")
        
          #TODO:Gather credit card information and process it.
        if user_election.lower() == "y":
            print ("SOLD!")
            tickets_remaining = tickets_remaining - int(amount_of_tickets)
            print ("There are now {} tickets remaining".format(tickets_remaining))
           
        else:
            print("Thank you {}, maybe next time.".format(name))
 
print ("Sorry, all the tickets are sold out")
