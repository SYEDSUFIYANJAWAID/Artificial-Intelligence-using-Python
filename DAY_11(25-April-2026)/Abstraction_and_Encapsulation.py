class BankAccount:
    bank = "SSJ Bank"

    @staticmethod
    def greet():
        print("THANK YOU FOR CHOOSING SSJ BANK")

    def __init__(self, account_number, name, balance):
        self.__accountnumber = account_number# encapsulation:Data hidden hota hai, but controlled access diya jata hai
        self.__name = name
        self.__balance = balance# private balance:Private ka matlab “hide from direct access” hota hai, “never show” nahi
# user direct access nahi kar sakta p1.__balance ❌  # not allowed

    # Abstraction - deposit
    def deposit(self, amount):
        self.__balance += amount
        print("Deposit Successful")

    # Abstraction - withdraw
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdraw Successful")
        else:
            print("Insufficient Balance")

    # Controlled access (abstraction)
    # def show_balance(self):    Hum controlled way me data dikhate hain
        print("Account Holder:", self.__name)
        print("Bank:", self.bank)
        print("Balance:", self.__balance)


# Object
p1 = BankAccount(12345, "SUFIYAN", 700000)

BankAccount.greet()

p1.deposit(50000)
p1.withdraw(20000)
p1.show_balance()      


# Ek class banao BankAccount
# 🎯 Requirements:
# ek private attribute ho:
# __balance
# 3 methods banao:
# deposit(amount)
# withdraw(amount)
# show_balance()

# class bankaccoount:
#     bank="SSJ bank"

#     @staticmethod
#     def greet():
#         print("THANK YOU FOR CHOSSING SSJ BANK")
    
#     def __init__(self,Account_Number,with_draw,Diposit_Amount,Deposit_Type,name,_balance):
#            self._balance=_balance
#            self.Account_number=Account_Number
#            self.with_draw=with_draw
#            self.Diposit_Amount=Diposit_Amount
#            self.DEposit_Tyoe=Deposit_Type
#            self.name=name
          

#     def show(self):
#      print("The Balance Of ",self.Diposit_Amount,"is Deposit in folling account number:",self.Account_number,"\n""\nWith Draw Amount:",self.with_draw,"\nDiposite Amount:",self.Diposit_Amount , "\nName:",self.name,"\nAccount Number:",self.Account_number,"\nBank:",self.bank,"\n")
      

 
# p1=bankaccoount(12345,0,700000,"cash","SUFIYAN",700000)

# p1.show()

# p1.greet() 