# banking system using oop
# parent class : user
# holds details about an user
# has a function to show user details

#child class :bank
# stores details about the account balance
# stores details about the amount
# allows for deposite , withdraw , view balance


#Parent Class 
class User() :
    def __init__(self , name , age , gender):
        self.name = name
        self.age = age
        self.gender = gender


    def show_details(self):
        print("Personal details")
        print("")
        print ("Name" , self.name)
        print("Age" , self.age )
        print("Gender" , self.gender)


#Child class
class Bank(User):
    def __init__(self , name , age , gender ):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self , amount) :
        self.amount = amount
        self.balance =  self.balance + amount
        print("Account balance has been updated : ",self.balance)

    def withdraw(self,amount):
        self.amount = amount
        if self.amount >self.balance :
            print("insufficient funds | Balance available : " , self.balance )
        else :
            self.balance  = self.balance - self.amount
            print("updated amount :" , self.balance )

    def view_balance(self) :
        self.show_details()
        print(" amount :" , self.balance )
        
        
