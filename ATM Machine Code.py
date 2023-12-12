class Atm:
    def __init__(self):
        self.pin =""
        self.balance = 0
        
        self.menu()
    
    def menu(self):
        user_input= input("""
                    Hello How Would you Like To Proceed ?
                    1. Enter 1 To Create Pin
                    2. Enter 2 For Deposit
                    3. Enter 3 For Withdrawal
                    4. Enter 4 For Check Balance
                    5. Enter 5 For Exit
                    
        """)
        
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.Deposit()
        elif user_input == "3":
            self.Withdraw()
        elif user_input == "4":
            self.Check_balance()
        elif user_input == "5":
            print("Bye")
            
            
    def create_pin(self):
        self.pin = int(input("Enter Your Pin"))
        print("Pin Created Successfully")

    def Deposit(self):
        temp = input("Enter your Pin")
        if temp == self.pin:
            amount= int(input("Enter the Amount You Want To Deposit"))
            self.balance = self.balance + amount
            print("Deposit Succesfull")

        else:
            print("Invalid Pin")

    def Withdraw(self):
        temp = input("Enter your Pin")
        if temp == self.pin:
            amount = int(input("Enter the amount you want to withdraw"))
            amount = self.balance - amount
            print("Amount Withdrawn Successfully")

        else:
            print("Invalid Pin")

    def Check_balance(self):
        temp = input("Enter Your Pin")
        if temp == self.pin:
            print(self.balance)

        else:
            print("Invalid Pin")