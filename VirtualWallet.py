from CryptoCoins import trading 

"""This while loop allows the user to enter a username and if its wrong it will keep asking
    till they enter the correct username """
# this allows determine the username 
while True:
   username = input("Enter your username: ")
   if username == "Crypto123":
    break
else:
    username = input("Enter your username: ")

#This while loop allows the user to enter a password if its wrong it will say access denied 
 #if the password is not correct it going to keep asking the user to enter the password
# if its right it will let them login 
# this also determine the password 
while True:
 password = input("Enter the password: ")
 if password == "Crypto123":
    print("Access Granted")
    break
else:
  print("Access Denied")

#constructor fot the virtual wallet letting user to deposit, withdraw money and look at their balance 
class Virtual_Wallet:
        def __init__(self):
          self.balance = 0.0 # money balance
          self.balances = {} # stores the balances in a dic 

        def check_balance(self,symbol = None):
           if symbol:
            return self.balances.get(symbol, 0)
           else:
              return self.balance

        def buy(self, symbol, amount, price):
         cost = amount * price
         if cost > self.balance:
            print("Insufficient funds to buy.")
            return
         self.balance -= cost
         if symbol in self.balances:
            self.balances[symbol] += amount
         else:
            self.balances[symbol] = amount
         print(f"Bought {amount} {symbol} for ${cost:.2f}")

        def sell(self, symbol, amount, price):
          if symbol in self.balances and self.balances[symbol] >= amount:
            self.balances[symbol] -= amount
            earnings = amount * price
            self.balance += earnings
            print(f"Sold {amount} {symbol} for ${earnings:.2f}")
          else:
            print(f"Not enough {symbol} to sell")


        def deposit(self, amount):
         if amount >= 0:
          self.balance += amount
          return(f"This {amount} has successfully been deposited")
         else:
          return("Invalid amount")
             
        def withdraw(self, amount):
         if 0 <= amount<= self.balance:
           self.balance -= amount
           return(f"{amount} has successfully been withdraw")
         else:
           return ("Insufficient funds or invalid withdrawal amount")

# this lets the user choice the option on the command line by pressing a number between 1-4
def Wallet_Interaction(wallet):
    while True:
        print( "options:")
        print("1. check Balance")
        print("2. deposit")
        print("3. withdraw")
        print("4. trade crypto")
        print("5. exit")  
        
    
        choice = int(input("choose your option: " ))
           
        if choice ==1:
            print("Current Balance", wallet.check_balance())
    
        elif choice == 2:
             amount = float(input("Enter a deposited amount: "))
             print(wallet.deposit(amount))

        elif choice ==3:
            amount = float(input("Enter a withdraw amount: "))
            print(wallet.withdraw(amount))

        elif choice == 4:
            trading(wallet)

        elif choice ==5:
          print("Exiting....")
          print (" ")
          break
        else: 
          print("Invalid choice please try again")

if __name__ == "__main__":     
  wallet = Virtual_Wallet()
  Wallet_Interaction(wallet)
    



  