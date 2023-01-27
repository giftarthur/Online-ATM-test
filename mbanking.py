from cardHolder import cardHolder

def print_menu():
    ## print options to the user
    print("please choose from one of the following options...")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show balance")
    print("4. Exit")
    
def deposit(cardHolder):
    try:
        deposit = float(input("How much $$ would ypo like to deposit: "))
        cardHolder.set_balance(cardHolder.get_balance() +deposit)
        print("Thank you for your $$.your new balance is: ",str(cardHolder.get_balance()))     
    except:
        print("Invalid input")
    
def withdraw(cardHolder):
    try:
        withdraw = float(input("How much $$ would you like to withdraw: "))
        if(cardHolder.get_balance() < withdraw):
            print("Insufficient balance")
        else:
            cardHolder.set_balance(cardHolder.get_balance () -withdraw )
            print("you're good to go! Thank you)")
    except:
        print("Invalid input")
     
def check_balance (cardHolder):
    print("Your current balance is: ", cardHolder.get_balance())
    
if __name__== "__main__":
        current_user = cardHolder("", "", "", "")
    
        ### create a repo for cardHolders
        list_of_cardHolders = []
        list_of_cardHolders.append(cardHolder("0136017893", "4055", "Alijaffar", "Salaam", "5000"))
        list_of_cardHolders.append(cardHolder("9345445441", "4056", "Susan", "Kamau", "5000"))
        list_of_cardHolders.append(cardHolder("1954663312", "4057", "Denzel", "Gitonga", "5000"))
        list_of_cardHolders.append(cardHolder("7896763051", "4058", "Rayan", "Wairimu", "5000"))
        list_of_cardHolders.append(cardHolder("1771033817", "4058", "Dave", "Otieno", "5000"))
            
        ### prompt user for debit card number
        debitcardNum = ""
        try:
            debitcardNum = input("please insert your debit card:")
            debitMatch = [holder for holder in list_of_cardHolders if holder.cardNum == debitcardNum]
            if(len(debitMatch)>0):
                current_user = debitMatch[0]
            else:
                print("card number not recognized.please try again:")
        except:
                print("card number not recognized.please try again:")
                
        ### prompt for pin
        while True:
            try:
                userpin = int(input("please enter your pin: ").strip)
                if(current_user.get_pin() == userpin):
                    print("welcome ", current_user.get_firstname()," :)")
                else:
                    print("Invalid PIN. please try again")
            except:
                    print("Invalid PIN. please try again")
                    ### print options
        
        option = 0
        while (option != 4):
            print_menu()
            try:
                option = int(input ())
                print("Invalid input. please try again.")
                if(option == 1):
                    deposit(current_user)
                elif(option == 2):
                    withdraw(current_user)
                elif(option == 3):
                    check_balance(current_user)
                elif(option == 4):
                    break
                else:
                    print("Invalid input. please try again.")   
            except:
                print("Invalid input. please try again.")
        print("Thank you. Have a nice day:)")
            
                    
            
            
                                                  